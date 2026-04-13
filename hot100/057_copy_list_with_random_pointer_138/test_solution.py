import pytest
from solution import Solution, Node


def build_random_list(info):
    """Build a linked list with random pointers from list of [val, random_index]."""
    if not info:
        return None
    nodes = [Node(x[0]) for x in info]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, x in enumerate(info):
        if x[1] is not None:
            nodes[i].random = nodes[x[1]]
    return nodes[0]


def list_to_info(head):
    """Convert linked list with random pointers to list of [val, random_index]."""
    nodes = []
    node = head
    while node:
        nodes.append(node)
        node = node.next
    node_to_idx = {id(n): i for i, n in enumerate(nodes)}
    result = []
    for n in nodes:
        random_idx = node_to_idx[id(n.random)] if n.random else None
        result.append([n.val, random_idx])
    return result


def verify_deep_copy(original_head, copied_head):
    """Verify that copied list is a true deep copy (no shared nodes)."""
    orig_nodes = set()
    node = original_head
    while node:
        orig_nodes.add(id(node))
        node = node.next
    node = copied_head
    while node:
        assert id(node) not in orig_nodes, "Copied list shares nodes with original"
        node = node.next


@pytest.fixture
def sol():
    return Solution()


class TestCopyRandomList:
    def test_example1(self, sol):
        info = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
        head = build_random_list(info)
        copied = sol.copyRandomList(head)
        assert list_to_info(copied) == info
        verify_deep_copy(head, copied)

    def test_example2(self, sol):
        info = [[1, 1], [2, 1]]
        head = build_random_list(info)
        copied = sol.copyRandomList(head)
        assert list_to_info(copied) == info
        verify_deep_copy(head, copied)

    def test_example3(self, sol):
        info = [[3, None], [3, 0], [3, None]]
        head = build_random_list(info)
        copied = sol.copyRandomList(head)
        assert list_to_info(copied) == info
        verify_deep_copy(head, copied)

    def test_empty_list(self, sol):
        assert sol.copyRandomList(None) is None

    def test_single_node_self_random(self, sol):
        info = [[1, 0]]
        head = build_random_list(info)
        copied = sol.copyRandomList(head)
        assert list_to_info(copied) == info
        verify_deep_copy(head, copied)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
