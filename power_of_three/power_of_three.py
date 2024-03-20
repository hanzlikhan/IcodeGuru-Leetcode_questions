class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        num = 1
        while num <= n:
            if num == n:
                return True
            num *= 3
        
        return False

# Example usage:
solution = Solution()
result = solution.isPowerOfThree(27)
print(result)  # Output: True
