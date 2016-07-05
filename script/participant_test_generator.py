import pandas as pd
import numpy as np
import scipy.stats as ss
import olives.Constants as Constants
import os


def _generate_participant_folder(num):
    if not os.path.exists(Constants.PARTICIPANT_FOLDER_PATH % num):
        os.makedirs(Constants.PARTICIPANT_FOLDER_PATH % num)


def generate_test_trip_ordering_csv(participant):
    _generate_participant_folder(participant)

    # Read the Test file that contains all combinations.
    df = pd.read_csv(Constants.TEST_FILE_PATH)

    # Lambda function that selects 2 rows at random without replacement from a column in the given DataFrame.
    group_by_op = lambda x: x.loc[np.random.choice(x.index, size=2, replace=False), :]

    # Group the DataFrame using the comparison column by selecting 2 items for each comparison value by random.
    # Reset the index so that the grouped column does not turn into an index.
    grouped_df = df.groupby('comparison', as_index=False).apply(group_by_op).reset_index(level=[0, 1])

    # Drop the first two columns which represented information about the grouping. (Information is irrelevant)
    grouped_df = grouped_df.drop(grouped_df.columns[[0, 1]], axis=1)

    # Remove last row. (Last row is a duplicate of the one before it so it could get paired in grouping.
    grouped_df = grouped_df[:-1]

    # Create a Series of True/False values which later get used to determine whether Left and Right stim need to get
    # switched. Needs to be type bool to work.
    idx = pd.Series(ss.bernoulli.rvs(p=0.5, size=len(grouped_df))).astype(bool)

    # Add column that says whether the Left and Right stim where switched based on idx Series value.
    grouped_df['correct'] = ['Right' if j else 'Left' for j in idx]

    grouped_df['participant'] = participant

    # Switch Left and Right stim based on the idx Series. If false, nothing happens; if true, the columns get switched.
    grouped_df.loc[idx, Constants.TEST_LEFT_COL_NAMES + Constants.TEST_RIGHT_COL_NAMES] = grouped_df.loc[
        idx, Constants.TEST_RIGHT_COL_NAMES + Constants.TEST_LEFT_COL_NAMES].values

    # Shuffle the colour and dots test rows
    grouped_df = pd.concat([grouped_df.iloc[np.random.permutation(range(Constants.NUM_OF_COLOUR_DOT_TEST_COMP))],
                            grouped_df.iloc[Constants.NUM_OF_COLOUR_DOT_TEST_COMP:]])

    grouped_df.to_csv(Constants.PARTICIPANT_TEST_FILE_PATH % (participant, participant), index=False)


if __name__ == '__main__':
    for i in range(100, Constants.NUM_OF_PARTICIPANTS + 101):
        generate_test_trip_ordering_csv(i)
