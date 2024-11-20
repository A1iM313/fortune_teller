# This is my fortune teller game based on conditionals
print("Welcome to the game Paku-Paku, a fortune teller game that can predict the future!\n In order to play, you must select one of the options provided as your fortune is locked in.")
print("Please input one of the numbers below.\n (1\n (2\n (3\n (4") 
player_choice1 = int(input(""))

if player_choice1 == 1 or player_choice1 == 2:
    print("Please pick 'red' or 'blue'")
    player_choice2 = input("")
    if player_choice2 == "red":
        print("You got this.")
    elif player_choice2 == "blue":
        print("I believe in you")
    else:
        print("Please try again with a valid option")
elif player_choice1 == 3 or player_choice1 == 4:
    player_choice3 = input("Please pick 'green' or 'yellow'")
    if player_choice3 == "green":
     print("answer")
    elif player_choice3 == "yellow":
     print("answer2")
    else:
     print("Please try again with a valid option")
else:
   print("Please try again with a valid number.")









# if player_choice1 == 3 or 4:
#     print("Please pick 'green' or 'yellow")
#     player_choice2 = input("")
#     if player_choice2 == "green":
#         print("")
#     elif player_choice2 == "yellow":
#         print("")
#     else:
#         print("Please try again with a valid option")
