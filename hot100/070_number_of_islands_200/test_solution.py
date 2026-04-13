import pytest
from solution import Solution


class TestNumIslands:
    def test_example1(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        assert Solution().numIslands(grid) == 1

    def test_example2(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        assert Solution().numIslands(grid) == 3

    def test_example3_all_water(self):
        grid = [["0", "0"], ["0", "0"]]
        assert Solution().numIslands(grid) == 0

    def test_all_land(self):
        grid = [["1", "1"], ["1", "1"]]
        assert Solution().numIslands(grid) == 1

    def test_single_cell_land(self):
        grid = [["1"]]
        assert Solution().numIslands(grid) == 1

    def test_diagonal_not_connected(self):
        grid = [
            ["1", "0"],
            ["0", "1"],
        ]
        assert Solution().numIslands(grid) == 2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
