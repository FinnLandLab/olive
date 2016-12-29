from psychopy import event, core
from Instructions import load_instructions
import Constants


def display_rt(data_handlers, graphics):
    """
    Display the training phase
    :param data_handlers: DataHandler object used for reading from participant file and writing to output file.
    :param graphics: graphics object which holds all visuals.
    """

    # Timers for trial
    routine_timer = core.CountdownTimer()
    response_timer = core.Clock()

    # Go through every row for the training participant file
    for row in data_handlers.get_current_table():

        # Check if the dot and colour column are empty.
        # If both are empty, then a Square will be drawn instead of circle/dots
        dot_cols_empty = str(row[Constants.DOT_COL]) == 'nan' or row[Constants.DOT_COL] is None
        colour_cols_empty = str(row[Constants.COLOUR_COL]) == 'nan' or row[Constants.COLOUR_COL] is None

        # Displaying only colour circle indicates that it is the last trial for that stim number.
        # Display instructions for next stim number before moving on.
        if dot_cols_empty:
            if row[Constants.STIM_TYPE_OUTPUT_COL] == Constants.CIRCLE_STIM:
                instruction_text = Constants.RT_INSTRUCT_CIRCLE
                graphics.set_line_colour(Constants.VIS_CIRCLE, row[Constants.RT_STIM_OUTPUT_COL])
                graphics.set_colour(Constants.VIS_CIRCLE, row[Constants.RT_STIM_OUTPUT_COL])
                graphics.draw(Constants.VIS_CIRCLE)
            else:
                instruction_text = Constants.RT_INSTRUCT_DOT
                graphics.set_colour(Constants.VIS_CIRCLE, Constants.DOT_RT_INSTRUCT_CIRCLE_COL)
                graphics.set_line_colour(Constants.VIS_CIRCLE, Constants.DOT_RT_INSTRUCT_CIRCLE_COL)
                graphics.draw(Constants.VIS_CIRCLE)
                graphics.set_pos(Constants.VIS_DOT, Constants.DOT_CORD[int(row[Constants.RT_STIM_OUTPUT_COL])])
                graphics.draw(Constants.VIS_DOT)
            load_instructions(graphics, [instruction_text], delay=1, stim=Constants.VIS_RT_INSTRUCT)
            graphics.refresh()

        response = ""
        response_time = ""
        response_timer.reset()
        routine_timer.reset()

        # Set the colours for the circle.
        graphics.set_colour(Constants.VIS_CIRCLE, row[Constants.COLOUR_COL])
        graphics.set_line_colour(Constants.VIS_CIRCLE, row[Constants.COLOUR_COL])

        # Draw the appropriate shape based on the values of the rows for dots and colours.
        if not dot_cols_empty:
            graphics.set_pos(Constants.VIS_DOT, Constants.DOT_CORD[row[Constants.DOT_COL]])

        if dot_cols_empty:
            # Only big circle appears (colour)
            graphics.draw(Constants.VIS_CIRCLE)
        elif colour_cols_empty:
            # Only small circle appears (dot)
            graphics.draw(Constants.VIS_DOT)
        else:
            # Both small and big circles appear (colour and dot)
            graphics.draw(Constants.VIS_CIRCLE)
            graphics.draw(Constants.VIS_DOT)

        routine_timer.add(Constants.DISPLAY_VISUAL_TIME)
        graphics.refresh()
        event.clearEvents()

        # Display visuals for the given amount of time.
        while routine_timer.getTime() > 0:
            if event.getKeys(keyList=Constants.ESCAPE_KEYS):
                core.quit()
            elif event.getKeys(keyList=Constants.SKIP_KEYS):
                return
            elif not response and event.getKeys(keyList=Constants.SPACE_KEYS):
                response = Constants.CIRCLE_KEY
                response_time = response_timer.getTime()

        graphics.refresh()

        # Remove visuals for the given amount of time.
        routine_timer.add(Constants.NO_VISUAL_TIME)
        while routine_timer.getTime() > 0:
            if event.getKeys(keyList=Constants.ESCAPE_KEYS):
                core.quit()

        # Tell exp handler that the row/trial is finished
        data_handlers.table_add_value(Constants.DATA_OUTPUT_COL, response)
        data_handlers.table_add_value(Constants.DATA_OUTPUT_RESP_COL, response_time)

        # Tell exp handler that the row/trial is finished
        data_handlers.exp_next_row()


if __name__ == '__main__':
    from Instructions import load_instructions
    import Graphics
    import DataHandlers

    # Create handlers and graphics
    data_handlers = DataHandlers.DataHandlers()
    graphics = Graphics.Graphics()

    # TRAINING PHASE
    data_handlers.set_exp_handler(Constants.PHASE_REACTION_TIME)
    display_rt(data_handlers, graphics)

    core.quit()
