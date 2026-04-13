import pytest
from solution import Solution, ListNode


def build_cycle_list(values, pos):
    """Build a linked list with an optional cycle. pos=-1 means no cycle."""
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0]


@pytest.fixture
def sol():
    return Solution()


class TestLinkedListCycle:
    def test_example1(self, sol):
        head = build_cycle_list([3, 2, 0, -4], pos=1)
        assert sol.hasCycle(head) is True

    def test_example2(self, sol):
        head = build_cycle_list([1, 2], pos=0)
        assert sol.hasCycle(head) is True

    def test_example3(self, sol):
        head = build_cycle_list([1], pos=-1)
        assert sol.hasCycle(head) is False

    def test_empty_list(self, sol):
        assert sol.hasCycle(None) is False

    def test_no_cycle_multiple_nodes(self, sol):
        head = build_cycle_list([1, 2, 3, 4], pos=-1)
        assert sol.hasCycle(head) is False

    def test_cycle_to_self(self, sol):
        head = build_cycle_list([1], pos=0)
        assert sol.hasCycle(head) is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
