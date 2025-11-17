import random

class Game:
    def __init__(self):
        pass

    def get_user_item(self):
        while True:
            user_input = input("Choose rock, paper, or scissors: ").lower()
            if user_input in ["rock", "paper", "scissors"]:
                return user_input
            else:
                print("Invalid choice. Please try again.")

    def get_computer_item(self):
        return random.choice(["rock", "paper", "scissors"])
    
    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (user_item == "rock" and computer_item == "scissors") or \
             (user_item == "scissors" and computer_item == "paper") or \
             (user_item == "paper" and computer_item == "rock"):
            return "win"
        else:
            return "loss"
        
    def play(self):
        user_choice = self.get_user_item()
        computer_choice = self.get_computer_item()
        result = self.get_game_result(user_choice, computer_choice)
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(f"Result: {result.capitalize()}!\n")
        
        return result