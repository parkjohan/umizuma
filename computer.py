import random

class Computer:

    def __init__(self) -> None:
        self.curr_choice = 0
        self.rebuttle = False

    def get_ran_choice(self):
        self.curr_choice = random.randint(0, 2)

    