# Given a sorted array of distinct integers and a target value, return the index
# if the target is found. If not, return the index where it would be if it were
# inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
#
# Example 1:
#
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:
#
# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:
#
# Input: nums = [1,3,5,6], target = 7
# Output: 4
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104


def searchInsert(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid - 1
        elif nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1

    return l


assert searchInsert([1, 3, 5, 6], 5) == 2
assert searchInsert([1, 3, 5, 6], 2) == 1
assert searchInsert([1, 3, 5, 6], 7) == 4
