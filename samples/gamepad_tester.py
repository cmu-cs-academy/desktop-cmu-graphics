from cmu_graphics import *
import samples.joystick

def onJoyPress(button, joystick):
    """Tells you which button was pushed on which joystick"""
    print(f"Joystick {joystick} button pressed: {button}")
    pass

def onJoyRelease(button, joystick):
    """Tells you when a button is released on which joystick"""
    print(f"Joystick {joystick} button released: {button}")
    pass

def onJoyButtonHold(buttons, joystick):
    """Is called every step if a button is being held"""
    print(f"Joystick {joystick} buttons being held: {buttons}")
    pass

def onJoyAxis(value, axis, joystick):
    """Is called every step if a joystick analog stick is activated
    axis tells you which analog axis from the joystick is returning the value
    This is very noisy, so you will need to do some smoothing/rounding with it
    """
    print(f"Joystick {joystick} axis {axis} returning {value}")
    pass

def onDigitalJoyAxis(results, joystick):
    """Is called every step that a joystick analog stick is activated, but this
    rounds the values to the nearest 0, 1, or -1.  This is useful when you just
    want to know if the stick is being pushed to its extreme.

    results contains a list of tuples of (axis, value) pairs.

    This operates similarly to oneJoyButtonHold in that a specific axis,value
    combination is only in the results list if it is currently being held.
    """
    print(f"Joystick {joystick} axis being held: {results}")
    pass

cmu_graphics.run()