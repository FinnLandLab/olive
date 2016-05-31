from psychopy import visual

# Screen window
win = visual.Window(size=(800, 500), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
                    monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
                    blendMode='avg', useFBO=True,
                    )

circle_visual = visual.Circle(win, pos=[0, 0], radius=5, edges=64, units='deg', fillColor='red', lineColor='red')
dot_circle_visual = visual.Circle(win, pos=[0, 0], radius=1, edges=64, units='deg', fillColor='black',
                                  lineColor='black')
square_visual = visual.Rect(win, pos=[0, 0], width=0.5, height=1, lineColor='black')
