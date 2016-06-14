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

participant_filename = '%s/%s_%s' % (Constants.DATA_PATH, expInfo['participant'], expInfo['date'])
dots_test_filename = Constants.DOTS_TEST_FILE_PATH

info = {'date': expInfo['date']}

thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=info, runtimeInfo=None,
                                 savePickle=True, saveWideText=True,
                                 dataFileName=participant_filename)

# Get participant file
participant_filename = Constants.PARTICIPANT_FILE_PATH % expInfo['participant']
participant_table = data.TrialHandler(nReps=1, method='sequential',
                                      extraInfo=None, trialList=data.importConditions(participant_filename),
                                      seed=None, name='')

dots_test_table = data.TrialHandler(nReps=1, method='sequential',
                                    extraInfo=None, trialList=data.importConditions(dots_test_filename),
                                    seed=None, name='')

# Add participant file to experiment
thisExp.addLoop(participant_table)
