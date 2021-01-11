
from assignment.lib.common_utils import getRelationshipTypeFromCorrelationValue


def test_getRelationshipTypeFromCorrelationValue_for_Veryweak():
    """
    Validate and Verify the Correlation type of Very Weak.

    """
    assert getRelationshipTypeFromCorrelationValue(-2.0) == "Very Weak"
    assert getRelationshipTypeFromCorrelationValue(0.0) == "Very Weak"
    assert getRelationshipTypeFromCorrelationValue(0.29) == "Very Weak"


def test_getRelationshipTypeFromCorrelationValue_for_Weak():
    """
    Validate and Verify the Correlation type of Weak.

    """
    assert getRelationshipTypeFromCorrelationValue(0.3) == "Weak"
    assert getRelationshipTypeFromCorrelationValue(0.49) == "Weak"


def test_getRelationshipTypeFromCorrelationValue_for_Moderate():
    """
    Validate and Verify the Correlation type of Moderate.

    """
    assert getRelationshipTypeFromCorrelationValue(0.5) == "Moderate"
    assert getRelationshipTypeFromCorrelationValue(0.69) == "Moderate"


def test_getRelationshipTypeFromCorrelationValue_for_Strong():
    """
    Validate and Verify the Correlation type of Strong.

    """
    assert getRelationshipTypeFromCorrelationValue(0.7) == "Strong"
    assert getRelationshipTypeFromCorrelationValue(1.0) == "Strong"
    assert getRelationshipTypeFromCorrelationValue(100) == "Strong"
