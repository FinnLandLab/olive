import pandas as pd
import constants

df = pd.read_csv("participant_1.csv")

# Drop the first column (index)
df.drop(df.columns[0], axis=1, inplace=True)

# Pairs for grouping the table
index_and_col_trip = [('c1', 'd1'), ('c2', 'd2'), ('c3', 'd3')]

output_df = pd.DataFrame()

# Go through each colour and dot pair and find all the probability for each and join the tables together into one table
for i in index_and_col_trip:
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

    # Flip i[COLOUR_INDEX] & i[DOT_INDEX] to show probability for colours
    df_trip = df_trip.pivot_table(index=i[constants.COLOUR_INDEX], columns=i[constants.DOT_INDEX],
                                  values=constants.VALUE)

    # Provide a better name for index and column
    # Flip 'colour' and 'number' for showing probability for colours
    df_trip.index.names, df_trip.columns.names = ['colour'], ['number']

    # join the created table with the previous tables.
    output_df = output_df.join(df_trip, how="outer")

# Replace NaN values with 0
output_df = output_df.fillna(0)

# Sort columns in alphabetical order
# output_df.sort_index(axis=1, inplace=True)

print output_df

# Save output to CSV
output_df.to_csv("dot_probability.csv")
