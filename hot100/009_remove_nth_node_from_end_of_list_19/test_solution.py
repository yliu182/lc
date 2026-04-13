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
    result = linked_list_to_list(sol.removeNthFromEnd(head, 2))
    assert result == [1, 2, 3, 5]


def test_example2(sol):
    head = list_to_linked_list([1])
    result = linked_list_to_list(sol.removeNthFromEnd(head, 1))
    assert result == []


def test_example3(sol):
    head = list_to_linked_list([1, 2])
    result = linked_list_to_list(sol.removeNthFromEnd(head, 1))
    assert result == [1]


# --- Edge Cases ---

def test_remove_first(sol):
    head = list_to_linked_list([1, 2])
    result = linked_list_to_list(sol.removeNthFromEnd(head, 2))
    assert result == [2]


def test_remove_middle(sol):
    head = list_to_linked_list([1, 2, 3])
    result = linked_list_to_list(sol.removeNthFromEnd(head, 2))
    assert result == [1, 3]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
