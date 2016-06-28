from psychopy import event, core
import Constants


def display_training(data_handlers, graphics):
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

        response = ""
        response_time = ""
        response_timer.reset()

        # Check if the dot and colour column are empty.
        # If both are empty, then a Square will be drawn instead of circle/dots
        dot_cols_empty = str(row[Constants.DOT_COL]) == 'nan'
        colour_cols_empty = str(row[Constants.COLOUR_COL]) == 'nan'

        # Set the colours for the circle.
        graphics.set_colour(Constants.VIS_CIRCLE, row[Constants.COLOUR_COL])
        graphics.set_line_colour(Constants.VIS_CIRCLE, row[Constants.COLOUR_COL])

        # Draw the appropriate shape based on the values of the rows for dots and colours.
        if not dot_cols_empty:
            graphics.set_pos(Constants.VIS_DOT, Constants.DOT_CORD[row[Constants.DOT_COL]])
        if dot_cols_empty and colour_cols_empty:
            # Square shape should appear
            graphics.draw(Constants.VIS_SQUARE)
        elif dot_cols_empty:
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
            elif not response and event.getKeys(keyList=Constants.CIRCLE_KEYS):
                response = Constants.CIRCLE_KEY
                response_time = response_timer.getTime()
            elif not response and event.getKeys(keyList=Constants.SQUARE_KEYS):
                response = Constants.SQUARE_KEY
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
