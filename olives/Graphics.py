from psychopy import visual
import Constants


class Graphics:
    def __init__(self):
        # Screen window
        self._win = visual.Window(size=Constants.WIN_SIZE, fullscr=Constants.WIN_FULL_SCREEN, screen=0, allowGUI=False,
                                  allowStencil=False, monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
                                  blendMode='avg',
                                  useFBO=True)

        self._circle_visual = visual.Circle(self._win, pos=Constants.CENTER_CORD, radius=Constants.CIRCLE_RADIUS,
                                            edges=Constants.SHAPE_EDGE, units='deg')

        self._dot_circle_visual = visual.Circle(self._win, pos=Constants.CENTER_CORD, radius=Constants.DOT_RADIUS,
                                                edges=Constants.SHAPE_EDGE,
                                                units='deg', fillColor=Constants.DOT_FILL_COL,
                                                lineColor=Constants.DOT_LINE_COL)

        self._square_visual = visual.Rect(self._win, pos=Constants.CENTER_CORD, width=Constants.SQUARE_WIDTH,
                                          height=Constants.SQUARE_HEIGHT, fillColor=Constants.SQUARE_FILL_COL,
                                          lineColor=Constants.SQUARE_LINE_COL)

        # Instructions Text
        self._practice_instructions = visual.TextStim(win=self._win, ori=0, name='practice_instruction_screen',
                                                      text='PRACTICE INSTRUCTIONS GO HERE',
                                                      font='Arial',
                                                      pos=Constants.CENTER_CORD, height=0.1, wrapWidth=None,
                                                      color='white', colorSpace='rgb', opacity=1,
                                                      depth=0.0)

        self._main_instructions = visual.TextStim(win=self._win, ori=0, name='instruction_screen',
                                                  text='MAIN INSTRUCTIONS GO HERE',
                                                  font='Arial',
                                                  pos=Constants.CENTER_CORD, height=0.1, wrapWidth=None,
                                                  color='white', colorSpace='rgb', opacity=1,
                                                  depth=0.0)

        self._test_instructions = visual.TextStim(win=self._win, ori=0, name='test_instruction_screen',
                                                  text='TEST INSTRUCTIONS GO HERE',
                                                  font='Arial',
                                                  pos=Constants.CENTER_CORD, height=0.1, wrapWidth=None,
                                                  color='white', colorSpace='rgb', opacity=1,
                                                  depth=0.0)

        self._practice_left_stim = visual.TextStim(win=self._win, ori=0, name='training_left_stim',
                                                   text='A',
                                                   font='Arial',
                                                   pos=[-0.5, 0], height=0.5, wrapWidth=None,
                                                   color='white', colorSpace='rgb', opacity=1,
                                                   depth=0.0)

        self._practice_right_stim = visual.TextStim(win=self._win, ori=0, name='training_left_stim',
                                                    text='B',
                                                    font='Arial',
                                                    pos=[0.5, 0], height=0.5, wrapWidth=None,
                                                    color='white', colorSpace='rgb', opacity=1,
                                                    depth=0.0)

        self._question_mark_visual = visual.TextStim(win=self._win, ori=0, name='training_left_stim',
                                                     text='?',
                                                     font='Arial',
                                                     pos=[0, 0], height=0.5, wrapWidth=None,
                                                     color='white', colorSpace='rgb', opacity=1,
                                                     depth=0.0)

        self._instructions = {'PRACTICE': self._practice_instructions, 'TRAINING': self._main_instructions,
                              'TEST': self._test_instructions}

        self._instruction = None

        self._graphics = {'CIRCLE': self._circle_visual, 'DOT': self._dot_circle_visual, 'SQUARE': self._square_visual,
                          "PRACTICE_LEFT_STIM": self._practice_left_stim,
                          "PRACTICE_RIGHT_STIM": self._practice_right_stim, 'QUESTION_MARK': self._question_mark_visual}

    def set_instruction(self, instruction):
        if instruction not in Constants.INSTRUCTIONS:
            raise ValueError('Wrong instruction type passed in. Make sure instruction type is a string in all caps')

        self._instruction = self._instructions[instruction]

    def get_instruction(self):
        return self._instruction

    def set_colour(self, graphic, colour):
        self._graphics[graphic].fillColor = colour

    def set_line_colour(self, graphic, colour):
        self._graphics[graphic].lineColor = colour

    def set_pos(self, graphic, pos):
        self._graphics[graphic].pos = pos

    def set_text(self, graphic, text):
        self._graphics[graphic].setText(text)

    def draw(self, graphic):
        self._graphics[graphic].draw()

    def refresh(self):
        self._win.flip()
