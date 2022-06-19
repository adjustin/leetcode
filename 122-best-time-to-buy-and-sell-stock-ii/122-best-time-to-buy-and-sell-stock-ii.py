class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev=prices[0]
        profit=0
        for i in prices[1:]:
            if (prev<i):
                profit+=i-prev
            prev=i
        return profit
            