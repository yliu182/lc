import pytest
from solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestGroupAnagrams:
    def test_example1(self, sol):
        result = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        result_sorted = sorted([sorted(g) for g in result])
        expected_sorted = sorted([sorted(g) for g in [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]])
        assert result_sorted == expected_sorted

    def test_example2(self, sol):
        assert sol.groupAnagrams([""]) == [[""]]

    def test_example3(self, sol):
        assert sol.groupAnagrams(["a"]) == [["a"]]

    def test_no_anagrams(self, sol):
        result = sol.groupAnagrams(["abc", "def", "ghi"])
        result_sorted = sorted([sorted(g) for g in result])
        expected_sorted = sorted([["abc"], ["def"], ["ghi"]])
        assert result_sorted == expected_sorted

    def test_all_anagrams(self, sol):
        result = sol.groupAnagrams(["ab", "ba", "ab"])
        assert len(result) == 1
        assert sorted(result[0]) == ["ab", "ab", "ba"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
