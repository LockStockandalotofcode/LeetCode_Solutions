# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1

        ptr1, ptr2 = l1, l2
        dummy = dummy_head = ListNode(0)
        carry = 0
        while ptr1 and ptr2:
            curr_sum = ptr1.val + ptr2.val + carry
            if curr_sum > 9:
                carry = 1
            else:
                carry = 0

            dummy.next = ListNode(curr_sum % 10)
            dummy = dummy.next
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        while ptr1:
            curr_sum = ptr1.val + carry
            if curr_sum > 9:
                carry = 1
            else:
                carry = 0

            dummy.next = ListNode(curr_sum % 10)
            dummy = dummy.next
            ptr1 = ptr1.next

        while ptr2:
            curr_sum = ptr2.val + carry
            if curr_sum > 9:
                carry = 1
            else:
                carry = 0

            dummy.next = ListNode(curr_sum % 10)
            dummy = dummy.next
            ptr2 = ptr2.next

        if carry != 0:
            dummy.next = ListNode(carry)
            dummy = dummy.next
        
        return dummy_head.next