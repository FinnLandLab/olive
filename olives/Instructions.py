from psychopy import event, core
import time
import Constants


def load_instructions(graphics):
    """
    Loads the instructions based on graphics object and current set instruction in graphics
    :param graphics: The graphics object which holds the instructions
    """

    # Get the current instruction and display it on the screen
    graphics.get_instruction().draw()
    graphics.refresh()

    # Keep displaying the instructions until the user presses the key to continue or the key to exit.
    while True:
        time.sleep(1)  # Reduces amount of resources used
        if event.getKeys(keyList=Constants.ESCAPE_KEYS):
            core.quit()
        elif event.getKeys(keyList=Constants.SPACE_KEYS):
            return
