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
        if l == []: return ListNode()

        head = ListNode(val=l[0])
        if len(l) == 1: return head
        node = head

        for i in range(1, len(l)):
            next = ListNode(val=l[i])
            node.next = next
            node = next

        return head


    def __init__(self, val: Any = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next

    def __iter__(self):
        node = self
        while node != None:
            yield node.val
            node = node.next

    def __eq__(self, other: object) -> bool:
        print(self.__class__)
        print(other.__class__)
        if not isinstance(other, ListNode):
            return NotImplemented
        node1 = self
        node2 = other
        while node1 != None and node2 != None:
            if node1.val != node2.val:
                return False
            node1 = node1.next
            node2 = node2.next
        return not (node1 == None and node2 == None)

    def __str__(self) -> str:
        out = ""
        for nodeVal in self:
            out += f"{nodeVal} "
        return out

    def reverse(self) -> ListNode:
        prev = self
        node = self.next
        while node != None:
            next = node.next
            node.next = prev
            prev = node
            node = next
        return prev

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return ListNode(val=0, next=None)

class TestListNode(unittest.TestCase):
    def testIter(self) -> None:
        nodeList = ListNode(val=0, next=ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3))))
        expectedList = [0,1,2,3]
        outputList: list[Any] = []
        for node in nodeList:
            outputList.append(node)
        self.assertEqual(outputList, expectedList)

    def testEq(self) -> None:
        list1 = ListNode(val=0, next=ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3))))
        list2 = ListNode(val=0, next=ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3))))
        print(list1)
        print(list2)
        self.assertEqual(list1, list2, f"expected {list(list1)}, got {list(list2)}")

    def testNodeListifyMany(self) -> None:
        nodeList = ListNode(val=0, next=ListNode(val=1, next=ListNode(val=2)))
        l = list(nodeList)
        self.assertEqual(l, [0,1,2], "expected [0,1,2], got {l}".format(l=l))

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
        nodeList = ListNode(val=1, next=None)
        self.assertEqual(
            nodeList.reverse(),
            nodeList,
            "expect [1], got {}".format(list(nodeList)),
        )

    def testReverseTwo(self) -> None:
        reversed = ListNode(val=1, next=ListNode(val=2)).reverse()
        expected = ListNode(val=2, next=ListNode(val=1))
        self.assertEqual(
            reversed,
            expected,
            "expected {}, got {}".format(list(expected), list(reversed)),
        )

class TestAddTwoNumbers(unittest.TestCase):
    def testAddTwoNumbers(self) -> None:
        sol: Solution = Solution()
        list1 = ListNode.nodify([2,4,3])
        list2 = ListNode.nodify([5,6,4])
        ans = sol.addTwoNumbers(list1, list2)
        print(ans)
        exp = [7,0,8]
        self.assertEqual(list(ans), exp, "342 + 465 = 807")

        list1 = ListNode.nodify([0])
        list2 = ListNode.nodify([0])
        res = [0]
        self.assertEqual(list(sol.addTwoNumbers(list1, list2)), res, "0 + 0 = 0")

        list1 = ListNode.nodify([9,9,9,9,9,9,9])
        list2 = ListNode.nodify([9,9,9,9])
        res = [8,9,9,9,0,0,0,1]
        self.assertEqual(list(sol.addTwoNumbers(list1, list2)), res, "9999999 + 9999 = 89990001")

if __name__ == "__main__":
    unittest.main()
