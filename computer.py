import random

class Computer:

    def __init__(self) -> None:
        self.random_sum_guess = 0
        self.random_guess = 0
        self.rebuttle = False

    def get_random_sum_guess(self) -> int:
        self.random_sum_guess = random.randint(0, 2)
        return self.random_sum_guess

    def get_random_guess(self):
        self.random_guess = random.randint(0, 1)
        return self.random_guess
    