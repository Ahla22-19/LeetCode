# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:

            if l1:
                v1 = l1.val
            else:
                v1 = 0

            if l2:
                v2 = l2.val
            else:
                v2 = 0

            res = v1 + v2 + carry
            carry = res // 10
            res = res % 10
            cur.next = ListNode(res)

            cur = cur.next
            if l1:
                l1 = l1.next
            else:
                None
            if l2:
                l2 = l2.next
            else:
                None

        return dummy.next


        