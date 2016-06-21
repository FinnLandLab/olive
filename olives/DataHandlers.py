from psychopy import data, core, gui
import Constants


class DataHandlers:
    def __init__(self):
        self._expName = 'olives'
        self._expInfo = {'participant': '', 'session': '001'}
        self._dlg = gui.DlgFromDict(dictionary=self._expInfo, title=self._expName)
        self._expInfo['date'] = data.getDateStr()  # add a simple timestamp
        self._expInfo['expName'] = self._expName
        self._block = None

        if not self._dlg.OK:
            core.quit()  # user pressed cancel

        self._participant_filename = '%s/%s_%s' % (
            Constants.DATA_PATH, self._expInfo['participant'], self._expInfo['date'])

        self._participant_test_filename = '%s/%s_test_%s' % (
            Constants.DATA_PATH, self._expInfo['participant'], self._expInfo['date'])

        self._test_filename = Constants.PARTICIPANT_TEST_FILE_PATH % (
            int(self._expInfo['participant']), int(self._expInfo['participant']))

        self._training_filename = Constants.PARTICIPANT_FILE_PATH % (
            int(self._expInfo['participant']), int(self._expInfo['participant']))

        self._info = {'date': self._expInfo['date']}

        self._thisExp = None

        self._participant_table = data.TrialHandler(nReps=1, method='sequential',
                                                    extraInfo=None,
                                                    trialList=data.importConditions(self._training_filename),
                                                    seed=None, name='')

        self._test_table = data.TrialHandler(nReps=1, method='sequential',
                                             extraInfo=None, trialList=data.importConditions(self._test_filename),
                                             seed=None, name='')

        self._data_file_names = {'PRACTICE': None, 'TRAINING': self._participant_filename,
                                 'TEST': self._participant_test_filename}

        self._data_tables = {'PRACTICE': None, 'TRAINING': self._participant_table, 'TEST': self._test_table}

    def set_exp_handler(self, block):
        if block not in Constants.BLOCKS:
            raise ValueError('Wrong block type passed in. Make sure block type is a string in all caps')

        self._block = block

        self._thisExp = data.ExperimentHandler(name=self._expName, version='',
                                               extraInfo=self._info, runtimeInfo=None,
                                               savePickle=True, saveWideText=True,
                                               dataFileName=self._data_file_names[block])

        self._thisExp.addLoop(self._data_tables[block])

    def get_current_table(self):
        return self._data_tables[self._block]

    def exp_next_row(self):
        self._thisExp.nextEntry()

    def table_add_value(self, col_name, col_value):
        self._data_tables[self._block].addData(col_name, col_value)
