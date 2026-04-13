import pytest
from solution import MedianFinder


def test_example1():
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(3)
    assert mf.findMedian() == 2.0


def test_example2():
    mf = MedianFinder()
    mf.addNum(6)
    assert mf.findMedian() == 6.0
    mf.addNum(10)
    assert mf.findMedian() == 8.0
    mf.addNum(2)
    assert mf.findMedian() == 6.0


def test_example3():
    mf = MedianFinder()
    mf.addNum(-1)
    assert mf.findMedian() == -1.0
    mf.addNum(-2)
    assert mf.findMedian() == -1.5


def test_single_element():
    mf = MedianFinder()
    mf.addNum(5)
    assert mf.findMedian() == 5.0


def test_duplicates():
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(1)
    mf.addNum(1)
    assert mf.findMedian() == 1.0


def test_increasing_sequence():
    mf = MedianFinder()
    for i in range(1, 6):
        mf.addNum(i)
    assert mf.findMedian() == 3.0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
