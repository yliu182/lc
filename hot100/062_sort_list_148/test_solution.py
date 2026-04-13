import pytest
from solution import Solution, ListNode


def build_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class TestSortList:
    def test_example1(self):
        head = build_list([4, 2, 1, 3])
        result = Solution().sortList(head)
        assert list_to_array(result) == [1, 2, 3, 4]

    def test_example2(self):
        head = build_list([-1, 5, 3, 4, 0])
        result = Solution().sortList(head)
        assert list_to_array(result) == [-1, 0, 3, 4, 5]

    def test_example3_empty(self):
        result = Solution().sortList(None)
        assert result is None

    def test_single_node(self):
        head = build_list([1])
        result = Solution().sortList(head)
        assert list_to_array(result) == [1]

    def test_already_sorted(self):
        head = build_list([1, 2, 3, 4, 5])
        result = Solution().sortList(head)
        assert list_to_array(result) == [1, 2, 3, 4, 5]

    def test_duplicates(self):
        head = build_list([3, 1, 2, 3, 1])
        result = Solution().sortList(head)
        assert list_to_array(result) == [1, 1, 2, 3, 3]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
