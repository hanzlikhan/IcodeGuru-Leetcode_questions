class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = 0
        for ele in digits:
            n = (n*10) + ele
        n = n+1
        digit = []
        while n>0:
            digit.insert(0,n%10)
            n//=10
        return digit
        