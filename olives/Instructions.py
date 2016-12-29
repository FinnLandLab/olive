from psychopy import event, core
import time
import Constants


def load_instructions(graphics, instructions_list, delay=0, stim=None):
    """
    Loads the instructions based on graphics object and current set instruction in graphics
    :param stim: Provide special stim if instruction format is different
    :param delay: Delay after all instructions are displayed. Default is 0
    :param instructions_list: A list of strings where each item in the list represents an instruction page message
    :param graphics: The graphics object which holds the instructions
    """

    # Go through every instruction in the list of instructions
    for instruction in instructions_list:

        if stim is None:
            graphics.set_instruction(instruction)
            graphics.get_instruction().draw()
        else:
            graphics.set_text(stim, instruction)
            graphics.draw(stim)

        # Get the current instruction and display it on the screen
        graphics.refresh()

        # Keep displaying the instructions until the user presses the key to continue or the key to exit.
        while True:
            time.sleep(1)  # Reduces amount of resources used
            if event.getKeys(keyList=Constants.ESCAPE_KEYS):
                core.quit()
            elif event.getKeys(keyList=Constants.SPACE_KEYS):
                break

        graphics.refresh()
        time.sleep(delay)
