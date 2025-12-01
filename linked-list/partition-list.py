# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        left = ListNode()
        right = ListNode()
        ldummy, rdummy = left, right

        while head:
            if head.val < x:
                ldummy.next = head
                ldummy = ldummy.next
            else:
                rdummy.next = head
                rdummy = rdummy.next
            head = head.next

        ldummy.next = right.next 
        rdummy.next = None

        return left.next