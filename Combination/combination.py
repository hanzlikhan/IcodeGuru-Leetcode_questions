class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        for i in range(1,n+1):
            ans.append(i)
        return combinations(ans,k)