from src.theme import Theme


class Config:
    def __init__(self):
        self.theme = Theme()
        self.show_hints = True
        self.promote_to = "queen"
