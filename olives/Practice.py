from psychopy import event, core
import Constants
import time


def display_practice(graphics):
    """
    Display the practice phase
    :param graphics: graphics object which holds all visuals.
    """

    # The two trials for left and right stim
    left = [['A', 'B', 'C'], ['Z', 'X', 'Y']]
    right = [['B', 'C', 'A'], ['X', 'Y', 'Z']]

    # num of trials in left must be equal to num of trials in right.
    if len(left) != len(right):
        return

    num_of_practice_trials = 2
    practice_stim_val = ['PRACTICE_LEFT_STIM', 'PRACTICE_RIGHT_STIM']
    practice_stim = [left, right]
    routine_timer = core.CountdownTimer()

    for trial in range(num_of_practice_trials):  # 2 practices
        for i in range(2):  # Left stim then right stim
            for stim in range(3):  # Go through each triplet

                # Set timer for each stim
                routine_timer.reset()
                routine_timer.add(Constants.DISPLAY_VISUAL_TIME)

                # Set and display current stim.
                graphics.set_text(practice_stim_val[i], practice_stim[i][trial][stim])
                graphics.draw(practice_stim_val[i])
                graphics.refresh()

                # Display for the given length
                while routine_timer.getTime() > 0:
                    if event.getKeys(keyList=Constants.ESCAPE_KEYS):
                        core.quit()
                    elif event.getKeys(keyList=Constants.SKIP_KEYS):
                        return

                graphics.refresh()
                routine_timer.add(Constants.NO_VISUAL_TIME)

                # Remove visuals for the given length (transition from one stim to another)
                while routine_timer.getTime() > 0:
                    if event.getKeys(keyList=Constants.ESCAPE_KEYS):
                        core.quit()
                    elif event.getKeys(keyList=Constants.SKIP_KEYS):
                        return

        # After stims have been displayed, draw a question mark and wait for response.
        graphics.draw('QUESTION_MARK')
        graphics.refresh()
        event.clearEvents()

        # Wait until response given or escape key is pressed.
        while True:
            if event.getKeys(keyList=Constants.ESCAPE_KEYS):
                core.quit()
            elif event.getKeys(keyList=Constants.PRACTICE_RESP_KEYS):
                break

        # Clear screen and wait for the given length before starting next trial.
        graphics.refresh()
        time.sleep(Constants.NO_VISUAL_TIME)
