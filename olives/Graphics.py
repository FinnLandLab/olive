from psychopy import visual
import Constants


def _graphics_check(graphic):
    if graphic not in Constants.GRAPHICS:
        raise ValueError('Graphics does not exist')


class Graphics:
    """
    Holds all graphics objects
    """

    def __init__(self):
        # Screen window
        self._win = visual.Window(size=Constants.WIN_SIZE, fullscr=Constants.WIN_FULL_SCREEN, screen=0, allowGUI=False,
                                  allowStencil=False, monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
                                  blendMode='avg',
                                  useFBO=True)

        # shape visuals for training and test phase
        self._circle_visual = visual.Circle(self._win, pos=Constants.CENTER_CORD, radius=Constants.CIRCLE_RADIUS,
                                            edges=Constants.SHAPE_EDGE, units='deg')

        self._dot_visual = visual.Circle(self._win, pos=Constants.CENTER_CORD, radius=Constants.DOT_RADIUS,
                                         edges=Constants.SHAPE_EDGE,
                                         units='deg', fillColor=Constants.DOT_FILL_COL,
                                         lineColor=Constants.DOT_LINE_COL)

        self._square_visual = visual.Rect(self._win, pos=Constants.CENTER_CORD, width=Constants.SQUARE_WIDTH,
                                          height=Constants.SQUARE_HEIGHT, fillColor=Constants.SQUARE_FILL_COL,
                                          lineColor=Constants.SQUARE_LINE_COL)

        # Instructions Text

        self._instruction = visual.TextStim(win=self._win, ori=0, name='instruction_screen',
                                            text="",
                                            font='Arial',
                                            pos=Constants.CENTER_CORD, height=0.15, wrapWidth=None,
                                            color='white', colorSpace='rgb', opacity=1,
                                            depth=0.0)

        # practice stim texts
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

        # Question mark for practice and test phase
        self._question_mark_visual = visual.TextStim(win=self._win, ori=0, name='training_left_stim',
                                                     text='?',
                                                     font='Arial',
                                                     pos=[0, 0], height=0.5, wrapWidth=None,
                                                     color='white', colorSpace='rgb', opacity=1,
                                                     depth=0.0)

        # Used for quick access to visual objects based on type
        self._graphics = {Constants.VIS_CIRCLE: self._circle_visual, Constants.VIS_DOT: self._dot_visual,
                          Constants.VIS_SQUARE: self._square_visual,
                          Constants.VIS_PRACTICE_LEFT_STIM: self._practice_left_stim,
                          Constants.VIS_PRACTICE_RIGHT_STIM: self._practice_right_stim,
                          Constants.VIS_QUESTION_MARK: self._question_mark_visual}

    def set_instruction(self, instruction):
        """
        Sets the instructions based on the passed in instruction phase
        :param instruction: Instruction phase (Must be one of 'INSTRUCTIONS' from Constants file.
        """
        self._instruction.text = instruction

    def get_instruction(self):
        """
        Gets the last set instruction
        :return: last instruction TextStim
        """
        return self._instruction

    def set_colour(self, graphic, colour):
        """
        Sets the colour for the given visual.
        :param graphic: String that represents the given visual. Must be value from 'GRAPHICS' in Constants file.
        :param colour: The fill colour.
        """
        _graphics_check(graphic)
        if (colour == 'LightPink' or colour == 'pink'):
            self._graphics[graphic].fillColor = 'LightBlue'
        else:
            self._graphics[graphic].fillColor = colour

    def set_line_colour(self, graphic, colour):
        """
        Sets the line colour for the given visual.
        :param graphic: String that represents the given visual. Must be value from 'GRAPHICS' in Constants file.
        :param colour: The line colour.
        """
        if (colour == 'LightPink' or colour == 'pink'):
            self._graphics[graphic].lineColor = 'LightBlue'
        else:
            self._graphics[graphic].lineColor = colour

    def set_pos(self, graphic, pos):
        """
        Sets the position for the given visual.
        :param graphic: String that represents the given visual. Must be value from 'GRAPHICS' in Constants file.
        :param pos: position coordinates for the visual.
        """
        _graphics_check(graphic)
        self._graphics[graphic].pos = pos

    def set_text(self, graphic, text):
        """
        Sets the text for the given visual.
        :param graphic: String that represents the given visual. Must be value from 'GRAPHICS' in Constants file.
        :param text: The text value.
        """
        _graphics_check(graphic)
        self._graphics[graphic].setText(text)

    def draw(self, graphic):
        """
        Draws the given graphic to the screen.
        :param graphic: String that represents the given visual. Must be value from 'GRAPHICS' in Constants file.
        """
        _graphics_check(graphic)
        self._graphics[graphic].draw()

    def refresh(self):
        """
        Refresh the window. Anything drawn since the last time the screen was refreshed will be displayed.
        """
        self._win.flip()
