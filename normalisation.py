import csv
import sys
import pandas as pd
import difflib
import numpy as np


# ignore Levenshtein distance for now. It doesn't affect the computation in anyway . Although, it can be used to improve the program

def levenshtein_distance(first_string,second_string):

    first_string_char_array = first_string.split()
    first_size  = len(first_string_char_array) + 1
    second_string_char_array  = second_string.split()
    second_size = len(second_string_char_array) + 1

    # initializing the distance_array as 0
    distance_array = np.zeros((first_size, second_size))

    for i in range(1,first_size): # valid because first_size = m+1
        distance_array[i][0] = i

    for j in range(1,second_size): # valid because second_size = n+1
        distance_array[0][j] = j

    # since the subsitution cost is a non zero quantity

    for j in range(1 , second_size):
        for i in range(1 , first_size):
            if first_string_char_array[i-1] == second_string_char_array[j-1] :

                    substitution_cost = 0
            else:
                    substitution_cost = 1
                    distance_array[i][j] = min(distance_array[i-1][j]+1 , distance_array[i][j-1]+1 , distance_array[i-1][j-1]+substitution_cost)

    return distance_array[first_size-1][second_size-1]

# The header that have to be set up if the form change
mapping_headers = {
    "ts": "Timestamp",
    "name": "Full Name",
    "gender": "Gender",
    "is_captain": "Are you Captain of a Sport",
    "representing_sports_ivp": "Are you representing NUS (Competed in IVP/SUNIG A) - indicate yes/no and which sport(s)",
    "sports_currently_in": "Sports you are currently in this season (after the latest cut)",
    "core_sport": "What is your core sport?  (Your jersey orders will be given to this TM)",
    "main_jersey": "Main Jersey- Yellow ($17) (for all sports except Track, Road Relay and Trug)",
    "main_shorts": "Main Shorts (Black) ($15)",
    "road_relay_singlet": "Road Relay/Track Singlet ($16)",
    "touch_rugby_singlet": "Touch Rugby Singlet ($16)",
    "long_socks": "Long Socks (Black) ($12)",
    "is_handball_or_soccer_keeper_or_a_volleyball_libero": "Are you a Handball/Soccer Keeper or a Volleyball Libero?",
    "additional_orders": 'Additional orders (indicate jersey type,size and additional quantity)',
    "first_choice": "First Choice",
    "second_choice": "Second Choice",
    "third_choice": "Third Choice",
    "touch_rugby_number": "Touch Rugby Number",
    "main_jersey_handball_soccer": "Main Jersey- Black ($17) (for Handball/Soccer Keepers and Liberos)"
}


sports = {"soccer", "softball", "rugby", "netball", "dragonboat" , "floorball", "tennis" , "basketball" , "takraw", "swimming", "table tennis" , "track" , "touch rugby" , "road relay"  , "handball", "squash" , "badminton" , "water polo" }
data_frame= pd.read_csv("SMC_test_data.csv" )

def yes_no(string):
    answer = "yes"
    if (difflib.SequenceMatcher(None , answer , string).ratio() >0.7):
        return 1
    else:
        return 0


final_score = []

 # calculates the final points .. takes into consideration .. the possible
 # since a player is a captain of atmost 1 team .. consider yes / no
def calculate_points():
    data_frame= pd.read_csv("SMC_test_data.csv")
    is_captain_column = data_frame[str(mapping_headers["is_captain"])]
    sports_column = data_frame[str(mapping_headers["sports_currently_in"])]
    representing_sports_column = data_frame[str(mapping_headers["representing_sports_ivp"])]


    for i in range(len(is_captain_column)):
        score = 0
        score += yes_no(is_captain_column[i].lower())

        all_sports_currently_involved_in = sports_column[i].split(",")
        # counting points for all the sports currently represented

        for sport in all_sports_currently_involved_in:
            sport = sport.strip().lower()


            for s in sports:
                if difflib.SequenceMatcher(None, s, sport).ratio() >= 0.7:
                    score+= 1

        all_sports_represented = representing_sports_column[i].split(",")

        for sports_represented in all_sports_represented:
            sports_represented = sports_represented.strip().lower()

            for s in sports: # the set
                if difflib.SequenceMatcher(None, s , sports_represented).ratio() >= 0.7 :
                    score+= 1

        final_score.insert(i , score)


calculate_points()
data_frame["total_points"] = final_score

#uncomment the line below to test
#print(data_frame["total_points"])
