# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You
# may assume that the majority element always exists in the array.
#
# Example 1:
#
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
#
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
#
#
# Follow-up: Could you solve the problem in linear time and in O(1) space?


def majorityElement(nums: list[int]) -> int:
    n = len(nums) / 2
    for elem in set(nums):
        if nums.count(elem) > n:
            return elem


# optimal solution, not mine
# def majorityElement(nums: list[int]) -> int:
#         nums.sort()
#         n = len(nums)
#         return nums[n // 2]


assert majorityElement([3, 2, 3]) == 3
assert majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
