class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        lf = r = 0
        q = collections.deque()
        while r<len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if lf>q[0]:
                q.popleft()
            if (r+1) >=k:
                output.append(nums[q[0]])
                lf+=1
            r+=1
        return output
        