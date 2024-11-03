# Given a string s consisting of words and spaces, return the length of the last
# word in the string.
#
# A word is a maximal
# substring
#  consisting of non-space characters only.
#
#
#
# Example 1:
#
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:
#
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:
#
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.


# simplest solution
# def lengthOfLastWord(s: str) -> int:
#     return len(s.split()[-1])


def lengthOfLastWord(s: str) -> int:
    s = s.rstrip()
    _len = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == " ":
            return _len
        _len += 1
    return _len


assert lengthOfLastWord("Hello World") == 5
assert lengthOfLastWord("   fly me   to   the moon  ") == 4
assert lengthOfLastWord("luffy is still joyboy") == 6
