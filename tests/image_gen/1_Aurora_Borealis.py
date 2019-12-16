# back layer to maintain color
Rect(0, 0, 400, 400, fill=gradient('navy', 'darkCyan', start='top'))
# create the stary effect
Line(0, 400, 400, 0, fill='white', lineWidth=600, dashes=(1, 30))
Line(0, 200, 400, 200, fill=gradient('navy', 'darkCyan', start='top'),
     lineWidth=400, dashes=(25, 1))
# create light effect
Rect(0, 0, 400, 300,
     fill=gradient('whiteSmoke', 'darkMagenta', 'chartreuse', 'lightCyan',
                   'darkMagenta', 'royalBlue', start='right-bottom'), opacity=40)
# overlay to give the night time effect
Rect(0, 0, 400, 300, fill=gradient('black', 'darkCyan', start='top'), opacity=50)
# lake background color and reflection color
Rect(0, 300, 400, 100, fill='midnightBlue')
Rect(0, 300, 400, 100,
     fill=gradient('whiteSmoke', 'darkMagenta',
                   'chartreuse', 'lightCyan', 'darkMagenta', 'royalBlue',
                   start='right-bottom'), opacity=20)
# mountain
Polygon(0, 400, 0, 290, 24, 281, 39, 284, 59, 268, 74, 283, 96, 290, 116, 277,
        126, 258, 140, 269, 157, 282, 178, 280, 189, 271, 220, 260, 244, 270,
        265, 265, 279, 245, 305, 228, 343, 198, 380, 158, 395, 170, 400, 150,
        400, 300, 386, 304, 359, 310, 342, 310, 335, 310, 325, 304, 304, 300,
        280, 303, 246, 315, 210, 324, 159, 319, 127, 324, 92, 330, 70, 325, 55,
        320, 60, 330, 82, 347, 93, 361, 118, 375, 185, 375, 199, 372, 211, 363,
        229, 375, 243, 381, 262, 381, 295, 380, 313, 383, 344, 385, 354, 390,
        376, 392, 389, 396, 400, 400)
# slight mountain highlight
Polygon(0, 400, 0, 290, 24, 281, 39, 284, 59, 268, 74, 283, 96, 290, 116, 277,
        126, 258, 140, 269, 157, 282, 178, 280, 189, 271, 220, 260, 244, 270,
        265, 265, 279, 245, 305, 228, 343, 198, 380, 158, 395, 170, 400, 150,
        400, 300, 386, 304, 359, 310, 342, 310, 335, 310, 325, 304, 304, 300,
        280, 303, 246, 315, 210, 324, 159, 319, 127, 324, 92, 330, 70, 325, 55,
        320, 60, 330, 82, 347, 93, 361, 118, 375, 185, 375, 199, 372, 211, 363,
        229, 375, 243, 381, 262, 381, 295, 380, 313, 383, 344, 385, 354, 390,
        376, 392, 389, 396, 400, 400, opacity=50,
        fill=gradient('black', 'midnightBlue', 'darkBlue', start='bottom'))

# This test case is intentionally left blank.

