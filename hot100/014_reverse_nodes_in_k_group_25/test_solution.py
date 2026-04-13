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
    head = list_to_linked_list([1, 2, 3, 4, 5])
    result = linked_list_to_list(sol.reverseKGroup(head, 2))
    assert result == [2, 1, 4, 3, 5]


def test_example2(sol):
    head = list_to_linked_list([1, 2, 3, 4, 5])
    result = linked_list_to_list(sol.reverseKGroup(head, 3))
    assert result == [3, 2, 1, 4, 5]


# --- Edge Cases ---

def test_k_equals_1(sol):
    head = list_to_linked_list([1, 2, 3])
    result = linked_list_to_list(sol.reverseKGroup(head, 1))
    assert result == [1, 2, 3]


def test_k_equals_length(sol):
    head = list_to_linked_list([1, 2, 3])
    result = linked_list_to_list(sol.reverseKGroup(head, 3))
    assert result == [3, 2, 1]


def test_single_node(sol):
    head = list_to_linked_list([1])
    result = linked_list_to_list(sol.reverseKGroup(head, 1))
    assert result == [1]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
