from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lo, hi = 10e4 + 1, -1  # constraint: 0 <= prices[i] <= 10^4
        los, his = [], []
        for p in prices:
            lo = min(p, lo)
            los.append(lo)
        for p in reversed(prices):
            hi = max(p, hi)
            his.append(hi)
        his.reverse()
        return max(hi - lo for hi, lo in zip(his, los))

if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
    print(Solution().maxProfit([7, 6, 4, 3, 1]))
    print(Solution().maxProfit([4, 1, 2]))
