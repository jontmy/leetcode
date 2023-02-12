class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = [c for c in s.lower() if c.isalnum()]
        a, b = t[:len(t) // 2], t[len(t) // 2 + len(t) % 2:]  # split the string into 2 equal halves
        return all(x == y for x, y in zip(a, reversed(b)))  # flip b around and compare against a


if __name__ == "__main__":
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
