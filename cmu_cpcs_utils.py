import copy

EPSILON = 10**-7


def almostEqual(x, y, epsilon=EPSILON):
    return abs(x - y) <= epsilon


def rounded(d):
    sign = 1 if (d >= 0) else -1
    d = abs(d)
    n = int(d)
    if d - n >= 0.5:
        n += 1
    return sign * n


def testFunction(fn):
    return fn


def multilineRepr(s):
    if not isinstance(s, str) or '\n' not in s:
        return repr(s)

    quote = "'"
    if "'" in s and '"' not in s:
        quote = '"'

    result = [quote * 3]

    startIdx = 0
    if s[0] == '\n':
        startIdx = 1
        result.append('\n')
    else:
        result.append('\\')
        result.append('\n')

    for i in range(startIdx, len(s)):
        c = s[i]

        if c == quote or c == '\\':
            result.append('\\')
            result.append(c)
        elif c == '\t':
            result.append('\\')
            result.append('t')
        elif c == '\n':
            result.append('\n')
        elif c == '\r':
            result.append('\\')
            result.append('t')
        elif c < ' ' or c >= '\x7f':
            result.append('\\x')
            result.append('%02x' % ord(c))
        else:
            result.append(c)

    result.append(quote * 3)

    return ''.join(result)


def getColWidths(a):
    colWidths = dict()
    for row in range(len(a)):
        if not (isinstance(a[row], list) or isinstance(a[row], tuple)):
            continue
        for col in range(len(a[row])):
            colWidths[col] = max(colWidths.get(col, 0), len(repr(a[row][col])))
    return colWidths


def nestedListReprAddElem(output, a, row, col, colWidths):
    elem = a[row][col]
    if col > 0:
        output.append(', ')
    justMethod = 'ljust'
    if isinstance(a[row][col], int) or isinstance(a[row][col], float):
        justMethod = 'rjust'
    output.append(getattr(repr(elem), justMethod)(colWidths[col]))


def is2dList(a):
    if not isinstance(a, list):
        return False
    for elem in a:
        if isinstance(elem, list) or isinstance(elem, tuple):
            return True
    return False


def prettyListRepr(a):
    if a == []:
        return '[]'
    if not is2dList(a):
        return repr(a)
    output = []
    colWidths = getColWidths(a)
    output.append('[\n')
    for row in range(len(a)):
        if isinstance(a[row], list) or isinstance(a[row], tuple):
            lParen, rParen = '[', ']'
            if isinstance(a[row], tuple):
                lParen, rParen = '(', ')'
            output.append(f' {lParen} ')
            for col in range(len(a[row])):
                nestedListReprAddElem(output, a, row, col, colWidths)
            output.append(f' {rParen}')
        else:
            output.append(' ' + repr(a[row]))
        if row < len(a) - 1:
            output.append(',')
        output.append('\n')
    output.append(']')
    return ''.join(output)


def prettyStr(o):
    if isinstance(o, str) and '\n' in o:
        return multilineRepr(o)

    if isinstance(o, list):
        return prettyListRepr(o)

    return repr(o)


def prettyPrint(o):
    print(prettyStr(o))


class Tree:
    def __init__(self, value, *children):
        self.value = value
        self.children = children

    def __str__(self):
        return self.toString()

    def __repr__(self):
        if self.isLeaf():
            return f'Tree({repr(self.value)})'
        else:
            childStrs = [repr(child) for child in self.children]
            children = ', '.join(childStrs)
            return f'Tree({repr(self.value)}, {children})'

    def __eq__(self, other):
        return (
            isinstance(other, Tree)
            and (self.value == other.value)
            and (len(self.children) == len(other.children))
            and (
                all(
                    [
                        myChild == otherChild
                        for myChild, otherChild in zip(self.children, other.children)
                    ]
                )
            )
        )

    def isLeaf(self):
        return len(self.children) == 0

    def addChild(self, child):
        if not isinstance(child, Tree):
            raise Exception('The child is not a Tree object.')
        if self._containsTree(child):
            raise Exception('The child tree is already in this tree.')
        self.children += (child,)

    def removeChild(self, child):
        if child not in self.children:
            raise Exception('The tree is not a child of this tree.')
        i = self.children.index(child)
        self.children = self.children[:i] + self.children[i + 1 :]

    def _containsTree(self, Tree):
        if self is Tree:
            return True
        for child in self.children:
            if child._containsTree(Tree):
                return True
        return False

    def toString(self, compact=False, symmetric=False):
        if compact:
            return self.vshow()
        else:
            return self.hshow(symmetric)

    def vshow(self):
        def walk(tree, prefix1, prefix2):
            lines = [prefix1 + str(tree.value)]
            for i in range(len(tree.children)):
                lastChild = i == len(tree.children) - 1
                c1, c2 = ('└', ' ') if lastChild else ('├', '│')
                lines.append(
                    walk(tree.children[i], prefix2 + c1 + '── ', prefix2 + c2 + '   ')
                )
            return '\n'.join(lines)

        return walk(self, '', '')

    def hshow(self, symmetric=False):
        padLengths = self._lengthsByLevel()
        paddedTree = self._padValues(padLengths)
        hshowList = paddedTree._hshowHelper(symmetric)
        # return hshowList
        return '\n'.join(''.join(row) for row in hshowList)

    # Assumes the tree is padded (by calling ._padValues), and all the values
    # are strings (which ._padValues) also does
    # Horizontal: chr(0x2500)
    # Vertical: chr(0x2502)
    # Top corner: chr(0x250c)
    # Bottom corner: chr(0x2514)
    def _hshowHelper(self, symmetric=False):
        if self.isLeaf():
            return [[chr(0x2500), chr(0x2500), chr(0x2500), str(self.value)]]
        else:
            childLists = []
            for child in self.children:
                childLists.append(child._hshowHelper(symmetric))
            # Pad each child tree to the larger of itself and its symmetric tree
            if symmetric:
                for i in range(len(childLists) // 2):
                    L1 = childLists[i]
                    L2 = childLists[-i - 1]
                    maxHeight = max(len(L1), len(L2))
                    Tree._padTreeToHeight(L1, maxHeight)
                    Tree._padTreeToHeight(L2, maxHeight)
            # Combine all the child lists vertically, leaving space in the front
            # for the current element, and 1 row of space between each child
            valueLen = len(self.value)
            frontPadding = 7 + valueLen
            for childList in childLists:
                for row in childList:
                    for _ in range(frontPadding):
                        row.insert(0, ' ')
            result = []
            for i in range(len(childLists)):
                result.extend(copy.deepcopy(childLists[i]))
                result.append([' '] * frontPadding)
            result.pop()  # remove the extra empty list added at the end
            # Insert the element and horizontal lines on either side of it
            midRow = len(result) // 2
            result[midRow][0] = chr(0x2500)
            result[midRow][1] = chr(0x2500)
            result[midRow][2] = chr(0x2500)
            for i in range(valueLen):
                result[midRow][3 + i] = self.value[i]
            result[midRow][3 + valueLen] = chr(0x2500)
            result[midRow][4 + valueLen] = chr(0x2500)
            result[midRow][5 + valueLen] = chr(0x2500)
            # Add the vertical lines connecting all the children
            startRow = len(childLists[0]) // 2
            endRow = len(result) - len(childLists[-1]) // 2
            if startRow == endRow - 1:  # if there's only 1 child just make -
                result[startRow][6 + valueLen] = chr(0x2500)
            else:  # If more than 1 child, make top and bottom corners
                result[startRow][6 + valueLen] = chr(0x250C)
                result[endRow - 1][6 + valueLen] = chr(0x2514)
            for row in range(startRow + 1, endRow - 1):
                left = result[row][5 + valueLen]
                right = (
                    result[row][7 + valueLen]
                    if (7 + valueLen < len(result[row]))
                    else ' '
                )
                if left != ' ' and right != ' ':  # character is +
                    c = chr(0x253C)
                elif left != ' ':  # character is -|
                    c = chr(0x2524)
                elif right != ' ':  # character is |-
                    c = chr(0x251C)
                else:  # character is |
                    c = chr(0x2502)
                result[row][6 + valueLen] = c
            return result

    # Returns a dictionary mapping each level to the max length of a value at
    # that level
    def _lengthsByLevel(self, level=0):
        res = {level: len(str(self.value))}
        for child in self.children:
            childLengths = child._lengthsByLevel(level + 1)
            for lvl, length in childLengths.items():
                if lvl in res:
                    res[lvl] = max(res[lvl], length)
                else:
                    res[lvl] = length
        return res

    # Creates a new tree with all values converted to a string
    # Values at the leaves do not change
    # Other values are padded with '-' on either side to the length of the
    # max length value in that level of the tree
    def _padValues(self, padLengths, level=0):
        if self.isLeaf():
            return Tree(str(f' {self.value} '))
        else:
            length = padLengths[level]
            paddedVal = Tree._padValue(self.value, length)
            paddedChildren = [
                child._padValues(padLengths, level + 1) for child in self.children
            ]
            return Tree(paddedVal, *paddedChildren)

    @staticmethod
    def _padValue(val, length):
        valStr = str(val)
        lengthDiff = length - len(valStr)
        leftPad = lengthDiff // 2
        rightPad = lengthDiff - leftPad
        return (chr(0x2500) * leftPad) + f' {val} ' + (chr(0x2500) * rightPad)

    @staticmethod
    def _padTreeToHeight(L, height):
        heightDiff = height - len(L)
        padding = heightDiff // 2
        for _ in range(padding):
            L.insert(0, [])
            L.append([])

    @staticmethod
    def fromVshowString(vshowString, valueType=str):
        lines = vshowString.splitlines()
        root = Tree(valueType(lines[0]))
        openTrees = [root]
        for line in lines[1:]:
            i = line.rfind('── ') + 3
            depth = i // 4
            openTrees = openTrees[:depth]
            child = Tree(valueType(line[i:]))
            openTrees[-1].addChild(child)
            openTrees.append(child)
        return root


__all__ = [
    'almostEqual',
    'testFunction',
    'prettyPrint',
    'prettyStr',
    'Tree',
    'rounded',
]
