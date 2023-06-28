try:
    # Use this to import pygame if cmu_graphics was installed via zip file
    from cmu_graphics.libs import pygame_loader as pygame
except:
    # Use this to import pygame if we couldn't use pygame_loader
    import pygame

from cmu_graphics import almostEqual, pygameEvent, onStepEvent

_allJoyButtonsDown = dict()
_allDigitalJoyAxisDown = dict()
_lastJoyAxis = dict()
_joysticks = dict()


def handlePygameEvent(event, callUserFn, app):
    print(event)
    if event.type == pygame.JOYDEVICEADDED:
        joy = pygame.joystick.Joystick(event.device_index)
        _joysticks[joy.get_instance_id()] = joy
        _allJoyButtonsDown[joy.get_instance_id()] = set()
        _allDigitalJoyAxisDown[joy.get_instance_id()] = set()
        joy.rumble(0, 0.7, 500)  # Rumble if it can and is connected
    elif event.type == pygame.JOYDEVICEREMOVED:
        del _joysticks[event.instance_id]
        key = f"J{event.instance_id}H"
        if key in _lastJoyAxis:
            del _lastJoyAxis[key]
        del _allJoyButtonsDown[event.instance_id]
        del _allDigitalJoyAxisDown[event.instance_id]
    elif event.type == pygame.JOYBUTTONDOWN:
        handleJoyPress(str(event.button), event.instance_id, callUserFn)
    elif event.type == pygame.JOYBUTTONUP:
        handleJoyRelease(str(event.button), event.instance_id, callUserFn)
    elif event.type == pygame.JOYHATMOTION:
        handleJoyHat(event.value, event.instance_id, callUserFn)
    elif event.type == pygame.JOYAXISMOTION:
        handleDigitalJoyAxis(event.value, event.axis, event.instance_id)
        callUserFn('onJoyAxis', (event.value, event.axis, event.instance_id))


pygameEvent.connect(handlePygameEvent)


def handleOnStepEvent(callUserFn, app):
    for joystick in _allJoyButtonsDown:
        if len(_allJoyButtonsDown[joystick]) > 0:
            callUserFn('onJoyButtonHold', (list(_allJoyButtonsDown[joystick]), joystick))
    for joystick in _allDigitalJoyAxisDown:
        if len(_allDigitalJoyAxisDown[joystick]) > 0:
            callUserFn('onDigitalJoyAxis', (list(_allDigitalJoyAxisDown[joystick]), joystick))


onStepEvent.connect(handleOnStepEvent)


def handleJoyPress(button, joystick, callUserFn):
    _allJoyButtonsDown[joystick].add(button)
    callUserFn('onJoyPress', (button, joystick))


def handleJoyRelease(button, joystick, callUserFn):
    if button in _allJoyButtonsDown[joystick]: _allJoyButtonsDown[joystick].remove(button)
    callUserFn('onJoyRelease', (button, joystick))


def handleDigitalJoyAxisPress(value, axis, joystick):
    _allDigitalJoyAxisDown[joystick].add((axis, value))


def handleDigitalJoyAxisRelease(value, axis, joystick):
    if (axis, value) in _allDigitalJoyAxisDown[joystick]: _allDigitalJoyAxisDown[joystick].remove(
        (axis, value))


# Hats are just DPADs, so we'll handle them like buttons
def handleJoyHat(values, joystick, callUserFn):
    # We will index the _lastJoyAxis dict using the joystick and H for hat
    key = f"J{joystick}H"
    prev = _lastJoyAxis.get(key, (0, 0))

    # Only signal a button press if it is newly pressed.
    # You can get (0,1) followed by (1,1), meaning one of the buttons stayed pressed.
    if values[1] == 1 and prev[1] != 1:
        handleJoyPress("H0", joystick, callUserFn)
    elif values[1] == -1 and prev[1] != -1:
        handleJoyPress("H2", joystick, callUserFn)

    if values[1] == 0 and prev[1] == 1:
        handleJoyRelease("H0", joystick, callUserFn)
    elif values[1] == 0 and prev[1] == -1:
        handleJoyRelease("H2", joystick, callUserFn)

    if values[0] == 1 and prev[0] != 1:
        handleJoyPress("H1", joystick, callUserFn)
    elif values[0] == -1 and prev[0] != -1:
        handleJoyPress("H3", joystick, callUserFn)

    if values[0] == 0 and prev[0] == 1:
        handleJoyRelease("H1", joystick, callUserFn)
    elif values[0] == 0 and prev[0] == -1:
        handleJoyRelease("H3", joystick, callUserFn)

    _lastJoyAxis[key] = values


def handleDigitalJoyAxis(value, axis, joystick):
    # We are going to treat this as a digital, which many are.
    if almostEqual(value, 0, 0.5):
        value = 0
    elif almostEqual(value, 1, 0.5):
        value = 1
    elif almostEqual(value, -1, 0.5):
        value = -1
    else:
        return

    # We will index the _lastJoyAxis dict using the joystick and axis
    key = f"J{joystick}A{axis}"
    prev = _lastJoyAxis.get(key, 0)

    # Control stick was pushed in a direction
    if value != 0 and prev == 0:
        handleDigitalJoyAxisPress(value, axis, joystick)

    # Control stick was released in that direction
    if value == 0 and prev != 0:
        handleDigitalJoyAxisRelease(prev, axis, joystick)

    _lastJoyAxis[key] = value
