from psychopy import event, core
from Graphics import *
import Constants
import time


def display_test(data_handler):
    left = [['stim1_dots1', 'stim1_dots2', 'stim1_dots3'], ['stim1_color1', 'stim1_color2', 'stim1_color3']]
    right = [['stim2_dots1', 'stim2_dots2', 'stim2_dots3'], ['stim2_color1', 'stim2_color2', 'stim2_color3']]

    test_stim = [left, right]
    test_stim_pos = [[Constants.TEST_LEFT_DOT_CORD, [-Constants.TEST_STIM_SHIFT, 0]],
                     [Constants.TEST_RIGHT_DOT_CORD, [Constants.TEST_STIM_SHIFT, 0]]]
    test_dict = {'colour': 1, 'dot': 0}

    routine_timer = core.CountdownTimer()

    for row in data_handler:  # 2 practices
        for i in range(2):  # Left stim then right stim
            for stim in range(3):  # Go through each triplet
                routine_timer.reset()
                routine_timer.add(Constants.DISPLAY_VISUAL_TIME)

                circle_visual.fillColor = row[test_stim[i][test_dict['colour']][stim]]
                circle_visual.lineColor = row[test_stim[i][test_dict['colour']][stim]]
                dot_circle_visual.pos = test_stim_pos[i][test_dict['dot']][row[test_stim[i][test_dict['dot']][stim]]]
                circle_visual.pos = test_stim_pos[i][test_dict['colour']]

                circle_visual.draw()
                dot_circle_visual.draw()

                win.flip()
                while routine_timer.getTime() > 0:
                    if event.getKeys(keyList=Constants.ESCAPE_KEYS):
                        core.quit()
                    elif event.getKeys(keyList=Constants.SKIP_KEYS):
                        return

                win.flip()
                # Remove visuals
                routine_timer.add(Constants.NO_VISUAL_TIME)
                while routine_timer.getTime() > 0:
                    if event.getKeys(keyList=Constants.ESCAPE_KEYS):
                        core.quit()
                    elif event.getKeys(keyList=Constants.SKIP_KEYS):
                        return

        question_mark_visual.draw()
        win.flip()
        event.clearEvents()
        while True:
            if event.getKeys(keyList=Constants.ESCAPE_KEYS):
                core.quit()
            elif event.getKeys(keyList=Constants.PRACTICE_RESP_KEYS):
                break
        win.flip()
        time.sleep(1)


if __name__ == '__main__':
    from DataHandlers import *

    display_test(test_table)