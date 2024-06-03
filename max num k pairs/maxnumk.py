class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        nums.sort()
        lf = 0
        rt = len(nums)-1
        while lf<rt:
            if nums[lf]+nums[rt] > k:
                rt = rt-1
            elif nums[lf]+nums[rt] < k:
                lf = lf+1
            else:
                lf+=1
                rt-=1
                ans += 1
        return ans