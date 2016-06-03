from Instructions import *
from Graphics import *


def display_practice():
    left = [['A', 'B', 'C'], ['Z', 'X', 'Y']]
    right = [['B', 'C', 'A'], ['X', 'Y', 'Z']]

    # num of trials in left must be equal to num of trials in right.
    if len(left) != len(right):
        return

    num_of_practice_trials = 2
    training_stim_val = [training_left_stim, training_right_stim]
    training_stim = [left, right]
    routine_timer = core.CountdownTimer()

    load_instructions(practice_instructions)

    for trial in range(num_of_practice_trials):  # 2 practices
        for i in range(2):  # Left stim then right stim
            for stim in range(3):  # Go through each triplet
                routine_timer.reset()
                routine_timer.add(Constants.DISPLAY_VISUAL_TIME)
                training_stim_val[i].setText(training_stim[i][trial][stim])
                training_stim_val[i].draw()
                win.flip()
                while routine_timer.getTime() > 0:
                    if event.getKeys(keyList=Constants.ESCAPE_KEYS):
                        core.quit()

                win.flip()
                # Remove visuals
                routine_timer.add(Constants.NO_VISUAL_TIME)
                while routine_timer.getTime() > 0:
                    if event.getKeys(keyList=Constants.ESCAPE_KEYS):
                        core.quit()

        question_mark_visual.draw()
        win.flip()
        event.clearEvents()
        while True:
            if event.getKeys(keyList=Constants.ESCAPE_KEYS):
                core.quit()
            elif event.getKeys(keyList=Constants.PRACTICE_RESP_KEYS):
                break
        win.flip()
        time.sleep(Constants.NO_VISUAL_TIME)


if __name__ == '__main__':
    display_practice()
