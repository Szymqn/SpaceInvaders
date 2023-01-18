class Levels:
    def __init__(self, new_level):
        # Default value
        self.level = 1
        self.new_level = new_level
        self.change_lvl()

    def change_lvl(self):
        self.level = self.new_level
