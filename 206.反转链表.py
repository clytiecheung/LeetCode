# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        # 迭代法 
        # 在遍历链表的过程中，边走边改变指针的方向。把原本指向下一个节点的 next 指针，改为指向上一个节点。
        # 为了防止改指针的时候丢失后面的节点，我们需要三个指针：
        # prev：指向前一个节点（初始为 None，因为反转后，原本的头节点将变成尾节点，指向空）。
        # curr：指向当前正在处理的节点（初始为 head）。
        # next_temp：用于提前保存当前节点的下一个节点（防止断链后找不到后面的路）。

        # prev = None
        # curr = head
        # while curr:
        #     next_temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next_temp
        # return prev


        # 递归法
        # 递归终止条件：如果链表为空，或者只有一个节点，直接返回
        if not head or not head.next:
            return head

        # 递归反转 head.next 之后的链表，返回反转后的新头节点
        new_head = self.reverseList(head.next)

        # 此时 head.next 是原链表的下一个节点，也是反转后链表的尾节点
        # 让它的 next 指向 head，实现反转
        head.next.next = head

        # 将当前节点的 next 置为 None（防止形成环）
        head.next = None
        
        return new_head

