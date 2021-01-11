
from pytest import approx
from assignment.lib.stats_utils import getMean, getMedian, getMode, getStandardDeviation, getRange, getCorrelationValue


def test_getMean():
    """
    Test for getMean() method of stats_utils module.

    """
    assert getMean([7, 9, 5, 3]) == 6


def test_getMedian():
    """
    Test for getMedian() method of stats_utils module.

    """
    assert getMedian([1, 9, 3, 7, 6, 8, 3]) == 6
    assert getMedian([6, 8, 9, 1, 4, 2, 5, 3]) == 4.5


def test_getMode():
    """
    Test for getMode() method of stats_utils module.

    """
    assert getMode([6, 3, 9, 6, 6, 5, 9, 3]) == [6]


def test_getRange():
    """
    Test for getRange() method of stats_utils module.

    """
    assert getRange([1, 2, 3, 4, 4, 5]) == 4


def test_getStandardDeviation():
    """
    Test for getStandardDeviation() method of stats_utils module.

    """
    assert getStandardDeviation([1, 2, 3, 4, 4, 5]) == approx(1.47, 0.01)


def test_getCorrelationValue():
    """
    Test for getCorrelationValue() method of stats_utils module.

    """
    assert getCorrelationValue([1, 2, 3, 4], [2, 4, 6, 8]) == approx(1)
    assert getCorrelationValue([1, 2, 3, 4], [8, 6, 4, 2]) == approx(-1)
    assert getCorrelationValue([1, 2, 3, 4], [1, 0, 0, 1]) == 0.0
