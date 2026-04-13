import pytest
from solution import Solution


class TestCourseSchedule:
    def test_example1(self):
        assert Solution().canFinish(2, [[1, 0]]) is True

    def test_example2_cycle(self):
        assert Solution().canFinish(2, [[1, 0], [0, 1]]) is False

    def test_example3_no_prerequisites(self):
        assert Solution().canFinish(3, []) is True

    def test_chain(self):
        assert Solution().canFinish(4, [[1, 0], [2, 1], [3, 2]]) is True

    def test_larger_cycle(self):
        assert Solution().canFinish(3, [[0, 1], [1, 2], [2, 0]]) is False

    def test_single_course(self):
        assert Solution().canFinish(1, []) is True

    def test_multiple_prerequisites(self):
        assert Solution().canFinish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
