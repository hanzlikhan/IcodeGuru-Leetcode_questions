class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        value = set()
        l = 0
        for i in range(len(nums)):
            if i-l>k:
                value.remove(nums[l])
                l+=1
            if nums[i] in value:
                return True
            value.add(nums[i])
        return False
        