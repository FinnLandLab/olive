# Number of random orderings created
NUM_RAND_ORD = 45

# Number of participants (used to creating participant and probability CSV files)
NUM_OF_PARTICIPANTS = 99

# Used when wanting to find number of rows in a DataFrame
VALUE = 'participant'

# Probability of getting a square
SQUARE_PROB = 0.1

# Max probability allowed for a colour to match with a dot value
MAX_PROB = 0.6

# Max probability allowed for the correct stim to appear on one given side for test phase
MAX_TEST_PROB = 0.75

# Number of test items for both colours and dots during the test phase.
NUM_OF_COLOUR_DOT_TEST_COMP = 24

############################################################
###                    TRIPLET VALUES                    ###
############################################################
DOT_TRIPS = [[1, 8, 6], [9, 2, 4], [5, 7, 3]]
COLOUR_TRIPS = [['Blue', 'Red', 'Green'], ['Yellow', 'LightPink', 'Brown'], ['Purple', 'Orange', 'DarkGray']]

# Index of colour in 'INDEX_AND_COL_TRIP' array
COLOUR_INDEX = 0
# Index of dot in 'INDEX_AND_COL_TRIP' array
DOT_INDEX = 1

# Practice left and right trials
PRACTICE_LEFT_STIMS = [['A', 'B', 'C'], ['Z', 'X', 'Y']]
PRACTICE_RIGHT_STIMS = [['B', 'C', 'A'], ['X', 'Y', 'Z']]
############################################################
###                      KEYBOARD KEYS                   ###
############################################################
ESCAPE_KEYS = ['esc', 'escape']
SKIP_KEYS = ['tab']
SPACE_KEYS = ['space']
CIRCLE_KEYS = ['z', 'Z']
SQUARE_KEYS = ['m', 'M']
LEFT_STIM_KEYS = ['1', 1]
RIGHT_STIM_KEYS = ['0', 0]
PRACTICE_RESP_KEYS = ['1', '0', 1, 0]
CIRCLE_KEY = 'z'
SQUARE_KEY = 'm'
LEFT_STIM_KEY = '1'
RIGHT_STIM_KEY = '0'

############################################################
###                     DATA COLUMNS                     ###
############################################################
DATA_OUTPUT_COL = 'response'
DATA_OUTPUT_RESP_COL = 'response_time'
TEST_OUTPUT_COL = 'stim_response'  # Used for direction (left stim or right stim)
TEST_STIM_RESP = {LEFT_STIM_KEY: 'Left', RIGHT_STIM_KEY: 'Right'}
DOT_COL = 'dot_values'
COLOUR_COL = 'colour_values'
TEST_CORRECT_COL = 'correct'
INDEX_AND_COL_TRIP = [DOT_COL, COLOUR_COL]
TEST_LEFT_COL_NAMES = ['stim1_dots1', 'stim1_dots2', 'stim1_dots3', 'stim1_color1', 'stim1_color2', 'stim1_color3']
TEST_RIGHT_COL_NAMES = ['stim2_dots1', 'stim2_dots2', 'stim2_dots3', 'stim2_color1', 'stim2_color2', 'stim2_color3']
TEST_LEFT_COL_ORD = [['stim1_dots1', 'stim1_dots2', 'stim1_dots3'], ['stim1_color1', 'stim1_color2', 'stim1_color3']]
TEST_RIGHT_COL_ORD = [['stim2_dots1', 'stim2_dots2', 'stim2_dots3'], ['stim2_color1', 'stim2_color2', 'stim2_color3']]

############################################################
###                 TIME VALUES                          ###
############################################################
DISPLAY_VISUAL_TIME = 0.6  # Seconds
NO_VISUAL_TIME = 0.2  # Seconds
TEST_DELAY_BETWEEN_TRIALS = 1  # Seconds

############################################################
###                    VISUAL VALUES                     ###
############################################################
# Window
WIN_SIZE = (1000, 500)  # (1920, 1080)
WIN_FULL_SCREEN = True  # True

# Values for graphics variables
BLOCKS = ['PRACTICE', 'TRAINING', 'TEST']
INSTRUCTIONS = ['PRACTICE', 'TRAINING', 'TEST', 'ENDING']
GRAPHICS = ['CIRCLE', 'DOT', 'SQUARE', 'PRACTICE_LEFT_STIM', 'PRACTICE_RIGHT_STIM', 'QUESTION_MARK']

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

# Psychopy Visuals
VIS_CIRCLE = 'CIRCLE'
VIS_DOT = 'DOT'
VIS_SQUARE = 'SQUARE'
VIS_PRACTICE_LEFT_STIM = 'PRACTICE_LEFT_STIM'
VIS_PRACTICE_RIGHT_STIM = 'PRACTICE_RIGHT_STIM'
VIS_QUESTION_MARK = 'QUESTION_MARK'

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
PARTICIPANT_TEST_PROBABILITY_FILE_PATH = '../participants/%d/participant_%d_test_probability.csv'
PARTICIPANT_TEST_FILE_PATH = '../participants/%d/participant_%d_test.csv'
PARTICIPANT_FILE_PATH = '../participants/%d/participant_%d_training.csv'
PARTICIPANT_FOLDER_PATH = '../participants/%d'
DATA_PATH = '../data'
TEST_FILE_PATH = '../test_items.csv'

############################################################
###                        PHASES                        ###
############################################################
PHASE_PRACTICE = 'PRACTICE'
PHASE_TRAINING = 'TRAINING'
PHASE_TEST = 'TEST'
PHASE_ENDING = 'ENDING'

############################################################
###                    INSTRUCTIONS                      ###
############################################################

TRAINING_INSTRUCT_1 = 'In this experiment you will see a series of images. These will be either blank squares or' \
                      ' colored circles with smaller circles inside. If you see a square press \'z\' and if you see a' \
                      ' circle press \'m\'\n\nPress space to continue'

TRAINING_INSTRUCT_2 = 'There will be many more circles than squares. The experiment will last about 6 minutes. ' \
                      'Please do your best to press the correct button as quickly as possible.\n\n' \
                      'Press space to continue'

TRAINING_INSTRUCT_3 = 'Press space when you are ready'

TRAINING_INSTRUCTIONS = [TRAINING_INSTRUCT_1, TRAINING_INSTRUCT_2, TRAINING_INSTRUCT_3]

PRACTICE_INSTRUCT_1 = 'Great job!\n\nNow we have a few short questions about the circles.\n\nPress space to continue'

PRACTICE_INSTRUCT_2 = 'In this next phase, you will see three circles presented in succession on the left side, these' \
                      ' will disappear and then three circles will be presented in succession on the right side and ' \
                      'then disappear.\n\nPress space to continue'

PRACTICE_INSTRUCT_3 = 'Please choose which set of circles - the ones presented on the left or the right - are more ' \
                      'likely to belong in the sequence of circles that you were just exposed to.' \
                      '\n\nPress space to continue'

PRACTICE_INSTRUCT_4 = 'You might not feel like you know the answer to this, but just take your best guess. \n' \
                      'Press 1 if you think the set on the left is more likely to belong and 0 if you think the set ' \
                      'on the right is more likely to belong.\n\nPress space to continue'

PRACTICE_INSTRUCT_5 = 'Before we do circles, lets quickly practice with letters. Which of the sets of letters fits' \
                      ' better in the alphabet?\n\nPress space to continue'

PRACTICE_INSTRUCT_6 = 'Press 1 if you think the set on the left and 0 if you think it\'s the one on the right. Once ' \
                      'you select, the experiment will automatically forward to the next question.\n\nPress space to ' \
                      'continue'

PRACTICE_INSTRUCT_7 = 'Ready?\n\nPress space to start practice.'

PRACTICE_INSTRUCTIONS = [PRACTICE_INSTRUCT_1, PRACTICE_INSTRUCT_2, PRACTICE_INSTRUCT_3, PRACTICE_INSTRUCT_4,
                         PRACTICE_INSTRUCT_5, PRACTICE_INSTRUCT_6, PRACTICE_INSTRUCT_7]

TEST_INSTRUCT_1 = 'Now lets do circles.  Please choose which set of circles - the ones presented on the left or the ' \
                  'right - are more likely to belong in the sequence of circles that you were just exposed to.' \
                  '\n\nPress space to continue'

TEST_INSTRUCT_2 = 'Press 1 if you think the set on the left is more likely to belong and 0 if you think the set on ' \
                  'the right is more likely to belong.\n\nPress space to continue'

TEST_INSTRUCT_3 = 'Once you select, the experiment will automatically forward to the next question.' \
                  '\n\nPress space to continue'

TEST_INSTRUCT_4 = 'Ready?\n\nPress space to start. This will take about 3 minutes.'

TEST_INSTRUCTIONS = [TEST_INSTRUCT_1, TEST_INSTRUCT_2, TEST_INSTRUCT_3, TEST_INSTRUCT_4]

FINAL_INSTRUCT_1 = 'Thank you for participating the experiment!'

FINAL_INSTRUCTIONS = [FINAL_INSTRUCT_1]
