# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        # 双指针法
        # 让指针 A 走完链表 A 后，去走链表 B；让指针 B 走完链表 B 后，去走链表 A。
        # 链表 A 的独立部分长度为 a，相交部分长度为 c。
        # 链表 B 的独立部分长度为 b，相交部分长度为 c。
        # 指针 A 走过的总路程：a + c + b
        # 指针 B 走过的总路程：b + c + a
        # 你会发现，它们走过的总路程是一样的！ 所以它们一定会同时到达相交节点。
        # 如果两个链表不相交，它们会同时走到两个链表的末尾（null），这时循环结束，返回 null。
        if not headA or not headB:
            return None
        pA = headA
        pB = headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA