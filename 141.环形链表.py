# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 快慢指针
        # 如果链表没有环：快指针 fast 会最先走到链表的尽头（即 fast == None 或 fast.next == None）。此时直接返回 False。

        # 如果链表有环：快指针 fast 一定会先进入环，并在环内一直转圈。慢指针 slow 随后也会进入环。因为 fast 每次比 slow 多走 1 步，所以两者的距离会越来越近，最终一定会在环内的某个节点相遇（即 slow == fast）。此时返回 True。
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False