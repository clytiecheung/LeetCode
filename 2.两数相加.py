# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0) # 这里数字没有影响，最后输出的是dummy.next，不会输出这个数字
        curr = dummy
        carry = 0 # 进位
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x + y +carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next