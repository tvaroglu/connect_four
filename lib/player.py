class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.default_name = 'Skynet'

    def full_color(self):
        return 'Red' if self.color == '🟥' else 'Black'
