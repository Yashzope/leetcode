class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        mini = prices[0]
        
        for i in range(1,len(prices)):
            profit = prices[i] - mini
            if profit > max_profit:
                max_profit = profit

            mini = min(prices[i],mini)
        return max_profit
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         if prices[i] - prices[j] > max_profit:
        #             max_profit = prices[i] - prices[j]
        #             return max_profit
        """
        :type prices: List[int]
        :rtype: int
        """
        