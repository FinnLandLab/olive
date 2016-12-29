from psychopy import data, core, gui
import Constants
import os


class DataHandlers:
    """
    DataHandlers are used for trial sequencing and data storage.
    """

    def __init__(self):

        # Get experiment information and prompt user for participant/session number.
        self._expName = 'olives'
        self._expInfo = {'participant': '', 'session': '001'}
        self._dlg = gui.DlgFromDict(dictionary=self._expInfo, title=self._expName)
        self._expInfo['date'] = data.getDateStr()  # add a simple timestamp
        self._expInfo['expName'] = self._expName
        self._block = None

        # Participant did not provide a number
        if not self._dlg.OK:
            core.quit()  # user pressed cancel

        # Create participant folder inside data path if one doesn't already exist
        if not os.path.exists('%s/%s' % (Constants.DATA_PATH, self._expInfo['participant'])):
            os.makedirs('%s/%s' % (Constants.DATA_PATH, self._expInfo['participant']))

        # File names for participants training/test files and output file names
        self._participant_training_filename = '%s/%s/%s_training_%s' % (
            Constants.DATA_PATH, self._expInfo['participant'], self._expInfo['participant'], self._expInfo['date'])

        self._participant_test_filename = '%s/%s/%s_test_%s' % (
            Constants.DATA_PATH, self._expInfo['participant'], self._expInfo['participant'], self._expInfo['date'])

        self._participant_rt_filename = '%s/%s/%s_rt_%s' % (
            Constants.DATA_PATH, self._expInfo['participant'], self._expInfo['participant'], self._expInfo['date'])

        self._test_filename = Constants.PARTICIPANT_TEST_FILE_PATH % (
            int(self._expInfo['participant']), int(self._expInfo['participant']))

        self._training_filename = Constants.PARTICIPANT_TRAINING_FILE_PATH % (
            int(self._expInfo['participant']), int(self._expInfo['participant']))

        self._rt_filename = Constants.PARTICIPANT_REACTION_TIME_FILE_PATH % (
            int(self._expInfo['participant']), int(self._expInfo['participant']))

        # Additional information which will get included in the output files.
        self._info = {'date': self._expInfo['date']}

        # Will hold ExperimentHandler, which is used for output file generation
        self._thisExp = None

        # TrailHandlers will hold the participant data. You can iterate through them to go through each row of the
        #  participant file
        self._training_table = data.TrialHandler(nReps=1, method='sequential',
                                                 extraInfo=None,
                                                 trialList=data.importConditions(self._training_filename),
                                                 seed=None, name='')

        self._test_table = data.TrialHandler(nReps=1, method='sequential',
                                             extraInfo=None, trialList=data.importConditions(self._test_filename),
                                             seed=None, name='')

        self._rt_table = data.TrialHandler(nReps=1, method='sequential',
                                           extraInfo=None, trialList=data.importConditions(self._rt_filename),
                                           seed=None, name='')

        # Used for quick access to needed variables based on current phase
        self._data_file_names = {Constants.PHASE_PRACTICE: None,
                                 Constants.PHASE_TRAINING: self._participant_training_filename,
                                 Constants.PHASE_TEST: self._participant_test_filename,
                                 Constants.PHASE_REACTION_TIME: self._participant_rt_filename}

        self._data_tables = {Constants.PHASE_PRACTICE: None, Constants.PHASE_TRAINING: self._training_table,
                             Constants.PHASE_TEST: self._test_table, Constants.PHASE_REACTION_TIME: self._rt_table}

    def set_exp_handler(self, block):
        """
        Set the exp handler for the current phase. Each new exp handler will generate a new output file.
        :param block: The current block. Values should be based on 'BLOCKS' from the Constants file.
        """
        if block not in Constants.BLOCKS:
            raise ValueError('Wrong block type passed in. Make sure block type is a string in all caps')

        # set the current block
        self._block = block

        # Set the exp handler based on the current phase.
        # All values are same for every phase with the exception of the output data file name
        self._thisExp = data.ExperimentHandler(name=self._expName, version='',
                                               extraInfo=self._info, runtimeInfo=None,
                                               savePickle=True, saveWideText=True,
                                               dataFileName=self._data_file_names[block])

        # Add the participant file to the exp handler.
        # This will add all the columns from the participant file to the output file.
        self._thisExp.addLoop(self._data_tables[block])

    def get_current_table(self):
        """
        Gets the current table based on the current phase
        :return: the current trial handler
        """
        return self._data_tables[self._block]

    def exp_next_row(self):
        """
        Tells the exp handler that the current trial is finish and to start the next trial.
        This function should get called at the end of each trial.
        """
        self._thisExp.nextEntry()

    def table_add_value(self, col_name, col_value):
        """
        Add a row to the exp output file. If the column does not exist, it will get created.
        :param col_name: The column name the row should be under.
        :param col_value: The value of the data that is being added.
        """
        self._data_tables[self._block].addData(col_name, col_value)
