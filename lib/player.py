class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def full_color(self):
        return 'Red' if self.color == 'R' else 'Black'

    def greet(self):
        return f"Welcome, {self.name}! Your color is '{self.full_color()}'"
