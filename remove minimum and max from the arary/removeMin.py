def minimum_deletions(nums):
    # min_index = 0
    # max_index = 0
    # min_num = float('inf')
    # max_num = float('-inf')
    
    # for i in range(len(nums)):
    #     if nums[i] > max_num:
    #         max_num = nums[i]
    #         max_index = i
    #     if nums[i] < min_num:
    #         min_num = nums[i]
    #         min_index = i
    min_index = nums.index(min(nums))
    max_index = nums.index(max(nums))
    
    n_deletions = 0
    
    # both from left
    n_deletions = max(min_index, max_index) + 1
    
    # both from right
    deletions_from_right = len(nums) - min(min_index, max_index)
    n_deletions = min(n_deletions, deletions_from_right)
    
    # min_index from left and max_index from right
    deletions_from_left = min(min_index, max_index) + 1
    deletions_from_right = len(nums) - max(min_index, max_index)
    total_deletions = deletions_from_left + deletions_from_right
    
    n_deletions = min(n_deletions, total_deletions)
    
    return n_deletions

# Example usage:
nums = [2,10,7,5,4,1,8,6]
print(minimum_deletions(nums))
