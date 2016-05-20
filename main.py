import pandas as pd
import random
import constants
import scipy.stats as ss
import numpy as np

def random_gen(trip_list):
    rand_ord = []

    # Create all the items that need to be randomized.
    for x in range(constants.NUM_RAND_ORD):
        rand_ord += trip_list

    index = random.randint(0, len(rand_ord) - 1)
    dot_ordering = [rand_ord.pop(index)]

    # Pick a random item and try to add it to the random ordering list
    # The item randomly generated cannot be the same as the last one added to the list
    while rand_ord:
        index = random.randint(0, len(rand_ord) - 1)

        # Only add the randomly generated number
        if dot_ordering[-1] != rand_ord[index]:
            dot_ordering.append(rand_ord.pop(index))
        else:

            # Exit if it is not possible to pick an item from the list that does not violate the constraint.
            temp = rand_ord[:]
            temp = [x for x in temp if x != dot_ordering[-1]]
            if not temp:
                return None

    return dot_ordering


for i in range(1, constants.NUM_OF_PARTICIPANTS + 1):
    dot_trip_ord = random_gen(constants.DOT_TRIPS)
    colour_trip_ord = random_gen(constants.COLOUR_TRIPS)

    # If a random ordering was not generated, keep attempting to generate one until both dot and colour have a random
    # ordering.
    while not dot_trip_ord or not colour_trip_ord:
        dot_trip_ord = random_gen(constants.DOT_TRIPS)
        colour_trip_ord = random_gen(constants.COLOUR_TRIPS)

    # Turn the randomly generated orderings into 2 tables
    df_dots = pd.DataFrame(dot_trip_ord, columns=["d1", "d2", "d3"])
    df_colours = pd.DataFrame(colour_trip_ord, columns=["c1", "c2", "c3"])

    # Merge the two tables into one.
    df_output = pd.merge(df_dots, df_colours, left_index=True, right_index=True, how='outer')

    square_prob_array = ss.bernoulli.rvs(0.1, size=135)
    for j in range(len(square_prob_array) - 1, -1, -1):
        if square_prob_array[j]:
            print 1
            square = pd.Series(np.nan, index=df_output.columns.values)
            result = df_output.ix[:j]
            result = result.append(square, ignore_index=True)
            result = result.append(df_output.ix[j + 1:], ignore_index=True)
            df_output = result
    # Add participant row to table
    result['participant'] = i

    # Save the table into a CSV file
    result.to_csv("participant_%d.csv" % 11)
