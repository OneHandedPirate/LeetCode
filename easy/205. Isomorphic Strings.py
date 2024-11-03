# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character, but a character may map to itself.
#
#
#
# Example 1:
#
# Input: s = "egg", t = "add"
# Output: true
# Example 2:
#
# Input: s = "foo", t = "bar"
# Output: false
# Example 3:
#
# Input: s = "paper", t = "title"
# Output: true
#
#
# Constraints:
#
# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.


def isIsomorphic(s: str, t: str) -> bool:
    map1, map2 = [], []

    for c1, c2 in zip(s, t):
        map1.append(s.index(c1))
        map2.append(t.index(c2))
    return map1 == map2


assert isIsomorphic("egg", "add") is True
assert isIsomorphic("foo", "bar") is False
assert isIsomorphic("paper", "title") is True
