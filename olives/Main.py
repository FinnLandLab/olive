from Practice import display_practice
from Test import display_test
from Instructions import load_instructions
from Training import display_training
from psychopy import core
import Graphics
import DataHandlers

# Create handlers and graphics
data_handlers = DataHandlers.DataHandlers()
graphics = Graphics.Graphics()

# TRAINING PHASE
data_handlers.set_exp_handler('TRAINING')
graphics.set_instruction('TRAINING')
load_instructions(graphics)
display_training(data_handlers, graphics)

# PRACTICE PHASE
graphics.set_instruction('PRACTICE')
load_instructions(graphics)
display_practice(graphics)

# TEST PHASE
data_handlers.set_exp_handler('TEST')
graphics.set_instruction('TEST')
load_instructions(graphics)
display_test(data_handlers, graphics)

core.quit()
