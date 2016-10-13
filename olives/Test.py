from psychopy import event, core
import Constants
import time


def display_test(data_handlers, graphics):
    """
    Display the test phase
    :param data_handlers: DataHandler object used for reading from participant file and writing to output file.
    :param graphics: graphics object which holds all visuals.
    """

    # Timers for trial
    routine_timer = core.CountdownTimer()
    response_timer = core.Clock()

    # Holds column names for left stim and right stim
    test_stim = [Constants.TEST_LEFT_COL_ORD, Constants.TEST_RIGHT_COL_ORD]

    # Holds dot positions for left stim and right stim
    test_stim_pos = [[Constants.TEST_LEFT_DOT_CORD, [-Constants.TEST_STIM_SHIFT, 0]],
                     [Constants.TEST_RIGHT_DOT_CORD, [Constants.TEST_STIM_SHIFT, 0]]]

    # Used to get appropriate value from test_stim
    test_dict = {'colour': 1, 'dot': 0}

    # Go through every row for the test participant file
    for row in data_handlers.get_current_table():
        for i in range(2):  # Left stim then right stim
            for stim in range(3):  # Go through each triplet
                
                if row[test_stim[i][test_dict['colour']][stim]] is None or str(row[test_stim[i][test_dict['colour']][stim]]) == 'nan' or \
                    row[test_stim[i][test_dict['dot']][stim]] is None or str(row[test_stim[i][test_dict['dot']][stim]]) == 'nan':
                    continue

                # Set the colour and coordinates for circle and dots for the given stim
                graphics.set_colour(Constants.VIS_CIRCLE, row[test_stim[i][test_dict['colour']][stim]])
                graphics.set_line_colour(Constants.VIS_CIRCLE, row[test_stim[i][test_dict['colour']][stim]])
                graphics.set_pos(Constants.VIS_DOT,
                                 test_stim_pos[i][test_dict['dot']][row[test_stim[i][test_dict['dot']][stim]]])
                graphics.set_pos(Constants.VIS_CIRCLE, test_stim_pos[i][test_dict['colour']])

                # Draw the circle and dot
                graphics.draw(Constants.VIS_CIRCLE)
                graphics.draw(Constants.VIS_DOT)

                routine_timer.reset()

                # Display visuals for the given length
                routine_timer.add(Constants.DISPLAY_VISUAL_TIME)
                graphics.refresh()
                while routine_timer.getTime() > 0:
                    if event.getKeys(keyList=Constants.ESCAPE_KEYS):
                        core.quit()
                    elif event.getKeys(keyList=Constants.SKIP_KEYS):
                        return

                # Clear the screen and wait for the given length
                graphics.refresh()
                routine_timer.add(Constants.NO_VISUAL_TIME)
                while routine_timer.getTime() > 0:
                    if event.getKeys(keyList=Constants.ESCAPE_KEYS):
                        core.quit()
                    elif event.getKeys(keyList=Constants.SKIP_KEYS):
                        return

        # Draw question mark and wait for response.
        graphics.draw(Constants.VIS_QUESTION_MARK)
        graphics.refresh()

        response_timer.reset()
        event.clearEvents()
        response = ""
        response_time = ""

        # Wait until response given or escape key is pressed.
        while True:
            if event.getKeys(keyList=Constants.ESCAPE_KEYS):
                core.quit()
                break
            elif not response and event.getKeys(keyList=Constants.LEFT_STIM_KEYS):
                response = Constants.LEFT_STIM_KEY
                response_time = response_timer.getTime()
                break
            elif not response and event.getKeys(keyList=Constants.RIGHT_STIM_KEYS):
                response = Constants.RIGHT_STIM_KEY
                response_time = response_timer.getTime()
                break

        # Add the response and response time to the output file.
        data_handlers.table_add_value(Constants.DATA_OUTPUT_COL, response)
        data_handlers.table_add_value(Constants.DATA_OUTPUT_RESP_COL, response_time)
        data_handlers.table_add_value(Constants.TEST_OUTPUT_COL, Constants.TEST_STIM_RESP[response])

        # Tell exp handler that the row/trial is finished
        data_handlers.exp_next_row()

        graphics.refresh()

        # Delay before starting next trial.
        time.sleep(Constants.TEST_DELAY_BETWEEN_TRIALS)
