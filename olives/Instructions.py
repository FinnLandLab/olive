# from Graphics import win
from psychopy import event, core
import time
import Constants


def load_instructions(graphics):
    graphics.get_instruction().draw()
    graphics.refresh()
    while True:
        time.sleep(1)  # Reduces amount of resources used
        if event.getKeys(keyList=Constants.ESCAPE_KEYS):
            core.quit()
        elif event.getKeys(keyList=Constants.SPACE_KEYS):
            return
