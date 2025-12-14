class Move:
    def __init__(self, initial, final):
        self.initial = initial
        self.final = final

    def __eq__(self, other):
        return (
            isinstance(other, Move)
            and self.initial == other.initial
            and self.final == other.final
        )

    def __repr__(self):
        return f"{self.initial}->{self.final}"
