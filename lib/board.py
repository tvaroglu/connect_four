class Board:
    def __init__(self):
        pass

    def dividers(self):
        output_list = []
        section = '+---'
        for i in range(1, 8):
            output_list.append(section)
        output_list[-1] = section + '+'
        return output_list

    def full_divider(self):
        return ''.join(self.dividers())
