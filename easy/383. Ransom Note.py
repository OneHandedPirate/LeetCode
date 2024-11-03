# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
#
#
#
# Example 1:
#
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
#
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
#
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
#
#
# Constraints:
#
# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.

from collections import Counter


def canConstruct(ransomNote: str, magazine: str) -> bool:
    note_count = Counter(ransomNote)
    mag_count = Counter(magazine)
    for letter in note_count:
        if not mag_count.get(letter) or note_count[letter] > mag_count[letter]:
            return False
    return True


# without hashmaps
# def canConstruct(ransomNote: str, magazine: str) -> bool:
#     for i in ransomNote:
#         if i not in magazine:
#             return False
#         magazine = magazine.replace(i, '', 1)
#     return True


assert canConstruct("a", "b") is False
assert canConstruct("aa", "ab") is False
assert canConstruct("aa", "aab") is True
