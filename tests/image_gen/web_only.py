###########
# Ensure i18n for list remove works

a = [0, 1, 2]
a.remove(0)
assert a == [1, 2]