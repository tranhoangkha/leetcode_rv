class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        
        for i in range(len(prices) -1 ):
            time =0
            for j in range(i+1,len(prices)):
                
                if prices[i] >= prices[j] :
                    
                    prices[i] -= prices[j]
                    break
        return prices
    
prices = [8,4,6,2,3]
Solution = Solution()
print(Solution.finalPrices(prices))