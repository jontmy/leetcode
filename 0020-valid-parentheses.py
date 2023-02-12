class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '[': ']', '{': '}'}
        for c in s:
            stack.append(c)
            while len(stack) > 0 and stack[-1] not in pairs.keys():
                if len(stack) < 2:
                    return False
                if pairs[stack[-2]] == stack[-1]:
                    stack.pop()
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    print(Solution().isValid("()"))
    print(Solution().isValid("()[]{}"))
    print(Solution().isValid("(]"))
    print(Solution().isValid("(([]))"))
    print(Solution().isValid("(([{]}))"))
