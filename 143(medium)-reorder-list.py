from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # split input list into two halves xs and ys, reverse ys, then zip xs with ys
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None:
            return

        # compute the length of the input list
        cursor = head
        len = 0
        while cursor is not None:
            len += 1
            cursor = cursor.next

        # split the input list into xs and ys, such that len(xs) = len(ys) or len(ys) - 1
        len_xs, len_ys = len // 2 + len % 2, len // 2
        assert len_xs + len_ys == len
        xs, ys, xs_last = head, head, None
        for _ in range(len_xs):
            xs_last = ys
            ys = ys.next
        xs_last.next = None

        # reverse ys
        cursor = ys
        cursor.next, cursor, prev = None, cursor.next, cursor
        for _ in range(len_ys - 1):
            cursor.next, cursor, prev = prev, cursor.next, cursor
        ys = prev

        # zip xs with ys
        for _ in range(len_ys):
            xs.next, xs, ys.next, ys = ys, xs.next, xs.next, ys.next

    def print(self, head):
        ls = []
        cursor = head
        while cursor is not None:
            ls.append(cursor.val)
            cursor = cursor.next
        print(ls)


if __name__ == "__main__":
    ls = [i + 1 for i in range(5)]
    cursor = ListNode(val=ls[0])
    head = cursor
    for x in ls[1:]:
        next = ListNode(val=x)
        cursor.next = next
        cursor = next
    Solution().reorderList(head)
    Solution().print(head)
