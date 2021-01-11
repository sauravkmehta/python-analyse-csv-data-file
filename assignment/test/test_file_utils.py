import os
from pytest import raises
from assignment.lib.file_reader import getDataFromFile


def test_getDataFromFile_FileNotFound():
    with raises(SystemExit):
        TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), "FileNotFound.csv")
        getDataFromFile(TESTDATA_FILENAME)



def test_getDataFromFile_IsADirectoryError():
    with raises(SystemExit):
        TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), "test_directory")
        getDataFromFile(TESTDATA_FILENAME)


def test_getDataFromFile_PermissionError():
    with raises(SystemExit):
        TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), "NoPermission.csv")
        getDataFromFile(TESTDATA_FILENAME)


def test_getDataFromFile_SingleData():
    TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), "test_airbnb_updated_data.csv")
    dict_result = getDataFromFile(TESTDATA_FILENAME)
    assert len(dict_result["price_list"]) == 2
    assert len(dict_result["total_review_list"]) == 2
    assert len(dict_result["airbnb_properties_name"]) == 2
    assert len(dict_result["review_scores_rating_list"]) == 2
    assert dict_result["airbnb_properties_without_price"] == 0
    assert dict_result["county_properties_map"].keys() == {"Meath County Council", "Mayo County Council"}
    assert dict_result["airbnb_properties_without_review_scores_rating"] == 0
    assert verifyEqualList(dict_result["review_scores_rating_list"], {99, 97})
    assert verifyEqualList(dict_result["bedroom_properties_map"].keys(), {"7 rooms", "6 rooms"})


def verifyEqualList(list1, list2):
    return len(list1) == len(list2) and sorted(list1) == sorted(list2)
