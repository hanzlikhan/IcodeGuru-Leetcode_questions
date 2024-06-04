class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeroCnt = 0
        lngwin = 0
        start = 0
        for i in range(0,len(nums)):
            zeroCnt += (nums[i]==0)
            while zeroCnt > 1:
                zeroCnt -= (nums[start]==0)
                start+=1
            lngwin = max(lngwin,i-start)
        return lngwin