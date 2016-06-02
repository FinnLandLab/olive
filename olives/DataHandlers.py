from psychopy import data, core, gui
import Constants

# Prompt for participant number
expName = 'olives'
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
if not dlg.OK:
    core.quit()  # user pressed cancel

filename = '%s/%s_%s' % (Constants.DATA_PATH, expInfo['participant'], expInfo['date'])
info = {'date': expInfo['date']}

thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=info, runtimeInfo=None,
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)

# Get participant file
filename = Constants.PARTICIPANT_FILE_PATH % expInfo['participant']
table = data.TrialHandler(nReps=1, method='sequential',
                          extraInfo=None, trialList=data.importConditions(filename),
                          seed=None, name='dots_and_colours')

# Add participant file to experiment
thisExp.addLoop(table)
