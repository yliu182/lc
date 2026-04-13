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
    l1 = list_to_linked_list([1, 2, 4])
    l2 = list_to_linked_list([1, 3, 4])
    result = linked_list_to_list(sol.mergeTwoLists(l1, l2))
    assert result == [1, 1, 2, 3, 4, 4]


def test_example2(sol):
    result = linked_list_to_list(sol.mergeTwoLists(None, None))
    assert result == []


def test_example3(sol):
    l2 = list_to_linked_list([0])
    result = linked_list_to_list(sol.mergeTwoLists(None, l2))
    assert result == [0]


# --- Edge Cases ---

def test_one_empty(sol):
    l1 = list_to_linked_list([1, 2, 3])
    result = linked_list_to_list(sol.mergeTwoLists(l1, None))
    assert result == [1, 2, 3]


def test_single_elements(sol):
    l1 = list_to_linked_list([5])
    l2 = list_to_linked_list([1])
    result = linked_list_to_list(sol.mergeTwoLists(l1, l2))
    assert result == [1, 5]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
