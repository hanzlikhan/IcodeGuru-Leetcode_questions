class Solution:
    def arrangeCoins(self, n: int) -> int:
        lf, rt = 0, n
        while lf <= rt:
            mid = lf + (rt - lf) // 2
            total = (mid * (mid + 1)) // 2
            if total == n:
                return mid
            elif total < n:
                lf = mid + 1
            else:
                rt = mid - 1
        return rt  # returning rt instead of mid outside the loop
