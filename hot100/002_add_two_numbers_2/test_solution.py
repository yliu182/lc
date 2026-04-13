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
    l1 = list_to_linked_list([2, 4, 3])
    l2 = list_to_linked_list([5, 6, 4])
    result = linked_list_to_list(sol.addTwoNumbers(l1, l2))
    assert result == [7, 0, 8]


def test_example2(sol):
    l1 = list_to_linked_list([0])
    l2 = list_to_linked_list([0])
    result = linked_list_to_list(sol.addTwoNumbers(l1, l2))
    assert result == [0]


def test_example3(sol):
    l1 = list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = list_to_linked_list([9, 9, 9, 9])
    result = linked_list_to_list(sol.addTwoNumbers(l1, l2))
    assert result == [8, 9, 9, 9, 0, 0, 0, 1]


# --- Edge Cases ---

def test_single_digits(sol):
    l1 = list_to_linked_list([5])
    l2 = list_to_linked_list([5])
    result = linked_list_to_list(sol.addTwoNumbers(l1, l2))
    assert result == [0, 1]


def test_different_lengths(sol):
    l1 = list_to_linked_list([1])
    l2 = list_to_linked_list([9, 9, 9])
    result = linked_list_to_list(sol.addTwoNumbers(l1, l2))
    assert result == [0, 0, 0, 1]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
