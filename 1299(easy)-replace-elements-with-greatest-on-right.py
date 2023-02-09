from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = -1
        for i in reversed(range(len(arr))):
            arr[i], m = m, max(m, arr[i])
        return arr


if __name__ == "__main__":
    print(Solution().replaceElements([17, 18, 5, 4, 6, 1]))
    print(Solution().replaceElements([400]))
