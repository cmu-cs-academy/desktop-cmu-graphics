import io
import contextlib


def capture_stdout(f):
    captured_output = io.StringIO()
    with contextlib.redirect_stdout(captured_output):
        f()
    return captured_output.getvalue()

# Make sure warning prints when user tries to use a font that may not be installed
assert "INFO:" in capture_stdout(lambda: Label("Hello, World!",  100, 100, fill='black', font='orbitron', size=20))
# Make sure warning does not print when the user tries to use it again
assert "INFO:" not in capture_stdout(lambda: Label("Hello, World!",  100, 130, fill='black', font='orbitron', size=20))
# Make sure warning prints when a different font that may not be installed is used
assert "INFO:" in capture_stdout(lambda: Label("Hello, World!",  100, 160, fill='black', font='caveat', size=20))
# Make sure warning does not print with fonts that are widely available
assert "INFO:" not in capture_stdout(lambda: Label("Hello, World!",  100, 190, fill='black', font='arial', size=20))
# Make sure warning does not print when showFontWarnings is set to False
app.showFontWarnings = False
assert "INFO:" not in capture_stdout(lambda: Label("Hello, World!",  100, 220, fill='black', font='symbols', size=20))

