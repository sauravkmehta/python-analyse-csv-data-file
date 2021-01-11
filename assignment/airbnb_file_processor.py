"""
An interactive program to parse the Airbnb listing by A00288443.

We can chose one property from Review or Price.
Program will show the MAX, MIN, MEAN, MEDIAN, MODE, RANGE and STANDARD DEVIATION etc.
It will also calculate correlation between few key properties of Airbnb.
It will also print the scatter graph for correlation.
It will also print the pie Chart, box plot,horizontal bar and boxplot for airbnb properties.
"""

from assignment.lib.common_utils import getRelationshipTypeFromCorrelationValue

from assignment.lib.decorative_utils import printInteractiveMenu
from assignment.lib.decorative_utils import printEndingOfMethod
from assignment.lib.decorative_utils import printOnConsoleAndFile
from assignment.lib.decorative_utils import printEmptyLineOnConsoleAndFile
from assignment.lib.decorative_utils import printBeginingOfMethod
from assignment.lib.decorative_utils import printNewEntryInFile

from assignment.lib.file_reader import getDataFromFile

from assignment.lib.plot_utils import getFigureAndAxes
from assignment.lib.plot_utils import drawPieChart
from assignment.lib.plot_utils import drawScatterGraph
from assignment.lib.plot_utils import drawHorizontalBar
from assignment.lib.plot_utils import drawBoxplot


from assignment.lib.stats_utils import getCorrelationValue
from assignment.lib.stats_utils import getMean
from assignment.lib.stats_utils import getMedian
from assignment.lib.stats_utils import getMode
from assignment.lib.stats_utils import getRange
from assignment.lib.stats_utils import getStandardDeviation

filename = input("Enter the name of the file containing the details: ")
#filename = "airbnb_updated_data.csv"
data_in_map_form = getDataFromFile(filename)
airbnb_properties_name = data_in_map_form["airbnb_properties_name"]
review_scores_rating_list = data_in_map_form["review_scores_rating_list"]
total_number_of_review_list = data_in_map_form["total_review_list"]
price_list = data_in_map_form["price_list"]
bedroom_list = data_in_map_form["bedrooms"]
accomodation_list = data_in_map_form["accomodates"]
airbnb_properties_without_price = data_in_map_form["airbnb_properties_without_price"]
airbnb_properties_without_review_scores_rating = data_in_map_form["airbnb_properties_without_review_scores_rating"]
county_properties_map = data_in_map_form["county_properties_map"]
bedroom_properties_map = data_in_map_form["bedroom_properties_map"]
# Create a file "Result.txt" or append the existing "Result.txt"
output_file = open('Result.txt', 'a')
printNewEntryInFile(output_file)
while True:
    printInteractiveMenu(output_file)
    user_selection = input("Plese enter you selection : ")
    printOnConsoleAndFile(output_file, f"You have selected : {user_selection}")
    printEmptyLineOnConsoleAndFile(output_file)
    # If user select the price option, all details of price will be shown.
    if user_selection.lower() == "general" or user_selection.lower() == "g":
        # Title of the analysis. Decorative string.
        printBeginingOfMethod(output_file, "          General analysis for Airbnb Properties           ")
        # Informative information about the data e.g. total number of entry, number of entries which does not have price etc
        printOnConsoleAndFile(output_file,
                              f"Number of Airbnb property in the provided file : {len(airbnb_properties_name)}")
        printOnConsoleAndFile(output_file,
                              f"Number of Airbnb property which is missing price : {airbnb_properties_without_price}")
        printOnConsoleAndFile(output_file,
                              f"Number of Airbnb property which is missing rating : {airbnb_properties_without_review_scores_rating}")
        printOnConsoleAndFile(output_file,
                              f"Most expensive Airbnb property : ${max(price_list): .2f}")
        printOnConsoleAndFile(output_file,
                              f"Least expensive Airbnb property : ${min(price_list): .2f}")
        printOnConsoleAndFile(output_file,
                              f"Highest Rated of Airbnb property : {max(review_scores_rating_list)}")
        printOnConsoleAndFile(output_file,
                              f"Lowest Rated of Airbnb property : {min(review_scores_rating_list)}")
        printOnConsoleAndFile(output_file, f"Maximum people can stay in Airbnb property : {max(accomodation_list)}")
        printOnConsoleAndFile(output_file, f"Minimum people can stay in Airbnb property  : {min(accomodation_list)}")
        printOnConsoleAndFile(output_file, f"Maximum bedrooms in Airbnb property : {max(bedroom_list)}")
        printOnConsoleAndFile(output_file, f"Minimum bedrooms in Airbnb property  : {min(bedroom_list)}")
        need_graphical_data = input("Do you want the graphical data for visual representation of Airbnb properties? [y/n] :")
        if need_graphical_data.lower() == 'y':
            fig, ax = getFigureAndAxes(3, 2)
            drawPieChart(ax[0, 0], "Airbnb properties in Different County", county_properties_map)
            drawHorizontalBar(ax[1, 0], "Airbnb properties in Different County", "County",
                              "Properties", county_properties_map)
            drawPieChart(ax[0, 1], "Airbnb properties with number of rooms", bedroom_properties_map)
            drawHorizontalBar(ax[1, 1], "Airbnb properties with number of rooms", "Bedrooms",
                              "Properties", bedroom_properties_map)
            drawBoxplot(ax[2, 0], "Airbnb Properties Prices", "Price per day", price_list)
            drawBoxplot(ax[2, 1], "Airbnb Properties Review", "Average review score", review_scores_rating_list)
            # Saving figure
            fig.savefig("General analysis for Airbnb Properties.png", bbox_inches="tight")
            printOnConsoleAndFile(output_file,
                                  "General analysis for Airbnb Properties.png is saved in working directory.")
        # Decorative string
        printEndingOfMethod(output_file)
        output_file.flush()

    # If user selects price, all analysis of price will be shown to user.
    elif user_selection.lower() == "price" or user_selection.lower() == "p":
        # Title of the analysis. Decorative string.
        printBeginingOfMethod(output_file, "       Analysis of the prices for Airbnb Properties        ")
        # Number of values (records), maximum, minimum value of price
        printOnConsoleAndFile(output_file, f"Number of price entry : {len(price_list)}")
        printOnConsoleAndFile(output_file, f"Highest price of Airbnb property : ${max(price_list): .2f}")
        printOnConsoleAndFile(output_file, f"Lower price of Airbnb property : ${min(price_list): .2f}")
        # Calculate the Mean of the prices
        mean_price = getMean(price_list)
        printOnConsoleAndFile(output_file, f"Mean/Average price of Airbnb property : ${mean_price:.2f}")
        # Calculate the Median of the prices
        median_of_price = getMedian(price_list)
        printOnConsoleAndFile(output_file, f"Median of the prices of Airbnb property is: ${median_of_price:.2f}")
        # Calculate the Mode of the prices
        mode_price = getMode(price_list)
        printOnConsoleAndFile(output_file, f"Mode of the prices of Airbnb property is : {str(mode_price)}")
        # Calculate the Range of the prices
        range_price = getRange(price_list)
        printOnConsoleAndFile(output_file, f"Range of the prices of Airbnb property is : {str(range_price)}")
        # Standard Deviation of prices
        std_deviation_for_price = getStandardDeviation(price_list)
        printOnConsoleAndFile(output_file,
                              f"Standard Deviation for prices of Airbnb property is: {std_deviation_for_price:.2f} ")
        # Decorative string
        printEndingOfMethod(output_file)
        output_file.flush()
    # If user selects rating, all analysis of rating will be shown to user.
    elif user_selection.lower() == "rating" or user_selection.lower() == "r":
        # Title of the analysis. Decorative string.
        printBeginingOfMethod(output_file, "       Analysis of the Ratings for Airbnb Properties       ")
        # Number of values (records), maximum, minimum value of rating
        printOnConsoleAndFile(output_file, f"Number of review entry : {len(review_scores_rating_list)}")
        printOnConsoleAndFile(output_file, f"Highest Rated of Airbnb property : {max(review_scores_rating_list)}")
        printOnConsoleAndFile(output_file, f"Lowest Rated of Airbnb property : {min(review_scores_rating_list)}")
        # Calculate the Mean of the review_score_rating
        mean_review_scrore_rating = getMean(review_scores_rating_list)
        printOnConsoleAndFile(output_file,
                              f"Mean/Average Rating for Airbnb property : {mean_review_scrore_rating:.2f}")
        # Calculate the Median of the review_score_rating
        median_of_review_scrore_rating = getMedian(review_scores_rating_list)
        printOnConsoleAndFile(output_file,
                              f"Median of the rating for Airbnb property : {median_of_review_scrore_rating:.2f}")
        # Calculate the Mode of the rating
        mode_review_scores_rating = getMode(review_scores_rating_list)
        printOnConsoleAndFile(output_file,
                              f"Mode of the rating for Airbnb property : {mode_review_scores_rating}")
        # Calculate the Range of the prices
        range_ratings = getRange(review_scores_rating_list)
        printOnConsoleAndFile(output_file, f"Range of the rating of Airbnb property is : {str(range_ratings)}")
        # Standard Deviation in rating
        std_dev_for_review_rating = getStandardDeviation(review_scores_rating_list)
        printOnConsoleAndFile(output_file,
                              f"Standard Deviation for rating for Airbnb property : {std_dev_for_review_rating:.2f}")
        printEndingOfMethod(output_file)
        output_file.flush()

    elif user_selection.lower() == "bedroom" or user_selection.lower() == "b":
        # Title of the analysis. Decorative string.
        printBeginingOfMethod(output_file, "     Analysis of number of bedrooms in Airbnb Properties   ")
        # Number of values (records), maximum, minimum value of price
        printOnConsoleAndFile(output_file, f"Number of bedroom entry in Airbnb Properties : {len(bedroom_list)}")
        printOnConsoleAndFile(output_file, f"Maximum bedrooms in Airbnb property : {max(bedroom_list)}")
        printOnConsoleAndFile(output_file, f"Minimum bedrooms in Airbnb property  : {min(bedroom_list)}")
        # Calculate the Mean of the prices
        mean_bedroom_number = getMean(bedroom_list)
        printOnConsoleAndFile(output_file, f"Mean/Average number of bedroom in Airbnb property : {mean_bedroom_number:.2f}")
        # Calculate the Median of the prices
        median_bedroom_number = getMedian(bedroom_list)
        printOnConsoleAndFile(output_file, f"Median number of bedroom in Airbnb property is: {median_bedroom_number:.2f}")
        # Calculate the Mode of the prices
        mode_bedroom_number = getMode(bedroom_list)
        printOnConsoleAndFile(output_file, f"Mode number of bedroom in Airbnb property is : {str(mode_bedroom_number)}")
        # Calculate the Range of the prices
        range_bedroom_number = getRange(bedroom_list)
        printOnConsoleAndFile(output_file, f"Range of number of bedroom in Airbnb property is : {str(range_bedroom_number)}")
        # Standard Deviation of prices
        std_deviation_for_bedroom_number = getStandardDeviation(bedroom_list)
        printOnConsoleAndFile(output_file,
                              f"Standard Deviation for prices of Airbnb property is: {std_deviation_for_bedroom_number:.2f} ")
        # Decorative string
        printEndingOfMethod(output_file)
        output_file.flush()

    # If user selects price, all analysis of price will be shown to user.
    elif user_selection.lower() == "accomodation" or user_selection.lower() == "a":
        # Title of the analysis. Decorative string.
        printBeginingOfMethod(output_file, " Analysis of num of people accomodate in Airbnb Properties ")
        # Number of values (records), maximum, minimum value of price
        printOnConsoleAndFile(output_file, f"Number of people accomodate entry in Airbnb Properties : {len(accomodation_list)}")
        printOnConsoleAndFile(output_file, f"Maximum people can stay in Airbnb property : {max(accomodation_list)}")
        printOnConsoleAndFile(output_file, f"Minimum people can stay in Airbnb property  : {min(accomodation_list)}")
        # Calculate the Mean of the prices
        mean_accomodates = getMean(accomodation_list)
        printOnConsoleAndFile(output_file, f"Mean/Average number of people in Airbnb property : {mean_accomodates:.2f}")
        # Calculate the Median of the prices
        median_accomodates = getMedian(accomodation_list)
        printOnConsoleAndFile(output_file, f"Median number of people in Airbnb property is: {median_accomodates:.2f}")
        # Calculate the Mode of the prices
        mode_accomodates = getMode(accomodation_list)
        printOnConsoleAndFile(output_file, f"Mode number of people in Airbnb property is : {str(mode_accomodates)}")
        # Calculate the Range of the prices
        range_accomodates = getRange(accomodation_list)
        printOnConsoleAndFile(output_file, f"Range of number of people in Airbnb property is : {str(range_accomodates)}")
        # Standard Deviation of prices
        std_deviation_for_accomodates = getStandardDeviation(accomodation_list)
        printOnConsoleAndFile(output_file,
                              f"Standard Deviation for number of people of Airbnb property is: {std_deviation_for_accomodates:.2f} ")
        # Decorative string
        printEndingOfMethod(output_file)
        output_file.flush()

    # If user selects correlation, correlation between Price, Ratings and Total Number Of Review will be calculated
    elif user_selection.lower() == "Correlation" or user_selection.lower() == "c":
        # Title of the analysis. Decorative string.
        printBeginingOfMethod(output_file, "      Correlation between Price and Rating for Airbnb      ")
        correlation = getCorrelationValue(price_list, review_scores_rating_list)
        relationship = getRelationshipTypeFromCorrelationValue(correlation)
        printOnConsoleAndFile(output_file, f"The relationship between price and rating is {relationship}.")
        printOnConsoleAndFile(output_file, f"Number of price entry: {len(price_list)}")
        printOnConsoleAndFile(output_file, f"Number of review_score entry: {len(review_scores_rating_list)}")
        printOnConsoleAndFile(output_file, f"Correlation between price and rating: {correlation:.2f}")
        printBeginingOfMethod(output_file, "  Correlation between Rating and Total Rating for Airbnb   ")
        correlation_1 = getCorrelationValue(review_scores_rating_list, total_number_of_review_list)
        relationship_1 = getRelationshipTypeFromCorrelationValue(correlation_1)
        printOnConsoleAndFile(output_file, f"The relationship between rating and total number of rating is {relationship_1}.")
        printOnConsoleAndFile(output_file, f"Correlation between price and rating: {correlation_1:.2f}")
        printBeginingOfMethod(output_file, " Correlation between Bedroom and Accomodation for Airbnb   ")
        correlation_2 = getCorrelationValue(bedroom_list, accomodation_list)
        relationship_2 = getRelationshipTypeFromCorrelationValue(correlation_2)
        printOnConsoleAndFile(output_file, f"The relationship between bedroom and accomodation is {relationship_2}.")
        printOnConsoleAndFile(output_file, f"Correlation between bedroom and accomodation: {correlation_2:.2f}")
        printBeginingOfMethod(output_file, "     Correlation between Price and Bedrooms for Airbnb     ")
        correlation_3 = getCorrelationValue(price_list, bedroom_list)
        relationship_3 = getRelationshipTypeFromCorrelationValue(correlation_3)
        printOnConsoleAndFile(output_file, f"The relationship between price and bedroom is {relationship_3}.")
        printOnConsoleAndFile(output_file, f"Correlation between price and bedroom: {correlation_3:.2f}")
        need_graphical_data = input("Do you want the scatter graph for these correlations? [y/n] ")
        if need_graphical_data.lower() == 'y':
            fig, ax = getFigureAndAxes(2, 2)
            drawScatterGraph(ax[0][0], "Correlation between Price and Ratings for Airbnb Properties",
                             "Price", "Rating", price_list, review_scores_rating_list)
            drawScatterGraph(ax[0][1], "Correlation between Rating and  Number Of Ratings for Airbnb Properties",
                             "Rating", "Total Number Of Review", review_scores_rating_list, total_number_of_review_list)
            drawScatterGraph(ax[1][0], "Correlation between Bedroom and Accomodation for Airbnb Properties",
                             "Bedroom", "Accomodation", bedroom_list, accomodation_list)
            drawScatterGraph(ax[1][1], "Correlation between Price and  Bedroom for Airbnb Properties",
                             "Price", "Bedroom", price_list, bedroom_list)
            fig.savefig("Correlation between Price, Ratings and Total Number Of Review for Airbnb Properties.png",
                        bbox_inches="tight")
            printOnConsoleAndFile(output_file,
                                  "Correlation between Price, Ratings and Total Number Of Review for Airbnb Properties.png is saved in working directory.")
        # Decorative string
        printEndingOfMethod(output_file)
        output_file.flush()
        # If user selects price, all analysis of price will be shown to user.
    # If user select 'Q' or 'Quit' we need teh break the file loop
    elif user_selection.lower() == "quit" or user_selection.lower() == "q":
        break
    # To handle invalid selection
    else:
        printOnConsoleAndFile(output_file, "Invalid Input. Please enter the a valid input or Q/q to quit.")
        continue
printOnConsoleAndFile(output_file, "Thanks for using this application. \nAll output, which are dispalyed in console, are saved in Result.txt file.")
output_file.close()
