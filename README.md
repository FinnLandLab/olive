# olives 

## Launch Experiment

1. Install Psychopy: http://www.psychopy.org
2. Launch Main.py (located in Olives directory) using a version of Python with Psychopy installed. (Psychopy comes with python with all the required libraries already installed)

## General Information

- Number of triplet orderings:                                  45
- Number of participants:                                       100
- Number of training trials (excluding Square trials):          405
- Number of Test trials (2 triplets = 1 trial):					33
- Training block duration (minutes):                            5
- Testing block duration (minutes):                             3
- Probability of Square during training block:                  10%
- Maxium probability for dot/colour match (training):           60%
- Maxium probability for correct stim being on one side (test): 75%
- Dot triplets:
	- [1, 8, 6]
	- [9, 2, 4]
	- [5, 7, 3]
- Colour triplets:
	- [Blue, Red, Green]
	- [Yellow, LightPink, Brown]
	- [Purple, Orange, Grey]

## Files & Directories

- Olives: Holds experiment files
	- Constants.py: Constant values for experiment
	- DataHandlers.py: Handlers used for trial sequencing and data storage
	- Graphics.py: Graphics objects
	- Instructions.py: Loads the given instruction
	- Main.py: Main experiment file that gets launched
	- Practice.py: Practice block
	- Test.py: Test block
	- Training.py: Training block
	- __init__.py: Required to make Python treat the directories as containing packages (DO NOT DELETE)
	
- Participants: Holds participant files (Test, Training, Test probability, Training probability)
	- [Folders labeled 100 to 200]
		- participant_#_probability.csv: Overall probability of given dot being matched with a given colour
		- participant_#_test.csv: Participant file for test block
		- participant_#_test_probability.csv: Overall count of correct stim being on left and right
		- participant_#_training.csv: Participant files for training block
		
- Script:
	- participant_test_generator.py: Generates participant test files [100 - 200]
	- participant_training_generator.py: Generates participant training files [100 - 200]
	- trip_prob.py: Generates the participant training and test probability files [100 - 200]
	
- test_items.csv: List of all possible test items for test block. For Colour and Dot tests, the left stim is the correct stim. For dual test, the left stim is always the colour word. (Used by participant_test_generator.py)

## Participant File Generation Process

- Participant Training Files (participant_training_generator.py):
	1. Generate a random ordering of the dots and colours (separately) repeated 45 times where no triplet in the random ordering can be adjacent to itself.
	2. Dots and colours ordering are converted into 2 columns and concatenated to make a 2 column table. (Dot column is offset by 1 row - First row: only colour column has value, last row: only dot column has value)
	3. Insert an additional empty row (Row and Colour columns have empty values) for every row with a probability of 10%. This represents the square stim.
	
- Participant Test Files (participant_training_generator.py):
	1. Select 2 rows at random without replacement from the test_items.csv file for every comparsion column value. (Last row gets removed since comparsion column with value 17 has 2 identical values which both get selected. Last row was duplicate since there is an odd number of 'dual' tests)
	2. For every row: flip every left and right stim with a probability of 50%
	3. Shuffle the orderings of all the Colour and Dot trials. The ordering for dual is untouched and always after all the Colour and Dot trials.
	
- trip_prob.py:
	- Participant Training probability:
		- For every participant: Create training probability file with probability of each colour getting matched with each dot. If the probability of any given colour/dot exceeds 60%, recreate the participant training file for that given participant.
		
	- Participant Test probability:
		- For every participant: Create test probability file with count of the correct stim being on the left and count of the correct stim being on the right. If the probability for one given side exceeds 75%, recreate the participant test file for that given participant.
