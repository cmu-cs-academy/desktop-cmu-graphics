### For your reference, Monkey latin follows these rules:
#   - If the first letter of the word is a vowel, a 'way' is added to the end.
#   - If the first letter of the word is a consonant, the letter is put at the
#     end of the word and an 'ay' is added.

app.background = 'forestGreen'

# monkey
Arc(215, 270, 80, 70, 270, 180, fill=None, border='peru', borderWidth=16)
Arc(215, 270, 48, 38, 270, 180, fill='forestGreen')
Arc(280, 270, 80, 70, 90, 180, fill=None, border='peru', borderWidth=16)
Arc(280, 270, 48, 38, 90, 180, fill='forestGreen')
Circle(312, 270, 8, fill='peru')
Oval(180, 275, 50, 60, fill=rgb(190, 120, 50), rotateAngle=30)
Oval(70, 275, 50, 60, fill=rgb(190, 120, 50), rotateAngle=330)
Circle(125, 250, 65, fill='peru')
Oval(160, 235, 40, 70, fill=rgb(190, 120, 50), rotateAngle=40)
Oval(90, 235, 40, 70, fill=rgb(190, 120, 50), rotateAngle=320)
Oval(85, 310, 35, 20, fill='wheat')
Oval(165, 310, 35, 20, fill='wheat')
Circle(75, 170, 12, fill='wheat')
Circle(175, 170, 12, fill='wheat')
Circle(125, 172, 50, fill='peru')
Oval(125, 180, 60, 45, fill='wheat')
Circle(110, 165, 18, fill='wheat')
Circle(140, 165, 18, fill='wheat')
Oval(125, 177, 10, 5)
Circle(110, 165, 4)
Circle(140, 165, 4)

# speech bubble
Polygon(230, 95, 300, 85, 200, 145, fill='white', border='black')
Arc(200, 60, 300, 80, 168, 335, fill=None, border='black')
Oval(200, 60, 295, 75, fill='white')
translatedWord = Label('', 200, 60, size=18)

# tree
Rect(0, 0, 30, 400, fill=gradient('sienna', 'brown', start='right-top'))
Line(10, 335, 400, 335, fill=gradient('sienna', 'brown', start='right-top'),
     lineWidth=50)

Label('Press space to enter a word to translate', 215, 380, size=18, bold=True)

def speakMonkeyLatin():
    word = app.getTextInput()
    vowels = 'AEIOUaeiou'
    monkeyLatin = ''

    # If the first letter of the word is in the vowels string,
    # set monkeyLatin equal to that word + 'way'.
    if (word[0] in vowels):
        monkeyLatin = word + 'way'
    # Otherwise loop over the string, skipping the first letter.
    # Then put the first letter at the end and add 'ay'.
    else:
        for index in range(1, len(word)):
            monkeyLatin += word[index]
        monkeyLatin += word[0]
        monkeyLatin += 'ay'
    translatedWord.value = monkeyLatin

def onKeyPress(key):
    if (key == 'space'):
        speakMonkeyLatin()

app.setTextInputs('amazing')
onKeyPress('space')


# -
### For your reference, Monkey latin follows these rules:
#   - If the first letter of the word is a vowel, a 'way' is added to the end.
#   - If the first letter of the word is a consonant, the letter is put at the
#     end of the word and an 'ay' is added.

app.background = 'forestGreen'

# monkey
Arc(215, 270, 80, 70, 270, 180, fill=None, border='peru', borderWidth=16)
Arc(215, 270, 48, 38, 270, 180, fill='forestGreen')
Arc(280, 270, 80, 70, 90, 180, fill=None, border='peru', borderWidth=16)
Arc(280, 270, 48, 38, 90, 180, fill='forestGreen')
Circle(312, 270, 8, fill='peru')
Oval(180, 275, 50, 60, fill=rgb(190, 120, 50), rotateAngle=30)
Oval(70, 275, 50, 60, fill=rgb(190, 120, 50), rotateAngle=330)
Circle(125, 250, 65, fill='peru')
Oval(160, 235, 40, 70, fill=rgb(190, 120, 50), rotateAngle=40)
Oval(90, 235, 40, 70, fill=rgb(190, 120, 50), rotateAngle=320)
Oval(85, 310, 35, 20, fill='wheat')
Oval(165, 310, 35, 20, fill='wheat')
Circle(75, 170, 12, fill='wheat')
Circle(175, 170, 12, fill='wheat')
Circle(125, 172, 50, fill='peru')
Oval(125, 180, 60, 45, fill='wheat')
Circle(110, 165, 18, fill='wheat')
Circle(140, 165, 18, fill='wheat')
Oval(125, 177, 10, 5)
Circle(110, 165, 4)
Circle(140, 165, 4)

# speech bubble
Polygon(230, 95, 300, 85, 200, 145, fill='white', border='black')
Arc(200, 60, 300, 80, 168, 335, fill=None, border='black')
Oval(200, 60, 295, 75, fill='white')
translatedWord = Label('', 200, 60, size=18)

# tree
Rect(0, 0, 30, 400, fill=gradient('sienna', 'brown', start='right-top'))
Line(10, 335, 400, 335, fill=gradient('sienna', 'brown', start='right-top'),
     lineWidth=50)

Label('Press space to enter a word to translate', 215, 380, size=18, bold=True)

def speakMonkeyLatin():
    word = app.getTextInput()
    vowels = 'AEIOUaeiou'
    monkeyLatin = ''

    # If the first letter of the word is in the vowels string,
    # set monkeyLatin equal to that word + 'way'.
    if (word[0] in vowels):
        monkeyLatin = word + 'way'
    # Otherwise loop over the string, skipping the first letter.
    # Then put the first letter at the end and add 'ay'.
    else:
        for index in range(1, len(word)):
            monkeyLatin += word[index]
        monkeyLatin += word[0]
        monkeyLatin += 'ay'
    translatedWord.value = monkeyLatin

def onKeyPress(key):
    if (key == 'space'):
        speakMonkeyLatin()



# -
### For your reference, Monkey latin follows these rules:
#   - If the first letter of the word is a vowel, a 'way' is added to the end.
#   - If the first letter of the word is a consonant, the letter is put at the
#     end of the word and an 'ay' is added.

app.background = 'forestGreen'

# monkey
Arc(215, 270, 80, 70, 270, 180, fill=None, border='peru', borderWidth=16)
Arc(215, 270, 48, 38, 270, 180, fill='forestGreen')
Arc(280, 270, 80, 70, 90, 180, fill=None, border='peru', borderWidth=16)
Arc(280, 270, 48, 38, 90, 180, fill='forestGreen')
Circle(312, 270, 8, fill='peru')
Oval(180, 275, 50, 60, fill=rgb(190, 120, 50), rotateAngle=30)
Oval(70, 275, 50, 60, fill=rgb(190, 120, 50), rotateAngle=330)
Circle(125, 250, 65, fill='peru')
Oval(160, 235, 40, 70, fill=rgb(190, 120, 50), rotateAngle=40)
Oval(90, 235, 40, 70, fill=rgb(190, 120, 50), rotateAngle=320)
Oval(85, 310, 35, 20, fill='wheat')
Oval(165, 310, 35, 20, fill='wheat')
Circle(75, 170, 12, fill='wheat')
Circle(175, 170, 12, fill='wheat')
Circle(125, 172, 50, fill='peru')
Oval(125, 180, 60, 45, fill='wheat')
Circle(110, 165, 18, fill='wheat')
Circle(140, 165, 18, fill='wheat')
Oval(125, 177, 10, 5)
Circle(110, 165, 4)
Circle(140, 165, 4)

# speech bubble
Polygon(230, 95, 300, 85, 200, 145, fill='white', border='black')
Arc(200, 60, 300, 80, 168, 335, fill=None, border='black')
Oval(200, 60, 295, 75, fill='white')
translatedWord = Label('', 200, 60, size=18)

# tree
Rect(0, 0, 30, 400, fill=gradient('sienna', 'brown', start='right-top'))
Line(10, 335, 400, 335, fill=gradient('sienna', 'brown', start='right-top'),
     lineWidth=50)

Label('Press space to enter a word to translate', 215, 380, size=18, bold=True)

def speakMonkeyLatin():
    word = app.getTextInput()
    vowels = 'AEIOUaeiou'
    monkeyLatin = ''

    # If the first letter of the word is in the vowels string,
    # set monkeyLatin equal to that word + 'way'.
    if (word[0] in vowels):
        monkeyLatin = word + 'way'
    # Otherwise loop over the string, skipping the first letter.
    # Then put the first letter at the end and add 'ay'.
    else:
        for index in range(1, len(word)):
            monkeyLatin += word[index]
        monkeyLatin += word[0]
        monkeyLatin += 'ay'
    translatedWord.value = monkeyLatin

def onKeyPress(key):
    if (key == 'space'):
        speakMonkeyLatin()

app.setTextInputs('monkey')
onKeyPress('space')

