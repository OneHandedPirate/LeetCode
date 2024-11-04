# Given a string s which consists of lowercase or uppercase letters, return the length of the longest
# palindrome
#  that can be built with those letters.
#
# Letters are case sensitive, for example, "Aa" is not considered a palindrome.
#
#
#
# Example 1:
#
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:
#
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
#
#
# Constraints:
#
# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.
from collections import Counter


def longestPalindrome(s: str) -> int:
    _counter = Counter(s)
    odd_sum = sum([(val // 2) * 2 for val in _counter.values() if val > 1])
    return min(odd_sum + (1 if any(i > 2 and i % 2 == 1 for i in  _counter.values()) or [[i for i in _counter.values() if (i % 2 == 1 or i > 2)]] else 0), len(s))


assert longestPalindrome("abccccdd") == 7
assert longestPalindrome("a") == 1
assert longestPalindrome("ccc") == 3
assert longestPalindrome("bb") == 2