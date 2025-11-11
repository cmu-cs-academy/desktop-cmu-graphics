from cmu_cpcs_utils import almostEqual, Tree, rounded, testFunction


@testFunction
def foo():
    rounded(3.5)

foo()


tree = Tree(1,
          Tree(2,
            Tree(4)
          ),
          Tree(3)
         )

# Note there is a trailing space after both the 3 and 4 in this value:
expected = (
'         ┌─── 2 ─────── 4 \n'
'─── 1 ───┤\n'
'         └─── 3 '
)

assert expected == str(tree), (repr(expected),repr(str(tree)))