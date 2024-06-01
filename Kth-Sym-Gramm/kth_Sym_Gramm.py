class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # Start from the first row
        k -= 1
        # Initialize the result to 0
        result = 0
        while n > 0:
            # Toggle the result if k is odd
            if k & 1:
                result ^= 1
            # Right shift k by 1 and decrement n
            k >>= 1
            n -= 1
        return result