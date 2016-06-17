import pandas as pd
import numpy as np
import scipy.stats as ss
import olives.Constants as Constants
import glob
import os

participants = glob.glob('%s/[0-9]*/' % Constants.PARTICIPANT_PATH)

df = pd.read_csv(Constants.TEST_FILE_PATH)

for participant_path in participants:
    participant_num = int(participant_path.split(os.sep)[1])

    group_by_op = lambda x: x.loc[np.random.choice(x.index, size=2, replace=False), :]

    grouped_df = df.groupby('comparison', as_index=False).apply(group_by_op).reset_index(level=[0, 1])

    grouped_df = grouped_df.drop(grouped_df.columns[[0, 1]], axis=1)
    grouped_df = grouped_df[:-1]

    idx = pd.Series(ss.bernoulli.rvs(p=0.5, size=len(grouped_df))).astype(bool)

    grouped_df['correct'] = ['Right' if i else 'Left' for i in idx]
    grouped_df['participant'] = participant_num

    grouped_df.loc[idx, Constants.TEST_LEFT_COL_NAMES + Constants.TEST_RIGHT_COL_NAMES] = grouped_df.loc[
        idx, Constants.TEST_RIGHT_COL_NAMES + Constants.TEST_LEFT_COL_NAMES].values

    grouped_df.to_csv(Constants.PARTICIPANT_TEST_FILE_PATH % (participant_num, participant_num), index=False)
