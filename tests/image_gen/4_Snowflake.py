Rect(0, 0, 400, 400, fill='midnightBlue')
Star(200, 200, 200, 12, fill=None, border='azure', roundness=0)
Star(200, 200, 200, 6, fill=None, border='azure', roundness=70)
Star(200, 200, 185, 6, fill='midnightBlue', border='azure', roundness=55)
RegularPolygon(200, 200, 110, 6, fill=None, border='azure', roundness=10)
Star(200, 200, 160, 6, fill=None, border='azure', borderWidth=3, roundness=10)
Star(200, 200, 105, 6, fill='midnightBlue', border='azure', roundness=40)
Star(200, 200, 105, 6, fill=None, border='azure')
Star(200, 200, 70, 6, fill=None, border='azure', roundness=0)
Circle(200, 200, 15, fill='midnightBlue', border='azure')
# give an opacity to the entire snowflake
Star(200, 200, 200, 6,
     fill=gradient('azure', 'midnightBlue', 'azure', start='left-top'),
     opacity=30, roundness=70)

# This test case is intentionally left blank.

