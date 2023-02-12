from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def new(cls, ls):
        if not ls:
            return None
        cursor = ListNode(val=ls[0])
        start = cursor
        for x in ls[1:]:
            cursor.next = ListNode(val=x)
            cursor = cursor.next
        return start

    def print(self):
        cursor = self
        xs = []
        while cursor is not None:
            xs.append(cursor.val)
            cursor = cursor.next
        print(xs)


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        cursor = list2 if list2.val <= list1.val else list1  # start from the smallest of the two lists
        start = cursor
        x = list1 if list2.val <= list1.val else list1.next  # advance x if head of x is smaller
        y = list2.next if list2.val <= list1.val else list2  # advance y if head of y is smaller
        while True:
            if x is None:
                cursor.next = y
                return start
            if y is None:
                cursor.next = x
                return start
            if x.val <= y.val:
                x, cursor.next, cursor = x.next, x, x
            else:
                y, cursor.next, cursor = y.next, y, y


if __name__ == "__main__":
    Solution().mergeTwoLists(
        ListNode.new([1, 2, 4]),
        ListNode.new([1, 3, 4])
    ).print()
