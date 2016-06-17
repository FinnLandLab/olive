import pandas as pd
import numpy as np
import scipy.stats as ss
import olives.Constants as Constants
import glob
import os

# Find all participant folders (participant folders are labeled as the participant numbera)
participants = glob.glob('%s/[0-9]*/' % Constants.PARTICIPANT_PATH)

# Read the Test file that contains all combinations.
df = pd.read_csv(Constants.TEST_FILE_PATH)

for participant_path in participants:
    # Get participant number from the path (name of folder).
    participant_num = int(participant_path.split(os.sep)[1])

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
    grouped_df['correct'] = ['Right' if i else 'Left' for i in idx]

    grouped_df['participant'] = participant_num

    # Switch Left and Right stim based on the idx Series. If false, nothing happens; if true, the columns get switched.
    grouped_df.loc[idx, Constants.TEST_LEFT_COL_NAMES + Constants.TEST_RIGHT_COL_NAMES] = grouped_df.loc[
        idx, Constants.TEST_RIGHT_COL_NAMES + Constants.TEST_LEFT_COL_NAMES].values

    grouped_df.to_csv(Constants.PARTICIPANT_TEST_FILE_PATH % (participant_num, participant_num), index=False)
