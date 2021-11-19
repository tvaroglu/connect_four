class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def full_color(self):
        return 'Red' if self.color == '🟥' else 'Black'
