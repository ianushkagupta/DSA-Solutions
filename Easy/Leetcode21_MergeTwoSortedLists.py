# https://leetcode.com/problems/merge-two-sorted-lists/description/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        current = head

        while list1 and list2:
            if list1.val< list2.val:
                current.next = list1
                list1 = list1.next
            elif list1.val == list2.val:
                current.next = list1
                list1 = list1.next
                current = current.next
                current.next = list2
                list2 = list2.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2

        return head.next
        