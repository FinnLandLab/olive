import glob

from participant_generator import *

participants = glob.glob('%s/*.csv' % constants.PARTICIPANT_PATH)

for participant_path in participants:
    successful = False
    output_df = pd.DataFrame()
    df = pd.read_csv(participant_path)

    # Get the participant number.
    # All values in the participant col is the same. It's fine to get it from any index.
    participant_num = df['participant'].tolist()[0]

    while not successful:
        # Pairs for grouping the table

        # Go through each colour and dot pair and find all the probability for each and join the tables together into
        # one table.
        for i in constants.INDEX_AND_COL_TRIP:
            # Group by the current colour and dot pair and count the number of grouped rows
            df_trip = df.groupby([i[constants.COLOUR_INDEX], i[constants.DOT_INDEX]]).count()

            # Remove all unnecessary columns and only keep one column which contains the number of grouped rows
            df_trip = df_trip[constants.VALUE]

            # Convert series into DataFrame
            df_trip = df_trip.to_frame()

            # Divide the rows that represent number of grouped rows by the number of random orders.
            # This will give the probability for colour/dot appearing
            df_trip[constants.VALUE] /= constants.NUM_RAND_ORD

            # Convert the index columns into normal columns (Required for creating pivot table).
            df_trip.reset_index(level=[i[constants.COLOUR_INDEX], i[constants.DOT_INDEX]], inplace=True)

            # Flip i[constants.DOT_INDEX] & i[constants.COLOUR_INDEX] to show probability for colours
            df_trip = df_trip.pivot_table(index=i[constants.DOT_INDEX], columns=i[constants.COLOUR_INDEX],
                                          values=constants.VALUE)

            # Provide a better name for index and column
            # Flip 'index' and 'colour' for showing probability for dots
            df_trip.index.names, df_trip.columns.names = ['index'], ['colour']

            # join the created table with the previous tables.
            output_df = output_df.join(df_trip, how="outer")

        # Replace NaN values with 0
        output_df = output_df.fillna(0)

        # Generate new participant file and recalculate probability if there exists a cell in the probability table
        # that is greater than the maximum allowed probability.
        temp_df = output_df
        if len(temp_df[(temp_df > constants.MAX_PROB).any(axis=1)].index) == 0:
            successful = True
        else:
            generate_trip_ordering_csv(participant_num)
            output_df = pd.DataFrame()

    # Sort columns in alphabetical order
    # output_df.sort_index(axis=1, inplace=True)

    # Add participant column to table
    output_df['participant'] = participant_num

    # Save output to CSV
    output_df.to_csv(
        constants.PARTICIPANT_PROBABILITY_FILE_PATH % participant_num)
