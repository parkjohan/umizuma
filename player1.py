class Player1:

    def __init__(self) -> None:
        self.guess = 0
        self.sum_guess = 0
        self.rebuttle = False

    def get_sum_guess(self) -> int:
        while True:
            self.sum_guess = int(input())
            if self.sum_guess not in [x for x in range(0, 3)]:
                print("Your guess needs to be between 0 and 2!")
                continue
            else:
                return self.sum_guess

    def get_guess(self) -> int:
        while True:
            self.guess = int(input())
            if self.guess not in [x for x in range(0, 2)]:
                print("Your guess should be closed fist for 0 or thumbs up for 1")
                continue
            else:
                return self.guess
