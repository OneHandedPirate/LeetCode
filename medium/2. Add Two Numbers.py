# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a
# single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.

# Example 1:
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
#
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#
#
# Constraints:
#
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# TODO: not optimal at all
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    num1 = num2 = ""

    while l1 is not None:
        num1 += str(l1.val)
        l1 = l1.next

    while l2 is not None:
        num2 += str(l2.val)
        l2 = l2.next

    res: int = int(num1[::-1]) + int(num2[::-1])

    head: Optional[ListNode] = None
    previous_node: Optional[ListNode] = None

    for i in str(res)[::-1]:
        node = ListNode(int(i))
        if head is None:
            head = node
        else:
            previous_node.next = node
        previous_node = node

    return head