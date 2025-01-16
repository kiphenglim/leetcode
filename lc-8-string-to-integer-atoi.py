class Solution:
    def myAtoi(self, s: str) -> int:
        out = ""

        s = s.strip()

        isNeg = False
        if s.startswith(("+", "-")):
            isNeg = s.startswith("-")
            s = s[1:]

        s = s.lstrip("0")
        if len(s) == 0:
            return 0

        for char in s:
            if not char.isdigit():
                break
            out += char

        if out == "":
            out = 0
        out = int(out)
        if isNeg:
            out = -out

        if out < -(2**31):
            out = -(2**31)
        if out > 2**31 - 1:
            out = 2**31 - 1

        return out
