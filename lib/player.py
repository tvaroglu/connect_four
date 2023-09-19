class Player:

    def __init__(self, color, name='Skynet'):
        self.color = color
        self.name = name

    def full_color(self):
        return 'Red' if self.color == '🟥' else 'Black'
