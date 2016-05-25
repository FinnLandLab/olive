# Number of random orderings created
NUM_RAND_ORD = 45

# Number of participants (used to creating participant and probability CSV files)
NUM_OF_PARTICIPANTS = 10

# Delay between each Trial
STIM_DELAY = 0.4  # seconds

# Used when wanting to find number of rows in a DataFrame
VALUE = 'participant'

# Probability of getting a square
SQUARE_PROB = 0.1

# Max probability allowed for a colour to match with a dot value
MAX_PROB = 0.6

############################################################
###                    TRIPLET VALUES                    ###
############################################################
DOT_TRIPS = [[1, 8, 6], [9, 2, 4], [5, 7, 3]]
COLOUR_TRIPS = [['Blue', 'Red', 'Green'], ['Yellow', 'Pink', 'Brown'], ['Purple', 'Orange', 'DarkGray']]
DOT_COLS = ['d1', 'd2', 'd3']
COLOUR_COLS = ['c1', 'c2', 'c3']
INDEX_AND_COL_TRIP = [('c1', 'd1'), ('c2', 'd2'), ('c3', 'd3')]

# Index of colour in 'INDEX_AND_COL_TRIP' array
COLOUR_INDEX = 0
# Index of dot in 'INDEX_AND_COL_TRIP' array
DOT_INDEX = 1

############################################################
###                    VISUAL VALUES                     ###
############################################################
DOT_CORD_VERT_OFFSET = 2.5
DOT_CORD_HORZ_OFFSET = 3

# Dot coordinates for positioning
DOT_CORD = {1: (-DOT_CORD_VERT_OFFSET, -DOT_CORD_VERT_OFFSET), 2: (0, -DOT_CORD_HORZ_OFFSET),
            3: (DOT_CORD_VERT_OFFSET, -DOT_CORD_VERT_OFFSET),
            4: (-DOT_CORD_HORZ_OFFSET, 0), 5: (0, 0), 6: (DOT_CORD_HORZ_OFFSET, 0),
            7: (-DOT_CORD_VERT_OFFSET, DOT_CORD_VERT_OFFSET),
            8: (0, DOT_CORD_HORZ_OFFSET), 9: (DOT_CORD_VERT_OFFSET, DOT_CORD_VERT_OFFSET)}

############################################################
###                     PATHS                            ###
############################################################
PARTICIPANT_PATH = '../static/participants'
PARTICIPANT_PROBABILITY_FILE_PATH = '../static/participants/probabilities/participant_%s_probability.csv'
PARTICIPANT_FILE_PATH = '../static/participants/participant_%s.csv'
SQUARE_IMAGE_PATH = '../static/images/rainbow_square.png'
DATA_PATH = '../data'
