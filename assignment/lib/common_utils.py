
"""
Module contains some basic functionality.

@Author: Saurav
"""


def getRelationshipTypeFromCorrelationValue(correlation_value: float) -> str:
    """
    To get relationship type based on the correlation value.

    Parameters
    ----------
    correlation_value : float
        Value of correlation.

    Returns
    -------
    relationship : str
        Type of realtionship in string format.

    """
    if correlation_value < 0.3:
        relationship = "Very Weak"
    elif 0.3 <= correlation_value < 0.5:
        relationship = "Weak"
    elif 0.5 <= correlation_value < 0.7:
        relationship = "Moderate"
    else:
        relationship = "Strong"
    return relationship
