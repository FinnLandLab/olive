from psychopy import event, core
import Constants


def display_training(data_handlers, graphics):
    routine_timer = core.CountdownTimer()
    response_timer = core.Clock()
    skip = False

    for row in data_handlers.get_current_table():
        response = ""
        response_time = ""

        response_timer.reset()

        dot_cols_empty = str(row[Constants.DOT_COL]) == 'nan'
        colour_cols_empty = str(row[Constants.COLOUR_COL]) == 'nan'

        graphics.set_colour('CIRCLE', row[Constants.COLOUR_COL])
        graphics.set_line_colour('CIRCLE', row[Constants.COLOUR_COL])

        if not dot_cols_empty:
            graphics.set_pos('DOT', Constants.DOT_CORD[row[Constants.DOT_COL]])

        if dot_cols_empty and colour_cols_empty:
            # Square shape should appear
            print 1
            graphics.draw('SQUARE')
        elif dot_cols_empty:
            # Only big circle appears (colour)
            print 2
            graphics.draw('CIRCLE')
        elif colour_cols_empty:
            # Only small circle appears (dot)
            print 3
            graphics.draw('DOT')
        else:
            # Both small and big circles appear (colour and dot)
            print 4
            graphics.draw('CIRCLE')
            graphics.draw('DOT')

        routine_timer.add(Constants.DISPLAY_VISUAL_TIME)
        graphics.refresh()

        # Display visuals
        while routine_timer.getTime() > 0:
            if event.getKeys(keyList=Constants.ESCAPE_KEYS):
                core.quit()
            elif event.getKeys(keyList=Constants.SKIP_KEYS):
                skip = True
            elif not response and event.getKeys(keyList=Constants.CIRCLE_KEYS):
                response = Constants.CIRCLE_KEY
                response_time = response_timer.getTime()
            elif not response and event.getKeys(keyList=Constants.SQUARE_KEYS):
                response = Constants.SQUARE_KEY
                response_time = response_timer.getTime()

        graphics.refresh()

        if skip:
            break

        # Remove visuals
        routine_timer.add(Constants.NO_VISUAL_TIME)
        while routine_timer.getTime() > 0:
            if event.getKeys(keyList=Constants.ESCAPE_KEYS):
                core.quit()

        data_handlers.table_add_value(Constants.DATA_OUTPUT_COL, response)
        data_handlers.table_add_value(Constants.DATA_OUTPUT_RESP_COL, response_time)

        data_handlers.exp_next_row()
