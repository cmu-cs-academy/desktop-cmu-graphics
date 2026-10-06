# The MVC violation checker works by comparing appHash() before and after
# redrawAll, so every change to the model has to change the hash. Each of the
# models below has hashed the same before and after a change at some point.
from cmu_graphics import appHash


def checkHashChanges(description, change):
    before = appHash()
    change()
    after = appHash()
    assert before != after, f'appHash did not change after {description}'


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def setObjectAttr(app):
    # Make sure we're looking at properties of objects, in particular the
    # keys of the object's __dict__
    app.location.x = 2


def setListItem(app):
    # 1 is already elsewhere in the model, so hashing it as "a value we have
    # seen before" hides the change
    app.grid[2] = 1


def setDictValue(app):
    # Hashing only the keys of a dict misses this
    app.scores['b'] = 3


def setNestedDictValue(app):
    # In Python, tracking already-seen objects by id alone misses this: the
    # (key, value) tuples made while hashing one dict can be freed, and their
    # ids reused for the next dict's tuples
    app.boards[1]['k'] = 3


def reorderList(app):
    # Summing the item hashes misses this
    app.order.reverse()


def growLargeNumber(app):
    # Too large to be a JS number, so this hashes to a Brython long_int
    app.big += 1


def onAppStart(app):
    app.disableMvcChecker = True
    app.disableMvcChecker = False

    app.grid = [0, 1, 0]
    app.scores = {'a': 1, 'b': 2}
    app.boards = [{'k': 1}, {'k': 2}]
    app.order = [1, 2]
    app.big = 10**20
    app.point = (3, 4)
    app.tags = {'x', 'y'}
    app.location = Point(1, 5)

    assert appHash() == appHash(), 'appHash is not stable'

    checkHashChanges('setting an attribute of an object', lambda: setObjectAttr(app))
    checkHashChanges('setting a list item', lambda: setListItem(app))
    checkHashChanges('changing a dict value', lambda: setDictValue(app))
    checkHashChanges('changing a dict in a list', lambda: setNestedDictValue(app))
    checkHashChanges('reordering a list', lambda: reorderList(app))
    checkHashChanges('changing a large number', lambda: growLargeNumber(app))
    checkHashChanges('adding to a set', lambda: app.tags.add('z'))
    checkHashChanges('replacing a tuple', lambda: setattr(app, 'point', (4, 3)))
    checkHashChanges('adding an app property', lambda: setattr(app, 'extra', 1))


def redrawAll(app):
    drawRect(100, 100, 200, 200, fill='teal')
