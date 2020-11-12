"""
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.
"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l_occur = r_occur = total = 0
        for char in s:
            if char == 'L':
                l_occur += 1
            elif char == 'R':
                r_occur += 1
            if l_occur > 0 and l_occur == r_occur:
                total += 1
        return total
