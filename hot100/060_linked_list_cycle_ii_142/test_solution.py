import pytest
from solution import Solution, ListNode


def build_cycle_list(values, pos):
    """Build a linked list with an optional cycle. pos=-1 means no cycle.
    Returns (head, cycle_node) where cycle_node is the node at pos or None."""
    if not values:
        return None, None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    cycle_node = None
    if pos >= 0:
        nodes[-1].next = nodes[pos]
        cycle_node = nodes[pos]
    return nodes[0], cycle_node


@pytest.fixture
def sol():
    return Solution()


class TestDetectCycle:
    def test_example1(self, sol):
        head, cycle_node = build_cycle_list([3, 2, 0, -4], pos=1)
        assert sol.detectCycle(head) is cycle_node

    def test_example2(self, sol):
        head, cycle_node = build_cycle_list([1, 2], pos=0)
        assert sol.detectCycle(head) is cycle_node

    def test_example3(self, sol):
        head, _ = build_cycle_list([1], pos=-1)
        assert sol.detectCycle(head) is None

    def test_empty_list(self, sol):
        assert sol.detectCycle(None) is None

    def test_no_cycle_multiple_nodes(self, sol):
        head, _ = build_cycle_list([1, 2, 3, 4], pos=-1)
        assert sol.detectCycle(head) is None

    def test_cycle_to_self(self, sol):
        head, cycle_node = build_cycle_list([1], pos=0)
        assert sol.detectCycle(head) is cycle_node

    def test_cycle_at_tail(self, sol):
        head, cycle_node = build_cycle_list([1, 2, 3], pos=2)
        assert sol.detectCycle(head) is cycle_node


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
