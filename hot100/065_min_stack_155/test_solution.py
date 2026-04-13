import pytest
from solution import MinStack


class TestMinStack:
    def test_example1(self):
        stack = MinStack()
        stack.push(-2)
        stack.push(0)
        stack.push(-3)
        assert stack.getMin() == -3
        stack.pop()
        assert stack.top() == 0
        assert stack.getMin() == -2

    def test_example2_push_pop_sequence(self):
        stack = MinStack()
        stack.push(1)
        stack.push(2)
        assert stack.top() == 2
        assert stack.getMin() == 1
        stack.pop()
        assert stack.top() == 1
        assert stack.getMin() == 1

    def test_example3_duplicate_mins(self):
        stack = MinStack()
        stack.push(0)
        stack.push(1)
        stack.push(0)
        assert stack.getMin() == 0
        stack.pop()
        assert stack.getMin() == 0

    def test_single_element(self):
        stack = MinStack()
        stack.push(42)
        assert stack.top() == 42
        assert stack.getMin() == 42

    def test_decreasing_order(self):
        stack = MinStack()
        stack.push(3)
        stack.push(2)
        stack.push(1)
        assert stack.getMin() == 1
        stack.pop()
        assert stack.getMin() == 2
        stack.pop()
        assert stack.getMin() == 3


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
