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


class TestReverseLinkedList:
    def test_example1(self):
        head = build_list([1, 2, 3, 4, 5])
        result = Solution().reverseList(head)
        assert list_to_array(result) == [5, 4, 3, 2, 1]

    def test_example2(self):
        head = build_list([1, 2])
        result = Solution().reverseList(head)
        assert list_to_array(result) == [2, 1]

    def test_example3_empty(self):
        result = Solution().reverseList(None)
        assert result is None

    def test_single_node(self):
        head = build_list([1])
        result = Solution().reverseList(head)
        assert list_to_array(result) == [1]

    def test_three_nodes(self):
        head = build_list([1, 2, 3])
        result = Solution().reverseList(head)
        assert list_to_array(result) == [3, 2, 1]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
