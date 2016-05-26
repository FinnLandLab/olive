import os
import sys

from psychopy import visual, core, event, gui, data

import constants

#########################################################################
###                   Prompt for participant number                   ###
#########################################################################
expName = 'olive'
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
routineTimer = core.CountdownTimer()
if not dlg.OK:
    core.quit()  # user pressed cancel

# Screen window
win = visual.Window(size=(800, 500), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
                    monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
                    blendMode='avg', useFBO=True,
                    )

filename = '%s/%s_%s' % (constants.DATA_PATH, expInfo['participant'], expInfo['date'])

info = {'date': expInfo['date']}
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=info, runtimeInfo=None,
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)

filename = constants.PARTICIPANT_FILE_PATH % expInfo['participant']
table = data.TrialHandler(nReps=1, method='sequential',
                          extraInfo=None, trialList=data.importConditions(filename),
                          seed=None, name='dots_and_colours')
thisExp.addLoop(table)  # add the loop to the experiment

circle_visual = visual.Circle(win, pos=[0, 0], radius=5, edges=64, units='deg', fillColor='red', lineColor='red')
dot_circle_visual = visual.Circle(win, pos=[0, 0], radius=1, edges=64, units='deg', fillColor='black',
                                  lineColor='black')

square_visual = visual.Rect(win, pos=[0, 0], width=0.5, height=1, lineColor='black')
routineTimer.add(1)
for row in table:
    print row

    dot_cols_empty = str(row[constants.DOT_COL]) == 'nan'
    colour_cols_empty = str(row[constants.COLOUR_COL]) == 'nan'

    circle_visual.fillColor = row[constants.COLOUR_COL]
    circle_visual.lineColor = row[constants.COLOUR_COL]

    if not dot_cols_empty:
        dot_circle_visual.pos = constants.DOT_CORD[row[constants.DOT_COL]]

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

    routineTimer.add(constants.STIM_DELAY)
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
