import glob
import pandas as pd
import olives.Constants as Constants
from participant_generator import generate_trip_ordering_csv
from participant_test_generator import generate_test_trip_ordering_csv


def training_prob():
    """
    Calculates probability of a dot matching with a colour.
    If there is a probability greater than the max probability (as defined as 'MAX_PROB' in Constants) for a particular
    dot to appear with a particular colour, then a new participant training file will get created.
    """
    participants = glob.glob('%s/*/participant_?.csv' % Constants.PARTICIPANT_PATH)

    for participant_path in participants:
        successful = False
        output_df = pd.DataFrame()
        df = pd.read_csv(participant_path)

        # Get the participant number.
        # All values in the participant col is the same. It's fine to get it from any index.
        participant_num = df[Constants.VALUE].tolist()[0]

        while not successful:
            # Pairs for grouping the table

            # Group by the current colour and dot pair and count the number of grouped rows
            df_trip = df.groupby([Constants.COLOUR_COL, Constants.DOT_COL]).count()

            # Remove all unnecessary columns and only keep one column which contains the number of grouped rows
            df_trip = df_trip[Constants.VALUE]

            # Convert series into DataFrame
            df_trip = df_trip.to_frame()

            # Divide the rows that represent number of grouped rows by the number of random orders.
            # This will give the probability for colour/dot appearing
            df_trip[Constants.VALUE] /= Constants.NUM_RAND_ORD

            # Convert the index columns into normal columns (Required for creating pivot table).
            df_trip.reset_index(level=[Constants.COLOUR_COL, Constants.DOT_COL], inplace=True)

            # Flip i[constants.DOT_INDEX] & i[constants.COLOUR_INDEX] to show probability for colours
            df_trip = df_trip.pivot_table(index=Constants.DOT_COL, columns=Constants.COLOUR_COL,
                                          values=Constants.VALUE)

            # Provide a better name for index and column
            # Flip 'index' and 'colour' for showing probability for dots
            df_trip.index.names, df_trip.columns.names = ['Dot'], ['Colour']

            # join the created table with the previous tables.
            output_df = output_df.join(df_trip, how="outer")

            # Replace NaN values with 0
            output_df = output_df.fillna(0)

            # Generate new participant file and recalculate probability if there exists a cell in the probability table
            # that is greater than the maximum allowed probability.
            temp_df = output_df
            if len(temp_df[(temp_df > Constants.MAX_PROB).any(axis=1)].index) == 0:
                successful = True
            else:
                print 'Replacing Participant %d Test file.' % participant_num
                generate_trip_ordering_csv(participant_num)
                output_df = pd.DataFrame()

        # Sort columns in alphabetical order
        # output_df.sort_index(axis=1, inplace=True)

        # Add participant column to table
        output_df['participant'] = participant_num

        # Save output to CSV
        output_df.to_csv(Constants.PARTICIPANT_PROBABILITY_FILE_PATH % (participant_num, participant_num))


def test_prob():
    """
    Calculates probability of the correct stim appearing on the right and left side of the screen.
    If the probability of the correct stim appearing on either side is greater than the max probability
    (as defined as 'MAX_STIM_PROB' in Constants), then a new participant test file will get created.
    """

    participants = glob.glob('%s/*/participant_?_test.csv' % Constants.PARTICIPANT_PATH)

    for participant_path in participants:

        successful = False
        output_df = pd.DataFrame()
        df = pd.read_csv(participant_path)

        # Get the participant number.
        # All values in the participant col is the same. It's fine to get it from any index.
        participant_num = df[Constants.VALUE].tolist()[0]

        max_count = int(len(df) * Constants.MAX_TEST_PROB)

        while not successful:
            # Group by correct column and count number of correct stim on left and right
            output_df = df.groupby(Constants.TEST_CORRECT_COL).count()

            # Each row has same value for all columns. Take only one column
            output_df = output_df[Constants.VALUE]

            # Reset the index after grouping (Left and Right should be a column).
            output_df = output_df.reset_index([0, 1])

            # Rename the participant column to 'count' to represent the number of correct stim for each side.
            output_df.rename(columns={'participant': 'count'}, inplace=True)

            # Create new participant file if it is over the max probability allowed.
            if (output_df['count'] < max_count).any():
                successful = True
            else:
                print 'Replacing Participant %d Test file.' % participant_num
                generate_test_trip_ordering_csv(participant_num)
                output_df = pd.DataFrame()

        # Add participant column to table
        output_df['participant'] = participant_num

        # Save test probability file.
        output_df.to_csv(Constants.PARTICIPANT_TEST_PROBABILITY_FILE_PATH % (participant_num, participant_num),
                         index=False)


if __name__ == '__main__':
    training_prob()
    test_prob()
