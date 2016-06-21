# Number of random orderings created
NUM_RAND_ORD = 45

# Number of participants (used to creating participant and probability CSV files)
NUM_OF_PARTICIPANTS = 10

# Used when wanting to find number of rows in a DataFrame
VALUE = 'participant'

# Probability of getting a square
SQUARE_PROB = 0.1

# Max probability allowed for a colour to match with a dot value
MAX_PROB = 0.6

BLOCKS = ['PRACTICE', 'TRAINING', 'TEST']
INSTRUCTIONS = ['PRACTICE', 'TRAINING', 'TEST']
GRAPHICS = ['CIRCLE', 'DOT', 'SQUARE', "TRAINING_LEFT_STIM", "TRAINING_RIGHT_STIM", 'QUESTION_MARK']

############################################################
###                    TRIPLET VALUES                    ###
############################################################
DOT_TRIPS = [[1, 8, 6], [9, 2, 4], [5, 7, 3]]
COLOUR_TRIPS = [['Blue', 'Red', 'Green'], ['Yellow', 'LightPink', 'Brown'], ['Purple', 'Orange', 'DarkGray']]

# Index of colour in 'INDEX_AND_COL_TRIP' array
COLOUR_INDEX = 0
# Index of dot in 'INDEX_AND_COL_TRIP' array
DOT_INDEX = 1

############################################################
###                 DATA OUTPUT COLUMNS                  ###
############################################################
DATA_OUTPUT_COL = 'response'
DATA_OUTPUT_RESP_COL = 'response_time'
DOT_COL = 'dot_values'
COLOUR_COL = 'colour_values'
INDEX_AND_COL_TRIP = [DOT_COL, COLOUR_COL]
TEST_LEFT_COL_NAMES = ['stim1_dots1', 'stim1_dots2', 'stim1_dots3', 'stim1_color1', 'stim1_color2', 'stim1_color3']
TEST_RIGHT_COL_NAMES = ['stim2_dots1', 'stim2_dots2', 'stim2_dots3', 'stim2_color1', 'stim2_color2', 'stim2_color3']

############################################################
###                      KEYBOARD KEYS                   ###
############################################################
ESCAPE_KEYS = ['esc', 'escape']
SKIP_KEYS = ['tab']
SPACE_KEYS = ['space']
CIRCLE_KEYS = ['x', 'X']
SQUARE_KEYS = ['N', 'n']
PRACTICE_RESP_KEYS = ['N', 'n', 'X', 'x']
CIRCLE_KEY = 'x'
SQUARE_KEY = 'n'

############################################################
###                 DATA OUTPUT COLUMNS                  ###
############################################################
DISPLAY_VISUAL_TIME = 0.6  # Seconds
NO_VISUAL_TIME = 0.2  # Seconds

############################################################
###                    VISUAL VALUES                     ###
############################################################
# Window
WIN_SIZE = (1000, 500)  # (1920, 1080)
WIN_FULL_SCREEN = True  # True

# Shapes
DOT_CORD_VERT_OFFSET = 2.5
DOT_CORD_HORZ_OFFSET = 3
TEST_STIM_SHIFT = 10

SHAPE_EDGE = 66
CIRCLE_RADIUS = 5
DOT_RADIUS = 1
DOT_FILL_COL = 'black'
DOT_LINE_COL = 'black'
SQUARE_WIDTH = 0.4
SQUARE_HEIGHT = 0.8
SQUARE_LINE_COL = 'white'
SQUARE_FILL_COL = 'white'
CENTER_CORD = [0, 0]

# Dot coordinates for positioning
DOT_CORD = {1: (-DOT_CORD_VERT_OFFSET, -DOT_CORD_VERT_OFFSET), 2: (0, -DOT_CORD_HORZ_OFFSET),
            3: (DOT_CORD_VERT_OFFSET, -DOT_CORD_VERT_OFFSET),
            4: (-DOT_CORD_HORZ_OFFSET, 0), 5: (0, 0), 6: (DOT_CORD_HORZ_OFFSET, 0),
            7: (-DOT_CORD_VERT_OFFSET, DOT_CORD_VERT_OFFSET),
            8: (0, DOT_CORD_HORZ_OFFSET), 9: (DOT_CORD_VERT_OFFSET, DOT_CORD_VERT_OFFSET)}

TEST_LEFT_DOT_CORD = {1: (-DOT_CORD_VERT_OFFSET - TEST_STIM_SHIFT, -DOT_CORD_VERT_OFFSET),
                      2: (- TEST_STIM_SHIFT, -DOT_CORD_HORZ_OFFSET),
                      3: (DOT_CORD_VERT_OFFSET - TEST_STIM_SHIFT, -DOT_CORD_VERT_OFFSET),
                      4: (-DOT_CORD_HORZ_OFFSET - TEST_STIM_SHIFT, 0),
                      5: (- TEST_STIM_SHIFT, 0),
                      6: (DOT_CORD_HORZ_OFFSET - TEST_STIM_SHIFT, 0),
                      7: (-DOT_CORD_VERT_OFFSET - TEST_STIM_SHIFT, DOT_CORD_VERT_OFFSET),
                      8: (- TEST_STIM_SHIFT, DOT_CORD_HORZ_OFFSET),
                      9: (DOT_CORD_VERT_OFFSET - TEST_STIM_SHIFT, DOT_CORD_VERT_OFFSET)}

TEST_RIGHT_DOT_CORD = {1: (-DOT_CORD_VERT_OFFSET + TEST_STIM_SHIFT, -DOT_CORD_VERT_OFFSET),
                       2: (TEST_STIM_SHIFT, -DOT_CORD_HORZ_OFFSET),
                       3: (DOT_CORD_VERT_OFFSET + TEST_STIM_SHIFT, -DOT_CORD_VERT_OFFSET),
                       4: (-DOT_CORD_HORZ_OFFSET + TEST_STIM_SHIFT, 0),
                       5: (TEST_STIM_SHIFT, 0),
                       6: (DOT_CORD_HORZ_OFFSET + TEST_STIM_SHIFT, 0),
                       7: (-DOT_CORD_VERT_OFFSET + TEST_STIM_SHIFT, DOT_CORD_VERT_OFFSET),
                       8: (+ TEST_STIM_SHIFT, DOT_CORD_HORZ_OFFSET),
                       9: (DOT_CORD_VERT_OFFSET + TEST_STIM_SHIFT, DOT_CORD_VERT_OFFSET)}

############################################################
###                     PATHS                            ###
############################################################
PARTICIPANT_PATH = '../participants'
PARTICIPANT_PROBABILITY_FILE_PATH = '../participants/%d/participant_%d_probability.csv'
PARTICIPANT_TEST_FILE_PATH = '../participants/%d/participant_%d_test.csv'
PARTICIPANT_FILE_PATH = '../participants/%d/participant_%d.csv'
PARTICIPANT_FOLDER_PATH = '../participants/%d'
DATA_PATH = '../data'
TEST_FILE_PATH = '../test_items.csv'
