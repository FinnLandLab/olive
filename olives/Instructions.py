from psychopy import event, core
import time
import Constants


def load_instructions(graphics, instructions_list):
    """
    Loads the instructions based on graphics object and current set instruction in graphics
    :param instructions_list: A list of strings where each item in the list represents an instruction page message
    :param graphics: The graphics object which holds the instructions
    """

    # Go through every instruction in the list of instructions
    for instruction in instructions_list:

        graphics.set_instruction(instruction)

        # Get the current instruction and display it on the screen
        graphics.get_instruction().draw()
        graphics.refresh()

        # Keep displaying the instructions until the user presses the key to continue or the key to exit.
        while True:
            time.sleep(1)  # Reduces amount of resources used
            if event.getKeys(keyList=Constants.ESCAPE_KEYS):
                core.quit()
            elif event.getKeys(keyList=Constants.SPACE_KEYS):
                break
