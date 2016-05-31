from psychopy import visual
import Constants

# Screen window
win = visual.Window(size=Constants.WIN_SIZE, fullscr=Constants.WIN_FULL_SCREEN, screen=0, allowGUI=False,
                    allowStencil=False, monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb', blendMode='avg',
                    useFBO=True)

circle_visual = visual.Circle(win, pos=Constants.CENTER_CORD, radius=Constants.CIRCLE_RADIUS,
                              edges=Constants.CIRCLE_EDGE, units='deg')
dot_circle_visual = visual.Circle(win, pos=Constants.CENTER_CORD, radius=Constants.DOT_RADIUS, edges=Constants.DOT_EDGE,
                                  units='deg', fillColor=Constants.DOT_FILL_COL, lineColor=Constants.DOT_LINE_COL)
square_visual = visual.Rect(win, pos=Constants.CENTER_CORD, width=Constants.SQUARE_WIDTH,
                            height=Constants.SQUARE_HEIGHT, lineColor=Constants.SQUARE_LINE_COL)
