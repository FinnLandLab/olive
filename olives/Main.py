from Practice import display_practice
from Test import display_test
from Instructions import load_instructions
from Training import display_training
from psychopy import core
from ReactionTime import display_rt
import Graphics
import DataHandlers
import Constants

# Create handlers and graphics
data_handlers = DataHandlers.DataHandlers()
graphics = Graphics.Graphics()

# TRAINING PHASE
data_handlers.set_exp_handler(Constants.PHASE_TRAINING)
load_instructions(graphics, Constants.TRAINING_INSTRUCTIONS)
display_training(data_handlers, graphics)

# PRACTICE PHASE
load_instructions(graphics, Constants.PRACTICE_INSTRUCTIONS)
display_practice(graphics)

# RT PHASE
data_handlers.set_exp_handler(Constants.PHASE_REACTION_TIME)
load_instructions(graphics, Constants.RT_INSTRUCTIONS)
display_rt(data_handlers, graphics)

# TEST PHASE
data_handlers.set_exp_handler(Constants.PHASE_TEST)
load_instructions(graphics, Constants.TEST_INSTRUCTIONS)
display_test(data_handlers, graphics)


load_instructions(graphics, Constants.FINAL_INSTRUCTIONS)

core.quit()
