from .color import Color


class Theme:
    def __init__(self):
        self.light = Color.LIGHT_SQUARE
        self.dark = Color.DARK_SQUARE
        self.highlight = Color.HIGHLIGHT
        self.hint = Color.HINT
        self.outline = Color.OUTLINE
        self.bg = Color.BG
        self.text = Color.TEXT
        self.drag = Color.DRAG

    def square_colors(self):
        return self.light, self.dark
