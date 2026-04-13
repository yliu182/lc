import pytest
from solution import Solution, ListNode


def build_lists_with_intersection(valsA, valsB, shared_vals):
    """Build two linked lists that share a common tail."""
    # Build shared tail
    shared_head = None
    shared_tail = None
    for v in shared_vals:
        node = ListNode(v)
        if shared_head is None:
            shared_head = node
            shared_tail = node
        else:
            shared_tail.next = node
            shared_tail = node

    # Build list A
    dummyA = ListNode(0)
    curr = dummyA
    for v in valsA:
        curr.next = ListNode(v)
        curr = curr.next
    curr.next = shared_head
    headA = dummyA.next

    # Build list B
    dummyB = ListNode(0)
    curr = dummyB
    for v in valsB:
        curr.next = ListNode(v)
        curr = curr.next
    curr.next = shared_head
    headB = dummyB.next

    return headA, headB, shared_head


class TestIntersection:
    def test_example1(self):
        headA, headB, shared = build_lists_with_intersection(
            [4, 1], [5, 6, 1], [8, 4, 5]
        )
        result = Solution().getIntersectionNode(headA, headB)
        assert result is shared

    def test_example2(self):
        headA, headB, shared = build_lists_with_intersection(
            [1, 9, 1], [3], [2, 4]
        )
        result = Solution().getIntersectionNode(headA, headB)
        assert result is shared

    def test_example3_no_intersection(self):
        headA, _, _ = build_lists_with_intersection([2, 6, 4], [], [])
        headB, _, _ = build_lists_with_intersection([1, 5], [], [])
        result = Solution().getIntersectionNode(headA, headB)
        assert result is None

    def test_single_shared_node(self):
        headA, headB, shared = build_lists_with_intersection(
            [1], [2], [3]
        )
        result = Solution().getIntersectionNode(headA, headB)
        assert result is shared

    def test_entire_list_shared(self):
        headA, headB, shared = build_lists_with_intersection(
            [], [], [1, 2, 3]
        )
        result = Solution().getIntersectionNode(headA, headB)
        assert result is shared

    def test_both_single_no_intersection(self):
        a = ListNode(1)
        b = ListNode(2)
        result = Solution().getIntersectionNode(a, b)
        assert result is None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
