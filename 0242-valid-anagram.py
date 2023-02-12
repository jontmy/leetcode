class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(n log n), O(n) possible with collections.Counter
        return len(s) == len(t) and all(a == b for a, b in zip(sorted(s), sorted(t)))
