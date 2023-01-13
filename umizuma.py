
"""
TODO:
- add choice to select amount of players
"""

class Umizuma:
    """ Defines all functions needed to play a game of umizuma """

    def __init__(self):
        self.player_tracker = 0

    def menu_display(self):
        print("\nPress 1 to view game instructions\nPress 2 to start a new game\nPress 3 to quit")
    
    def game_instructions(self):
        print("\n--------------------\n\nAll players throw out their hand each showing zero or thumbs up for 1\nOne player calls out their guess of what the sum of all hands will be\nIf the player guesses the sum correctly, that player is either out, OR if there are only 2 players remaining, wins the round!\nThe first player to win 3 rounds wins the game!\n\n-------------------\n")
    
    def menu_selection(self):
        choices = [x for x in range(1, 4)]
        print("--- WELCOME TO UMIZUMA ---")
        while True:
            self.menu_display()
            user_choice = int(input())
            if user_choice not in choices:
                print("Please only select 1, 2, or 3")
                continue
            elif user_choice == 1:
                self.game_instructions()
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
