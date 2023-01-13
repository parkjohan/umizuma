"""
all players throw out a single hand, each showing zero to five fingers, and call out their guess at what the sum of all fingers shown will be. If one player guesses the sum, that player earns one point. The first player to reach three points wins the game.
"""

"""
TODO:
- add choice to select amount of players
"""

class Umizuma:
    """ Defines all functions needed to play a game of umizuma """

    def __init__(self):
        self.player_tracker = 0

    def intro_message(self):
        print("--- WELCOME TO UMIZUMA ---")
        # print("In this game, each player takes turns calling out a number.")
        # print("The number being called out MUST be from 0 up to the number of players playing.")
        print("\nPress 1 to view game instructions\nPress 2 to start a new game\nPress 3 to quit")
    
    def menu_selection(self):
        choices = [x for x in range(1, 4)]
        while True:
            self.intro_message()
            user_choice = int(input())
            if user_choice not in choices:
                print("Please only select 1, 2, or 3")
                continue
            elif user_choice == 1:
                print("Displaying game instructions")
                continue
            elif user_choice == 2:
                print("Starting a new game...")
                continue
            elif user_choice == 3:
                print("Thanks for playing!")
                break


if __name__ == "__main__":
    new_game = Umizuma()
    print(new_game.menu_selection())
