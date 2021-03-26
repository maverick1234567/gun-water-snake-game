import random
print("lets start this game:-")
list= ['Snake' , 'Gun' , 'Water']
no_of_turns = 11
def game():
    global no_of_turns
    player_points = 0
    computer_points = 0
    while True:
        no_of_turns = no_of_turns - 1
        if no_of_turns>0:
            player= (input("enter the choice you want to enter ['Snake','Gun','Water']:"))
            r = random.choice(list)
            print(f"Computer's turn:{r}")
            if player == "Snake" and r == "Water":
                print("Player wins the turn.")
                player_points += 1
                print(f"Player's point: {player_points}")
                print(f"Computer's points: {computer_points}")
                print("")
            elif player == "Gun" and r == "Snake":
                print("Player wins the turn.")
                player_points += 1
                print(f"Player's point: {player_points}")
                print(f"Computer's points: {computer_points}")
                print("")
            elif player == "Water" and r == "Gun":
                print("Player wins the turn.")
                player_points += 1
                print(f"Player's point: {player_points}")
                print(f"Computer's points: {computer_points}")
                print("")
            elif player == "Water" and r == "Snake":
                print("Computer wins the turn.")
                print(f"Player's point: {player_points}")
                computer_points += 1
                print(f"Computer's points: {computer_points}")
                print("")
            elif player == "Snake" and r == "Gun":
                print("Computer wins the turn.")
                print(f"Player's point: {player_points}")
                computer_points += 1
                print(f"Computer's points: {computer_points}")
                print("")
            elif player == "Gun" and r == "Water":
                print("Computer wins the turn.")
                print(f"Player's point: {player_points}")
                computer_points += 1
                print(f"Computer's points: {computer_points}")
                print("")
            elif player == "Gun" and r == "Gun":
                print("No one wins, Its a Tie.")
                print(f"Player's point: {player_points}")
                print(f"Computer's points: {computer_points}")
                print("")
            elif player == "Water" and r == "Water":
                print("No one wins, Its a Tie.")
                print(f"Player's point: {player_points}")
                print(f"Computer's points: {computer_points}")
                print("")
            elif player == "Snake" and r == "Snake":
                print("No one wins, Its a Tie.")
                print(f"Player's point: {player_points}")
                print(f"Computer's points: {computer_points}")
                print("")
            else:
                print("please enter the valid input")
                print("")
        elif no_of_turns == 0:
            print("no.of turns are over.")
            print("")
            print("Now lets print the results, and declare who wins.")
            print(f"Player's point: {player_points}")
            print(f"Computer's points: {computer_points}")
            print("")
            if player_points > computer_points:
                print("Player wins the game!!!")
                print("")
                print("Game Over.")
            elif player_points < computer_points:
                print("Computer wins the game!!!")
                print("")
                print("Game Over.")
            elif player_points == computer_points:
                print("Game has been tied, no one wins.")
                print("")
                print("Game Over.")
game()

