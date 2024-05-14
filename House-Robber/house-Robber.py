class solution
    def rob(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)-1
        sum1 = 0
        sum2 = 0
        tem = 0
        
        sum3 = 0
        res1=0
        while i<=n:
            
            sum1 += nums[i] 
            
            i+=2
            tem = i+1
            sum3 +=nums[tem]
            res1 = max(sum3,sum1)
        k = 1
        res2 = 0
        while k<=n:
            sum2 += nums[k]
            k+=2
            i+=2
            tem = i+1
            sum3 +=nums[tem]
            res2= max(sum3,sum2)
        return max(sum1,sum2)
            