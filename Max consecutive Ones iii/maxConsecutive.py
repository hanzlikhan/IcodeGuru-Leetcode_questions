class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        zerocnt = 0
        max_win = 0
        
        for end in range(len(nums)):
            if nums[end] == 0:
                zerocnt+=1
            while zerocnt > k:
                if nums[start] == 0:
                    zerocnt -= 1
                start+=1
            max_win = max(max_win,end-start+1)
        return max_win
                    
            