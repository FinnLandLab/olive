from DataHandlers import *
from Graphics import *
from psychopy import core, event

routineTimer = core.CountdownTimer()

routineTimer.add(1)
for row in table:
    print row

    dot_cols_empty = str(row[Constants.DOT_COL]) == 'nan'
    colour_cols_empty = str(row[Constants.COLOUR_COL]) == 'nan'

    circle_visual.fillColor = row[Constants.COLOUR_COL]
    circle_visual.lineColor = row[Constants.COLOUR_COL]

    if not dot_cols_empty:
        dot_circle_visual.pos = Constants.DOT_CORD[row[Constants.DOT_COL]]

    if dot_cols_empty and colour_cols_empty:
        # Square shape should appear
        print 1
        square_visual.draw()
    elif dot_cols_empty:
        # Only big circle appears (colour)
        print 2
        circle_visual.draw()
    elif colour_cols_empty:
        # Only small circle appears (dot)
        print 3
        dot_circle_visual.draw()
    else:
        # Both small and big circles appear (colour and dot)
        print 4
        circle_visual.draw()
        dot_circle_visual.draw()

    routineTimer.add(Constants.STIM_DELAY)
    win.flip()
    while routineTimer.getTime() > 0:
        if event.getKeys(keyList=['esc', 'escape']):
            core.quit()

    routineTimer.add(0.2)
    win.flip()
    while routineTimer.getTime() > 0:
        if event.getKeys(keyList=['esc', 'escape']):
            core.quit()

    thisExp.nextEntry()

core.quit()
