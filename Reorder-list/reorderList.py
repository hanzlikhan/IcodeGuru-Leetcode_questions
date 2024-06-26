class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None
        
        while second:
            temp = second.next
            second.next = prev 
            prev = second 
            second = temp
        second = prev
        first = head
        while second:
            temp1,temp2 = first.next , second.next
            first.next = second
            second.next = temp1
            first , second = temp1,temp2
        
        