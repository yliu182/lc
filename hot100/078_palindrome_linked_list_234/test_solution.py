import pytest
from solution import Solution, ListNode


def build_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


class TestPalindromeLinkedList:
    def test_example1_true(self):
        head = build_list([1, 2, 2, 1])
        assert Solution().isPalindrome(head) is True

    def test_example2_false(self):
        head = build_list([1, 2])
        assert Solution().isPalindrome(head) is False

    def test_example3_single(self):
        head = build_list([1])
        assert Solution().isPalindrome(head) is True

    def test_odd_length_palindrome(self):
        head = build_list([1, 2, 1])
        assert Solution().isPalindrome(head) is True

    def test_odd_length_not_palindrome(self):
        head = build_list([1, 2, 3])
        assert Solution().isPalindrome(head) is False

    def test_all_same(self):
        head = build_list([5, 5, 5, 5])
        assert Solution().isPalindrome(head) is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
