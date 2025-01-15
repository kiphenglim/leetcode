"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.
"""

from __future__ import annotations
from typing import Any, Iterable, Optional
import unittest


# Definition for singly-linked list.
class ListNode(Iterable[Any]):
    @staticmethod
    def nodify(l: list[Any]) -> ListNode:
        if l == []:
            return ListNode()

        head = ListNode(val=l[0])
        if len(l) == 1:
            return head
        node = head

        for i in range(1, len(l)):
            next = ListNode(val=l[i])
            node.next = next
            node = next

        return head

    @staticmethod
    def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = None
        node = head
        while node != None:
            next = node.next
            node.next = prev
            prev = node
            node = next
        return prev

    def __init__(self, val: Any = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next

    def __iter__(self):
        node = self
        while node:
            yield node.val
            node = node.next

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        node1 = self
        node2 = other
        while node1 != None and node2 != None:
            if node1.val != node2.val:
                return False
            node1 = node1.next
            node2 = node2.next
        # works since we expect both to be None if they're equal
        return node1 == None and node2 == None

    def __str__(self) -> str:
        out = ""
        for nodeVal in self:
            out += f"{nodeVal} "
        return out.strip()


class Solution:
    @staticmethod
    def pruneLeadingZeros(list: Optional[ListNode]) -> ListNode:
        node = list if list else ListNode()
        if node.val == 0 and node.next != None:
            node = node.next
        return node

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        out = ListNode()
        list1 = ListNode.reverse(l1)
        list2 = ListNode.reverse(l2)
        place = out
        carry = 0

        while list1 != None and list2 != None:
            place_sum = list1.val + list2.val + carry
            place.val = place_sum % 10
            carry = place_sum // 10
            next = ListNode()
            place.next = next
            list1 = list1.next
            list2 = list2.next
            place = next

        if list1 != None:
            if carry != 0:
                list1.val += carry
            place.next = list1

        if list2 != None:
            if carry != 0:
                list2.val += carry
            place.next = list2

        return Solution.pruneLeadingZeros(ListNode.reverse(out))


class TestListNode(unittest.TestCase):
    def testEq(self) -> None:
        list1 = ListNode(
            val=0, next=ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3)))
        )
        list2 = ListNode(
            val=0, next=ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3)))
        )
        self.assertEqual(list1, list2, f"expected {list(list1)}, got {list(list2)}")

    def testNeq(self) -> None:
        list1 = ListNode(val=0, next=ListNode(val=1, next=ListNode(val=2)))
        list2 = ListNode(
            val=0, next=ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3)))
        )
        self.assertNotEqual(list1, list2, f"expected {list(list1)}, got {list(list2)}")
        list1 = ListNode(val=0, next=ListNode(val=1))
        list2 = ListNode(
            val=0, next=ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3)))
        )
        self.assertNotEqual(list1, list2, f"expected {list(list1)}, got {list(list2)}")

    def testIter(self) -> None:
        nodeList = ListNode(
            val=0, next=ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3)))
        )
        expectedList = [0, 1, 2, 3]
        outputList: list[Any] = []
        for node in nodeList:
            outputList.append(node)
        self.assertEqual(outputList, expectedList)

    def testNodeListifyMany(self) -> None:
        nodeList = ListNode(val=0, next=ListNode(val=1, next=ListNode(val=2)))
        l = list(nodeList)
        self.assertEqual(l, [0, 1, 2], "expected [0,1,2], got {l}".format(l=l))

    def testListNodifyOne(self) -> None:
        l = [0]
        nodeList = ListNode.nodify(l)
        self.assertEqual(
            nodeList,
            ListNode(val=0),
            "expected [0], got {}".format(list(nodeList)),
        )

    def testListNodifyMany(self) -> None:
        l = [0, 1, 2]
        nodeList = ListNode.nodify(l)
        self.assertEqual(
            nodeList,
            ListNode(val=0, next=ListNode(val=1, next=ListNode(val=2))),
            "expected [0, 1, 2], got {}".format(list(nodeList)),
        )

    def testReverseOne(self) -> None:
        nodeList = ListNode(val=1)
        nodeList = ListNode.reverse(nodeList)
        expected = ListNode(val=1)
        self.assertEqual(
            nodeList,
            expected,
            f"expected {expected}, got {nodeList}",
        )

    def testReverseTwo(self) -> None:
        result = ListNode(val=0, next=ListNode(val=1))
        result = ListNode.reverse(result)
        expected = ListNode(val=1, next=ListNode(val=0))
        self.assertEqual(
            result,
            expected,
            f"expected {expected}, got {result}",
        )

    def testReverseMany(self) -> None:
        result = ListNode(
            val=0,
            next=ListNode(
                val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4)))
            ),
        )
        result = ListNode.reverse(result)
        expected = ListNode(
            val=4,
            next=ListNode(
                val=3, next=ListNode(val=2, next=ListNode(val=1, next=ListNode(val=0)))
            ),
        )
        self.assertEqual(
            result,
            expected,
            f"expected {expected}, got {result}",
        )


class TestAddTwoNumbers(unittest.TestCase):
    def testAddTwoNumbers(self) -> None:
        sol: Solution = Solution()
        list1 = ListNode.nodify([2, 4, 3])
        list2 = ListNode.nodify([5, 6, 4])
        res = sol.addTwoNumbers(list1, list2)
        exp = ListNode.nodify([8, 0, 7])
        self.assertEqual(res, exp, f"expected {exp}, got {res}")

        list1 = ListNode.nodify([0])
        list2 = ListNode.nodify([0])
        res = sol.addTwoNumbers(list1, list2)
        exp = ListNode.nodify([0])
        self.assertEqual(
            sol.addTwoNumbers(list1, list2), res, f"expected {exp}, got {res}"
        )

        list1 = ListNode.nodify([5])
        list2 = ListNode.nodify([5])
        res = sol.addTwoNumbers(list1, list2)
        exp = ListNode.nodify([1, 0])
        self.assertEqual(
            sol.addTwoNumbers(list1, list2), res, f"expected {exp}, got {res}"
        )

        list1 = ListNode.nodify([1, 0])
        list2 = ListNode.nodify([1])
        res = sol.addTwoNumbers(list1, list2)
        exp = ListNode.nodify([1, 1])
        self.assertEqual(
            sol.addTwoNumbers(list1, list2), res, f"expected {exp}, got {res}"
        )

        list1 = ListNode.nodify([9, 9, 9, 9, 9, 9, 9])
        list2 = ListNode.nodify([9, 9, 9, 9])
        res = sol.addTwoNumbers(list1, list2)
        exp = ListNode.nodify([8, 9, 9, 9, 0, 0, 0, 1])
        self.assertEqual(
            sol.addTwoNumbers(list1, list2), res, f"expected {exp}, got {res}"
        )


if __name__ == "__main__":
    unittest.main()
