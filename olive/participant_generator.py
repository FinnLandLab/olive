import random

import numpy as np
import pandas as pd
import scipy.stats as ss

import constants


def _random_gen(trip_list):
    """
    Generate a random ordering of the given list repeated constants.NUM_RAND_ORD times.
    No item in the random ordering can be adjacent to itself.
    :param trip_list: The list to be repeated and randomized
    :return: trip_list repeated constants.NUM_RAND_ORD times and randomized.
    """
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

            # If a random ordering that satisfies the restriction is not possible given the remaining items, recall the
            # function and try again until an ordering can be generated.
            temp = rand_ord[:]
            temp = [x for x in temp if x != dot_ordering[-1]]
            if not temp:
                return _random_gen(trip_list)

    return dot_ordering


def generate_trip_ordering_csv(participant_number):
    """
    Generate random ordering for dot and colour triplets that are independent from one another.
    Allow for an empty row to appear for each row with a probability of constants.SQUARE_PROB.
    :param participant_number: Participant Number
    """
    dot_trip_ord = _random_gen(constants.DOT_TRIPS)
    colour_trip_ord = _random_gen(constants.COLOUR_TRIPS)

    # Turn the randomly generated orderings into 2 tables
    df_dots = pd.DataFrame(dot_trip_ord, columns=constants.DOT_COLS)

    # Add additional row to dots table with empty values
    offset = pd.Series(np.nan, index=df_dots.columns.values)
    result = df_dots.ix[:-1]
    result = result.append(offset, ignore_index=True)
    result = result.append(df_dots[0:], ignore_index=True)
    df_dots = result

    df_colours = pd.DataFrame(colour_trip_ord, columns=constants.COLOUR_COLS)
    offset = pd.Series(np.nan, index=df_colours.columns.values)
    df_colours = df_colours.append(offset, ignore_index=True)

    # Merge the two tables into one.
    df_output = pd.merge(df_dots, df_colours, left_index=True, right_index=True, how='outer')

    # Insert an additional empty row in each row with the probability of the square appearing.
    square_prob_array = ss.bernoulli.rvs(constants.SQUARE_PROB, size=len(df_output.index))
    for j in range(len(square_prob_array) - 1, -1, -1):
        # If it should appear, place an additional empty row in the given index
        if square_prob_array[j]:
            square = pd.Series(np.nan, index=df_output.columns.values)
            result = df_output.ix[:j]
            result = result.append(square, ignore_index=True)
            result = result.append(df_output.ix[j + 1:], ignore_index=True)
            df_output = result

    # Add participant row to table
    df_output['participant'] = participant_number

    # Save the table into a CSV file
    df_output.to_csv(constants.PARTICIPANT_FILE_PATH % participant_number, index=False)


if __name__ == '__main__':
    for i in range(1, constants.NUM_OF_PARTICIPANTS + 1):
        generate_trip_ordering_csv(i)
