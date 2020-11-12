"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
"""


class Solution:
    def toLowerCase(self, str: str) -> str:
        res = ""
        for char in str:
            charCode = ord(char)
            if 65 <= charCode <= 90:
                res += chr(charCode + 32)
            else:
                res += char
        return res
