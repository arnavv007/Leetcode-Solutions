class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        i = 0
        discounted_prices = []
        while(i<len(prices)):
            item = prices[i]
            j = i+1
            while j < len(prices):
                discount = prices[j]
                if prices[j] <= item:
                    discounted_prices.append(item - discount)
                    break
                j += 1
            if(j==len(prices) and i==len(discounted_prices)):
                discounted_prices.append(item)
            i+=1
        return discounted_prices

print(Solution.finalPrices(Solution, [10,1,1,6]))
