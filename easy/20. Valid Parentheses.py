# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
# Example 1:
#
# Input: s = "()"
# Output: true
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
# Example 3:
#
# Input: s = "(]"
# Output: false
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


def isValid(s: str) -> bool:
    brackets = {"[": "]", "{": "}", "(": ")"}

    stk = []

    for bracket in s:
        if bracket in brackets:
            stk.append(bracket)
        else:
            if len(stk) == 0 or bracket != brackets[stk.pop()]:
                return False

    return len(stk) == 0


assert isValid("()[]{}") is True
assert isValid("(]") is False
assert isValid("()") is True
