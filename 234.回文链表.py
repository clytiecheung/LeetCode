# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # 1.快慢指针找中点，slow走一步，Fast走两步，最后slow在中点（偶数节点时偏左），fast在最后
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 2.反转链表，注意此处不能用递归反转（空间复杂度O(N)），只能用迭代反转（空间复杂度O(1)）
        prev = None
        curr = slow.next
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        # 3.对比前半段和反转后的后半段
        p1 = head
        p2 = prev
        res = True
        while p2:
            if p1.val != p2.val:
                res = False
                break
            p1 = p1.next
            p2 = p2.next

        # 4.恢复链表
        curr = prev
        prev = None
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        slow.next = prev
        return res