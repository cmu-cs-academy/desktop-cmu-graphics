# Wyvern

The goal of the `wyvern` project is to combine the `pygame` and `cairo` dependencies in Desktop CMU Graphics into a single library which uses Rust as a backend. Doing this will help reduce both the size of the CMU Graphics zipfile and possibly improve the speed and quality of the graphics.

## Organization

The `wyvern` directory has the following layout:
```
wyvern
- src
  - lib.rs
  - lib-old.rs
- Cargo.toml
- pyproject.toml
- modal.py
- test.py
  ...
```

- `src/lib-rs`
    - Contains the current Rust development, which will be described in more detail in the next section
- `src/lib-old.rs`
    - Contains the inital "prototype" implementation using `skia_safe` and `winit` to replace `cairo` and `pygame` written by Austin. This implementation can be used to run `test.py` (the current `lib.rs` does not support `test.py`)
- `Cargo.toml`
    - Rust project file which contains all of the Rust dependencies and linting options
- `pyproject.toml`
    - Python project file which specifies `maturin` as the build system. This is necessary to be able to build the Rust code into a Python wheel
- `modal.py`
    - A modified version `cmu_graphics/modal.py` which compiles with the current implementations from the Python `wyvern` module
- `test.py`
    - A prototype test file which works with `lib-old.rs`

## Building

To compile the project in Rust, simply run `cargo build`. Running `cargo build` will only compile the code in `lib.rs`, any other code inside the `src` directory will be ignored.

To build the `wyvern` Python module from the Rust code, run `maturin build`. This should create a directory in the Rust project called `target` with subdirectory `wheels`, which should contain the respective wheel. You can then install the wheel using `pip install wheelname.whl`. After you've installed the wheel, you can use `import wyvern` in a Python file as you would for a normal package.

## Current Work

The approach thus far has been to replace the minimum amount of `cairo`/`pygame` functionalities needed for CMU Graphics to work. To do this, I have been targeting the files in the `cmu_graphics` directory and doing a one-to-one translation of the methods from each package, starting with `cairo`.

To start, I targeted the `cairo` dependencies found in `cmu_graphics/modal.py`. This includes the following `cairo` structs and methods:
- `cairo.ImageSurface`
- Methods for drawing on the image surface context:
    - `save`
    - `restore`
    - `new_path`
    - `move_to`
    - `line_to`
    - `rel_line_to`
    - `rel_curve_to`
    - `rectangle`
    - `round_rectangle`
    - `close_path`
    - `set_source_rgba`
    - `set_line_width`
    - `select_font_face`
    - `set_font_size`
    - `text_path`
    - `text_extents`
    - `stroke`
    - `clip`
    - `fill`

All of the above methods are implemented as methods for the Rust `Canvas` struct and then are reimplemented as wrapper functions to operate on the type `Py<Canvas>` (a Python reference of the struct which can then be exported to Python).

## Issues and Future Work

Currently, the `modal.py` file in this directory compiles and successfully launches the `pygame` window, but does not yet draw anything to the `pygame` window.

Here is a list of issues I have run into which may have some impact on the above problem:
- It is forbidden to export structs with mutable properties from Rust to Python due to the requirement from Rust to keep track of lifetimes. For example, trying to change the `path` property in `Canvas` to a mutable reference (i.e. adding `&mut` to the type) will require you to add a lifetime label to the struct, and once the label has been added it is no longer compatible to be exported to Python. This means that any mutation is confined to be "benign" (i.e. hidden within the methods)
    - As a consequence, any method that updates the `Canvas` needs to return a new version of the `Canvas` with new properties. I have tried to implement a version that just mutates within the methods and returns a `()` when its done, but those updates are not observed in Python. As such, those updates are relegated to Python:
    ```
    def draw(self, ctx):
        ctx = wyvern.save(ctx)

        ctx = self.drawBox(ctx)
        _, ctx = self.drawPrompt(ctx)
        if self.textBox:
            ctx = self.textBox.draw(ctx)
        ctx = self.button.draw(ctx)

        ctx = wyvern.restore(ctx)

        return ctx
    ```
    - This could possibly also be a Rust skill issue on my part, at least with the issue of being forced to return a new copy of the context instead of mutating it internally, but at the very least the lifetime issue is real
- As mentioned, nothing is being drawn in the modal as of now. My guess is either (1) the drawing context is still not being updated correctly despite me changing the methods to return the updated `Canvas` or (2) the `Canvas` is not being correctly exported to `pygame`. Point (2) shows up in the following:
```
def redrawAll(self, screen, wyvern_surface, ctx):
    ctx = self.draw(ctx)
    data_string = wyvern_surface.data
    pygame_surface = pygame.image.frombuffer(
        data_string, (int(self.width), int(self.height)), 'RGBA'
    )
    screen.blit(pygame_surface, (0, 0))
```

For future work, I would start by trying to get `modal.py` working properly to check that the current implementations do indeed serve as a replacement for the `cairo` graphics methods. After that, I would start to replace the `pygame` dependencies in this file.