from typing import List


class Solution:
    def twoSumHash(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in seen:
                return [i, seen[remainder]]
            seen[num] = i

    def twoSumSort(self, nums: List[int], target: int) -> List[int]:
        s = sorted(nums)
        j = len(nums) - 1
        for i, x in enumerate(s):
            while s[j] + x > target:
                j -= 1
            if s[j] + x == target:
                a = nums.index(x)
                b = nums.index(s[j]) if x != s[j] else nums[a + 1:].index(s[j]) + a + 1
                return [a, b]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.twoSumSort(nums, target)


if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))
    print(Solution().twoSum([3, 2, 4], 6))
    print(Solution().twoSum([3, 3], 6))
    print(Solution().twoSum([-1, -2, -3, -4, -5], -8))
