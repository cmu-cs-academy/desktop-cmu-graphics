assert gradient('red', 'blue') == gradient('red', 'blue')
assert gradient('red', 'blue', start='center') == gradient('red', 'blue')
assert gradient('red', 'blue', start='left') == gradient('red', 'blue', start='left')

assert gradient('red', 'blue') != gradient('red', 'blue', start='left')
assert gradient('red', 'blue', start='left') != gradient('red', 'blue')
assert gradient('red', 'green') != gradient('red', 'blue')
assert gradient('red', 'blue', 'orange') != gradient('red', 'blue')


assert rgb(0, 0, 0) == rgb(0, 0, 0)
assert rgb(1, 0, 0) != rgb(0, 0, 0)
assert rgb(0, 1, 0) != rgb(0, 0, 0)
assert rgb(0, 0, 1) != rgb(0, 0, 0)

assert gradient('red', rgb(0, 0, 5)) == gradient('red', rgb(0, 0, 5))

assert gradient('red', rgb(0, 0, 5)) != gradient('red', rgb(0, 5, 0))
assert gradient('red', rgb(0, 0, 5)) != gradient('red', 'green')
assert gradient('red', 'green') != gradient('red', rgb(0, 0, 5))

rect = Rect(50, 50, 150, 150, fill=gradient('orange', 'red'))
assert rect.fill == gradient('orange', 'red')
