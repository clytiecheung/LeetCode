# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        GroupPrev = dummy

        while True:
            kth = GroupPrev
            for _ in range(k):
                kth = kth.next
                if kth == None:
                    return dummy.next
            GroupNext = kth.next
            prev = GroupNext
            curr = GroupPrev.next
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr 
                curr = nxt
            tmp = GroupPrev.next
            GroupPrev.next = kth
            GroupPrev = tmp
        return dummy.next
        