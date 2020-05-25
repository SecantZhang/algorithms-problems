"""
Date: 05-21-20
Problem: LeetCode 007
Title: Reverse Integer
Description: Given a 32-bit signed integer, reverse digits of an integer.
"""


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        raw_int = sign * x
        str_x = str(raw_int)
        result = int("".join([str_x[i] for i in range(len(str_x) - 1, -1, -1)]))
        return 0 if(abs(result) > (2 ** 31 - 1)) else sign * result