def quit_program():
    print("Exiting the program...")
    quit()


def playAgain():
    choice = input("\nDo you wish to play again? (Yes/No) : ")
    if choice.lower() == "yes":
        game()
    elif choice.lower() == "no":
        quit_program()


def game():
    print("\nOkay, Let's Play :)")
    score = 0

    answer = input("\nWhat is the Capital of Japan : ")
    if answer.lower() == "tokyo":
        print("Correct")
        score += 1

    else:
        print("Incorrect, You have lost the game!")
        print("Your Score : " + str(score))
        playAgain()

    answer = input("\nWhat is the Capital of India : ")
    if answer.lower() == "new delhi":
        print("Correct")
        score += 1

    else:
        print("Incorrect, You have lost the game!")
        print("Your Score : " + str(score))
        playAgain()

    answer = input("\nWhat is the Capital of Brazil : ")
    if answer.lower() == "brasilia":
        print("Correct")
        score += 1

    else:
        print("Incorrect, You have lost the game!")
        print("Your Score : " + str(score))
        playAgain()

    answer = input("\nWhat is the Capital of Australia : ")
    if answer.lower() == "sydney":
        print("Correct")
        score += 1

    else:
        print("Incorrect, You have lost the game!")
        print("Your Score : " + str(score))
        playAgain()

    print("\nCongratulations!, You have won the Game")
    print("Your Score : " + str(score))
    playAgain()


print("Hello, Welcome to my Quiz Game!")
play = input("Do you want to play this Game? (Yes/No) : ")

if play.lower() == "yes":
    game()
else:
    quit_program()
