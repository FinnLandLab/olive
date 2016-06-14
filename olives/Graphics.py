from psychopy import visual
import Constants

# Screen window
win = visual.Window(size=Constants.WIN_SIZE, fullscr=Constants.WIN_FULL_SCREEN, screen=0, allowGUI=False,
                    allowStencil=False, monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb', blendMode='avg',
                    useFBO=True)

circle_visual = visual.Circle(win, pos=Constants.CENTER_CORD, radius=Constants.CIRCLE_RADIUS,
                              edges=Constants.SHAPE_EDGE, units='deg')
dot_circle_visual = visual.Circle(win, pos=Constants.CENTER_CORD, radius=Constants.DOT_RADIUS,
                                  edges=Constants.SHAPE_EDGE,
                                  units='deg', fillColor=Constants.DOT_FILL_COL, lineColor=Constants.DOT_LINE_COL)
square_visual = visual.Rect(win, pos=Constants.CENTER_CORD, width=Constants.SQUARE_WIDTH,
                            height=Constants.SQUARE_HEIGHT, fillColor=Constants.SQUARE_FILL_COL,
                            lineColor=Constants.SQUARE_LINE_COL)

# Instructions Text
practice_instructions = visual.TextStim(win=win, ori=0, name='practice_instruction_screen',
                                        text='PRACTICE INSTRUCTIONS GO HERE',
                                        font='Arial',
                                        pos=Constants.CENTER_CORD, height=0.1, wrapWidth=None,
                                        color='white', colorSpace='rgb', opacity=1,
                                        depth=0.0)

main_instructions = visual.TextStim(win=win, ori=0, name='instruction_screen',
                                    text='MAIN INSTRUCTIONS GO HERE',
                                    font='Arial',
                                    pos=Constants.CENTER_CORD, height=0.1, wrapWidth=None,
                                    color='white', colorSpace='rgb', opacity=1,
                                    depth=0.0)

test_instructions = visual.TextStim(win=win, ori=0, name='test_instruction_screen',
                                    text='TEST INSTRUCTIONS GO HERE',
                                    font='Arial',
                                    pos=Constants.CENTER_CORD, height=0.1, wrapWidth=None,
                                    color='white', colorSpace='rgb', opacity=1,
                                    depth=0.0)

training_left_stim = visual.TextStim(win=win, ori=0, name='training_left_stim',
                                     text='A',
                                     font='Arial',
                                     pos=[-0.5, 0], height=0.5, wrapWidth=None,
                                     color='white', colorSpace='rgb', opacity=1,
                                     depth=0.0)

training_right_stim = visual.TextStim(win=win, ori=0, name='training_left_stim',
                                      text='B',
                                      font='Arial',
                                      pos=[0.5, 0], height=0.5, wrapWidth=None,
                                      color='white', colorSpace='rgb', opacity=1,
                                      depth=0.0)

question_mark_visual = visual.TextStim(win=win, ori=0, name='training_left_stim',
                                       text='?',
                                       font='Arial',
                                       pos=[0, 0], height=0.5, wrapWidth=None,
                                       color='white', colorSpace='rgb', opacity=1,
                                       depth=0.0)
