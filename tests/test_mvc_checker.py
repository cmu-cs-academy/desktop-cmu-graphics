from contextlib import contextmanager

CMU_GRAPHICS_DEBUG = True

from cmu_graphics import cmu_graphics as cg
from cmu_graphics.mvc_checker import appHash, deepHash


@contextmanager
def assertRaises(exceptionType):
    try:
        yield
    except exceptionType:
        return
    raise AssertionError(f'Expected {exceptionType.__name__} to be raised')


class Bag:
    pass


# Hashing the same object twice gives the same result
obj = {'a': [1, 2, {3, 4}], 'b': (5, 6)}
assert deepHash(obj, set()) == deepHash(obj, set())

# Appending to a list changes its hash
items = [1, 2, 3]
before = deepHash(items, set())
items.append(4)
assert before != deepHash(items, set())

# Changing a dict value (not just a key) changes its hash
scores = {'score': 1}
before = deepHash(scores, set())
scores['score'] = 2
assert before != deepHash(scores, set())

# A self-referential object doesn't cause infinite recursion
cyclic = Bag()
cyclic.self = cyclic
deepHash(cyclic, set())

# Mutating a container stored as an app attribute changes appHash
wrapper = Bag()
wrapper.items = [1, 2, 3]
before = appHash(wrapper, set())
wrapper.items.append(4)
assert before != appHash(wrapper, set())

app = cg.app
app._app._isMvc = True


def simulateRedrawAll(fn):
    # callUserFn swallows exceptions raised inside redrawAll and can os._exit()
    # the process if the app isn't running, so this runs fn as redrawAll's body
    # would run without going through callUserFn, letting a raised MvcException
    # reach assertRaises normally.
    app._app.inRedrawAll = True
    try:
        fn(app)
    finally:
        app._app.inRedrawAll = False


def assignValue(app):
    app.value = 2


def disableChecker(app):
    app.disableMvcChecker = True


# A redrawAll that doesn't touch the model doesn't raise
app.value = 1
redrawAll = lambda app: None
app._app.redrawAllWrapper()

# Directly assigning an app attribute during redrawAll still raises immediately
with assertRaises(cg.MvcException):
    simulateRedrawAll(assignValue)

# Mutating a container in place during redrawAll is now caught by the hash check
app.items = [1, 2, 3]
redrawAll = lambda app: app.items.append(4)
with assertRaises(cg.MvcException):
    app._app.redrawAllWrapper()

app.disableMvcChecker = True

# Disabling the checker suppresses the hash-based check
app.items = [1, 2, 3]
redrawAll = lambda app: app.items.append(4)
app._app.redrawAllWrapper()

# Disabling the checker also suppresses the direct setattr trap
simulateRedrawAll(assignValue)

app.disableMvcChecker = False

# disableMvcChecker itself can never be toggled from inside redrawAll
with assertRaises(cg.MvcException):
    simulateRedrawAll(disableChecker)

# Setting disableMvcChecker to a non-bool is rejected
with assertRaises(Exception):
    app.disableMvcChecker = 'yes'

print('All MVC checker tests passed')
