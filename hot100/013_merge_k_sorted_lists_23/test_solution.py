import pytest
from solution import Solution, ListNode


def list_to_linked_list(lst):
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


@pytest.fixture
def sol():
    return Solution()


# --- LeetCode Examples ---

def test_example1(sol):
    lists = [
        list_to_linked_list([1, 4, 5]),
        list_to_linked_list([1, 3, 4]),
        list_to_linked_list([2, 6]),
    ]
    result = linked_list_to_list(sol.mergeKLists(lists))
    assert result == [1, 1, 2, 3, 4, 4, 5, 6]


def test_example2(sol):
    result = linked_list_to_list(sol.mergeKLists([]))
    assert result == []


def test_example3(sol):
    result = linked_list_to_list(sol.mergeKLists([None]))
    assert result == []


# --- Edge Cases ---

def test_single_list(sol):
    lists = [list_to_linked_list([1, 2, 3])]
    result = linked_list_to_list(sol.mergeKLists(lists))
    assert result == [1, 2, 3]


def test_all_empty(sol):
    result = linked_list_to_list(sol.mergeKLists([None, None, None]))
    assert result == []


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
