# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        hash_map = {}
        i = 0
        curr = head
        while curr:
            hash_map[i] = curr.val
            i+=1
            curr = curr.next
        start = 0
        maxSum = 0
        end = i-1
        while start<end:
            maxSum = max(maxSum, hash_map.get(start)+hash_map.get(end))
            start+=1
            end-=1
        return maxSum