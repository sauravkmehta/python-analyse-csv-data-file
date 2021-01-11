"""
Utitlity module for Statistics.

This has functionality to calculate mean, median, mode.
This also have functionality to get standard deviation for a list and  to get
correlation between values of two list.

@Author: Saurav
"""

from math import sqrt

from collections import Counter


def getMean(inputList):
    """
    Calculate and return the Mean of the entries in given list.

    Parameters
    ----------
    inputList : list
        List containing int type values.

    Returns
    -------
    mean : float
        Mean or average value for the list.

    """
    number_of_entry_in_list = len(inputList)
    sum_of_all_elements_in_list = sum(inputList)
    mean = sum_of_all_elements_in_list / number_of_entry_in_list
    return mean


def getMedian(inputList):
    """
    Calculate and return the Median of the entries in given list.

    Parameters
    ----------
    inputList : list
        List containing int type values.

    Returns
    -------
    median : int
        Middle element of the list.

    """
    inputList.sort()
    number_of_entry_in_list = len(inputList)
    if number_of_entry_in_list % 2 == 0:
        median = (inputList[number_of_entry_in_list//2] +
                  inputList[number_of_entry_in_list//2 - 1])/2
    else:
        median = inputList[number_of_entry_in_list//2]
    return median


def getMode(inputList):
    """
    Calculate and return the Mode of the entries in given list.

    Parameters
    ----------
    inputList : list
        List containing int type values.

    Returns
    -------
    mode : TYPE
        the mode of the numbers.

    """
    list_counter = Counter(inputList)
    mode = [k for k, v in list_counter.items() if
            v == list_counter.most_common(1)[0][1]]
    return mode


def getRange(inputList):
    """
    Calculate and return the range for a given list.

    Parameters
    ----------
    inputList : list
         List containing int type values.

    Returns
    -------
    int
        the difference between the largest and smallest number in a list.

    """
    return max(inputList) - min(inputList)


def getStandardDeviation(inputList):
    """
    Calculate and return the standard deviation for a given list.

    Parameters
    ----------
    inputList : list
        List containing int type values.

    Returns
    -------
    std_deviation : float

    """
    mean = getMean(inputList)
    # Create a list of the deviations squared
    deviations_for_entries_in_list = [(value - mean) **
                                      2 for value in inputList]
    # Calculate the standard deviation
    std_deviation = sqrt(sum(deviations_for_entries_in_list) /
                         (len(inputList)-1))
    return std_deviation


def getCorrelationValue(first_list, second_list):
    """
    Calculate and return the correlation value between two list.

    Parameters
    ----------
    first_list : list
        List containing int type values.
    second_list : list
        List containing int type values.

    Returns
    -------
    correlation : float

    """
    # Calculate the means
    first_list_mean = sum(first_list)/len(first_list)
    second_list_mean = sum(second_list)/len(second_list)

    # Create a list of the deviations
    first_list_deviations = [list_item - first_list_mean for
                             list_item in first_list]
    second_list_deviations = [list_item - second_list_mean for
                              list_item in second_list]

    # Create a list of the deviations multipled
    first_list_second_list_deviations = [first_list_mean*second_list_mean for
                                         (first_list_mean, second_list_mean) in
                                         zip(first_list_deviations,
                                             second_list_deviations)]

    # Create a list of the deviations squared
    first_list_square_deviations = [(list_item - first_list_mean) ** 2 for
                                    list_item in first_list]
    second_list_rating_deviations = [(list_item - second_list_mean) ** 2 for
                                     list_item in second_list]

    # Calculate the correlation
    correlation = sum(first_list_second_list_deviations) / (sqrt(sum(first_list_square_deviations)) * sqrt(sum(second_list_rating_deviations)))
    return correlation


if __name__ == '__main__':
    inputList = [1, 1, 2, 3, 4, 5, 6, 7, 8, 8, 8]
    print(getStandardDeviation(inputList))
    print(getMedian(inputList))
    print(getMode(inputList))
    print(getMean(inputList))
