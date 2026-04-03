class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit=0
        # for i in range(len(prices)):
        #     for j in range(i,len(prices)):
        #         profit=max(profit,prices[j]-prices[i])
   
        # return profit
        #不是吧大人人，我写的这么好了还超时呢
        profit=0
        mini=prices[0]
        for i in prices:
            mini=min(i,mini)
            profit=max(profit,i-mini)
        return profit
        