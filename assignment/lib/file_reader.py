"""
Module is to read data from a given file.

@Author: Saurav
"""

import sys


def getDataFromFile(filename):
    """
    Read the file and return a dict object containing key value pair.

    Parameters
    ----------
    filename : str
        Name of the file which needs to read.

    Returns
    -------
    data : dict
        Dictionary containing key value objects.

    """
    # Create an empty list for review_scores_rating and price_list
    airbnb_properties_name = []
    review_scores_rating_list = []
    price_list = []
    total_review_list = []
    accomodates_people = []
    bedroom_list = []
    # Variable to store airbnb_properties without price or review_score
    airbnb_properties_without_price = 0
    airbnb_properties_without_review_scores_rating = 0
    data = {}
    county_properties_map = {}
    bedroom_properties_map = {}
    try:
        # Open the file in read mode
        with open(filename) as file_details:
            # Read in each line, one at a time
            count = 0
            for line in file_details:
                try:
                    # Skipping the header
                    if count == 0:
                        count = 1
                        continue
                    # Parse the data in CSV file
                    else:
                        # Amenities column is consists of list  or empty list.
                        # Check if CSV entry contains amenities list
                        if ',"["' in line:
                            start_list = line.index(',"["')
                            end_list = line.index('"]"')
                            amenities = line[start_list:end_list+3]
                        # Check if CSV entry contains empty amenities list
                        else:
                            start_list = line.index('[')
                            end_list = line.index(']')
                            amenities = line[start_list:end_list+1]
                        # Remove aminities from CSV row so that we don't have extra comma(",") when we parse it.
                        line = line.replace(amenities, " ").strip()
                        # Split the row
                        bnb_properties = line.split(",")
                        # This is to cover the scenario where each value of CSV is separted by comma and
                        # none of the data conatins extra comma.
                        # We are using only name, review_scores_rating and price in this program but we are parsing all data.
                        if len(bnb_properties) == 15:
                            listing_id = int(bnb_properties[0])
                            listing_url = bnb_properties[1]
                            name = bnb_properties[2]
                            host_identity_verified = bnb_properties[3]
                            room_type = bnb_properties[4]
                            accommodates = int(bnb_properties[5].strip()) if bnb_properties[5].strip() else 0
                            bedrooms = int(bnb_properties[6].strip()) if bnb_properties[6].strip() else 0
                            # If there is no data in price, we are setting it to zero
                            # If there is data, replace first '$' symbol by empty string and then we will remove any space.
                            price = float(bnb_properties[7].replace('$', '').strip()) if bnb_properties[7].strip() else 0
                            minimum_nights = bnb_properties[8]
                            number_of_reviews = int(bnb_properties[9].strip()) if bnb_properties[9].strip() else 0
                            last_review = bnb_properties[10]
                            # If data is blank set it to 0 otherwise convert value to integer and set it to review_scores_rating
                            review_scores_rating = int(bnb_properties[11].strip()) if bnb_properties[11].strip() else 0
                            instant_bookable = bnb_properties[12]
                            region_name = bnb_properties[13]
                            region_parent_name = bnb_properties[14]
                        # This is to cover the scenario where name contains one ","
                        elif len(bnb_properties) == 16:
                            listing_id = bnb_properties[0]
                            listing_url = bnb_properties[1]
                            name = bnb_properties[2] + ", " + bnb_properties[3]
                            host_identity_verified = bnb_properties[4]
                            room_type = bnb_properties[5]
                            accommodates = int(bnb_properties[6].strip()) if bnb_properties[6].strip() else 0
                            bedrooms = int(bnb_properties[7].strip()) if bnb_properties[7].strip() else 0
                            # If there is no data in price, we are setting it to zero
                            # If there is data, replace first '$' symbol by empty string and then we will remove any space.
                            price = float(bnb_properties[8].replace('$', '').strip()) if bnb_properties[8].strip() else 0
                            minimum_nights = bnb_properties[9]
                            number_of_reviews = int(bnb_properties[10].strip()) if bnb_properties[10].strip() else 0
                            last_review = bnb_properties[11]
                            # If data is blank set it to 0 otherwise convert value to integer and set it to review_scores_rating
                            review_scores_rating = int(bnb_properties[12].strip()) if bnb_properties[12].strip() else 0
                            instant_bookable = bnb_properties[13]
                            region_name = bnb_properties[14]
                            region_parent_name = bnb_properties[15]
                        # This is to cover the scenario where name contains two ","
                        elif len(bnb_properties) == 17:
                            listing_id = int(bnb_properties[0])
                            listing_url = bnb_properties[1]
                            name = bnb_properties[2] + ", " + bnb_properties[3]+", " + bnb_properties[4]
                            host_identity_verified = bnb_properties[5]
                            room_type = bnb_properties[6]
                            accommodates = int(bnb_properties[7].strip()) if bnb_properties[7].strip() else 0
                            bedrooms = int(bnb_properties[8].strip()) if bnb_properties[8].strip() else 0
                            # If there is no data in price, we are setting it to zero
                            # If there is data, replace first '$' symbol by empty string and then we will remove any space.
                            price = float(bnb_properties[9].replace('$', '').strip()) if bnb_properties[9] else 0
                            minimum_nights = bnb_properties[10]
                            number_of_reviews = int(bnb_properties[11].strip()) if bnb_properties[11] else 0
                            last_review = bnb_properties[12]
                            # If data is blank set it to 0 otherwise convert value to integer and set it to review_scores_rating
                            review_scores_rating = int(bnb_properties[13].strip()) if bnb_properties[13].strip() else 0
                            instant_bookable = bnb_properties[14]
                            region_name = bnb_properties[15]
                            region_parent_name = bnb_properties[16]
                        # This is to cover the scenario where name contains three ","
                        elif len(bnb_properties) == 18:
                            listing_id = int(bnb_properties[0])
                            listing_url = bnb_properties[1]
                            name = bnb_properties[2] + ", " + bnb_properties[3]+", " + bnb_properties[4]+", " + bnb_properties[5]
                            host_identity_verified = bnb_properties[6]
                            room_type = bnb_properties[7]
                            accommodates = int(bnb_properties[8].strip()) if bnb_properties[8].strip() else 0
                            bedrooms = int(bnb_properties[9].strip()) if bnb_properties[9].strip() else 0
                            # If there is no data in price, we are setting it to zero
                            # If there is data, replace first '$' symbol by empty string and then we will remove any space.
                            price = float(bnb_properties[10].replace('$', '').strip()) if bnb_properties[10].strip() else 0
                            minimum_nights = bnb_properties[11]
                            number_of_reviews = int(bnb_properties[12].strip()) if bnb_properties[12].strip() else 0
                            last_review = bnb_properties[13]
                            # If data is blank set it to 0 otherwise convert value to integer and set it to review_scores_rating
                            review_scores_rating = int(bnb_properties[14].strip()) if bnb_properties[14].strip() else 0
                            instant_bookable = bnb_properties[15]
                            region_name = bnb_properties[16]
                            region_parent_name = bnb_properties[17]
                        # This is exception/error scenario where we have more than 18 "," in row
                        else:
                            print("ERROR : Number of ',' is more than 18" + " ...." + str(len(bnb_properties)))
                            print(line)
                            price = 0
                            review_scores_rating = 0

                        # Adding name to property name list
                        airbnb_properties_name.append(name)
                        # Add review_scrore in review_scores_rating_list
                        if review_scores_rating:
                            review_scores_rating_list.append(review_scores_rating)
                        else:
                            airbnb_properties_without_review_scores_rating += 1
                            # Adding Default Rating
                            review_scores_rating_list.append(50)
                        # Add price in the price list
                        if price:
                            price_list.append(price)
                        else:
                            airbnb_properties_without_price += 1
                        # Add number of people accomodates in bnb
                        accomodates_people.append(accommodates)
                        # Add number of bedroom in bnb
                        bedroom_list.append(bedrooms)
                        # Add number of reviews in total_review_list
                        total_review_list.append(number_of_reviews)
                        # Create a map to put properties against County
                        county_properties_map[region_parent_name] = county_properties_map.get(region_parent_name, 0) + 1
                        # Create a map to put properties against number of room
                        bedroom_key = str(bedrooms) + " rooms"
                        bedroom_properties_map[bedroom_key] = bedroom_properties_map.get(bedroom_key, 0) + 1
                # Handle exception if there is any value error.
                except ValueError as v_error:
                    print("ERROR: Line in incorrect format:", line)
                    print(v_error)

    except FileNotFoundError:
        print("FileNotFoundError: Unable to open file", filename)
        print(f"Please check the file {filename} exists. This program will terminate gracefully.")
        sys.exit()
    except PermissionError:
        print("PermissionError: Not sufficient permission to open file : ", filename)
        print(f"Please check the you have sufficient permission to read file {filename}. This program will terminate gracefully.")
        sys.exit()
    except IsADirectoryError:
        print("IsADirectoryError: Provided file is a directory and not file : ", filename)
        print(f"Please check the {filename} is a file and not a directory. This program will terminate gracefully.")
        sys.exit()
    except IOError:
        print("IOError: IO exception while reading : ", filename)
        print(f"Please check the file {filename} exists. This program will terminate gracefully.")
        sys.exit()
    finally:
        data["airbnb_properties_name"] = airbnb_properties_name
        data["review_scores_rating_list"] = review_scores_rating_list
        data["price_list"] = price_list
        data["total_review_list"] = total_review_list
        data["bedrooms"] = bedroom_list
        data["accomodates"] = accomodates_people
        data["airbnb_properties_without_price"] = airbnb_properties_without_price
        data["airbnb_properties_without_review_scores_rating"] = airbnb_properties_without_review_scores_rating
        data["county_properties_map"] = county_properties_map
        data["bedroom_properties_map"] = bedroom_properties_map
    return data
