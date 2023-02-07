from collections import deque
from functools import lru_cache


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        # output is in breadth-first order
        queue = deque([self])
        lst = []
        while queue:
            node = queue.popleft()
            if node is None:
                lst.append(None)
                continue
            lst.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        # output removes all trailing `None`s
        for val in reversed(lst):
            if val is None:
                lst.pop()
            else:
                break
        return str(lst)


class Solution:
    @lru_cache
    def allPossibleFBT(self, n):
        if n % 2 == 0:
            return []
        elif n < 1:
            assert False, "no full binary trees for n < 1"
        elif n == 1:
            return [TreeNode()]
        elif n == 3:
            return [TreeNode(left=TreeNode(), right=TreeNode())]
        results = []
        for left_weight in range(1, n, 2):
            right_weight = n - 1 - left_weight
            assert left_weight + right_weight + 1 == n
            left_subtrees = self.allPossibleFBT(left_weight)
            right_subtrees = self.allPossibleFBT(right_weight)
            # cross product to get all possible combinations
            for left_subtree in left_subtrees:
                for right_subtree in right_subtrees:
                    tree = TreeNode(left=left_subtree, right=right_subtree)
                    results.append(tree)
        return results


if __name__ == "__main__":
    for fbt in Solution().allPossibleFBT(7):
        print(fbt)
