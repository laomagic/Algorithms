'''
题目：定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
'''
"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """

    def reverse(self, head):
        # write your code here
        new_head = None
        while head is not None:
            temp = head.next
            head.next = new_head
            new_head = head
            head = temp
        return new_head
