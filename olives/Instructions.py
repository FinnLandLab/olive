from Graphics import win
from psychopy import event, core
import time
import Constants


def load_instructions(instructions):
    instructions.draw()
    win.flip()
    while True:
        time.sleep(1)  # Reduces amount of resources used
        if event.getKeys(keyList=Constants.ESCAPE_KEYS):
            core.quit()
        elif event.getKeys(keyList=Constants.SPACE_KEYS):
            return


if __name__ == '__main__':
    pass
