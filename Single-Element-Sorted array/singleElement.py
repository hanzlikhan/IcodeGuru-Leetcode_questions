class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lf,r = 0, len(nums)-1
        while lf<r:
            mid = (lf+r)//2
            if (mid%2==1 and nums[mid-1]==nums[mid]) or (mid%2==0 and nums[mid] == nums[mid+1]):
                lf = mid+1
            else:
                r = mid
        return nums[lf]