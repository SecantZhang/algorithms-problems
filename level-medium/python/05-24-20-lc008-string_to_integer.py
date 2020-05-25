"""
Date: 05-24-20
Problem: LeetCode 008
Title: String to integer
Description: https://leetcode.com/problems/string-to-integer-atoi/
"""

class Solution:
    def myAtoi(self, str: str) -> int:
        try: 
            split = str.lstrip(" ")
            ans, split = [split[0]], split[1:]
            if ans[0] not in ["-", "+"] and not ans[0].isdigit():
                return 0

            for char in split: 
                if not char.isdigit(): 
                    break
                else: 
                    ans.append(char)
            ans = int("".join(ans))
            return ans if abs(ans) <= (2147483648 - 1) else [2147483647, -2147483648][ans <= 0]

        except IndexError:
            return 0
        except ValueError:
            return 0


if __name__ == "__main__":
    sol = Solution()

    testcases = {
        "42": 42, 
        "-42": -42, 
        "4193 with words": 4193, 
        "words and 987": 0, 
        "-91283472332": -2147483648, 
        "3.14159": 3, 
        "": 0, 
        "+-2": 0,
        "  -0012a42": -12,
        "-": 0
    }

    for key in testcases: 
        print("Checking key {}".format(key))
        ans = sol.myAtoi(key)
        assert ans == testcases[key], "Error at key: {} - type: {}, with answer: {} - type: {}".format(key, type(key), ans, type(ans))