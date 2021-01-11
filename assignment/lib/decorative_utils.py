
"""
Decorative utility module.

Functionality to decorate the output which will be printed on console and file.

@Author: Saurav
"""

import datetime

def printBeginingOfMethod(output_file, message):
    """
    Print the starting pattern of a method.

    Parameters
    ----------
    output_file : `file`
        file where an message will be printed..
    message : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    printEmptyLineOnConsoleAndFile(output_file)
    printOnConsoleAndFile(output_file, "#" * 100)
    printOnConsoleAndFile(output_file, "################## "+message+"  ####################")
    printOnConsoleAndFile(output_file, "#" * 100)
    printEmptyLineOnConsoleAndFile(output_file)


def printEndingOfMethod(output_file):
    """
    Print the ending pattern of a method.

    Parameters
    ----------
    output_file : `file`
        file where an message will be printed.

    Returns
    -------
    None.

    """
    printEmptyLineOnConsoleAndFile(output_file)
    printOnConsoleAndFile(output_file, "#"*100)
    printEmptyLineOnConsoleAndFile(output_file)


def printInteractiveMenu(output_file):
    """
    Print the list of options for interactive menu to the users.

    Parameters
    ----------
    output_file : `File`
        DESCRIPTION.

    Returns
    -------
    None.

    """
    print("-"*100)
    print("Please select one of the below options :")
    print("\t\"General\" or \"G\" to analayse overall Airbnb property")
    print("\t\"Price\" or \"P\" to analayse Airbnb property's prices")
    print("\t\"Rating\" or \"R\" to analyse rating provide to Airbnb property.")
    print("\t\"Bedroom\" or \"B\" to analyse number of bedrooms for Airbnb property.")
    print("\t\"Accomodation\" or \"A\" to analyse number of people can stay in Airbnb property.")
    print("\t\"Correlation\" or \"C\" to find correlation between Airbnb property's price and it's rating.")
    print("\t\"Quit\" or \"Q\" to quit the program")
    print("-"*100)


def printOnConsoleAndFile(output_file, message):
    """
    Print message on the console as well as output file.

    Parameters
    ----------
    output_file : `file`
        file where an message will be printed.
    message : str
        Message of str data type which need to be print on console & file.

    Returns
    -------
    None.

    """
    print(message)
    output_file.write(message + "\n")


def printEmptyLineOnConsoleAndFile(output_file):
    """
    Print an empty line on the console as well as output file.

    Parameters
    ----------
    output_file : `file`
        file where an empty line will be printed.

    Returns
    -------
    None.

    """
    print()
    output_file.write("\n")


def printNewEntryInFile(output_file):
    """
    Print text with timestamp to identify new entry in the file.

    Parameters
    ----------
    output_file : `file`
        file where an empty line will be printed.

    Returns
    -------
    None.

    """
    output_file.write("*****************************************************************************\n")
    output_file.write("****Execution of Program at " + datetime.datetime.now().strftime('%I.%M%p on %A %d %B %Y') + "**************\n")
    output_file.write("*****************************************************************************\n")
    output_file.write("\n")
    printEmptyLineOnConsoleAndFile(output_file)
