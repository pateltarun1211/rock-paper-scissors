import random

rpc = {
    1: 'rock',
    2: 'paper',
    3: 'scissors'
}

player_name = input("Enter your name player: ")
print(player_name + ", WELCOME TO DIE!")

while True:
    player_choice = input("\nChoose your move(rock, paper, scissors) or 'quit': ")
    computer_choice = random.randint(1, 3)
    print('\n')

    if player_choice.lower().strip() == 'quit':
        break

    for key, value in rpc.items():
        if player_choice == rpc[computer_choice]:
            print(f"{player_name} chose same as computer: It's a tie.")
            break
        elif player_choice == 'rock':
            if rpc[computer_choice] == 'scissors':
                print("Computer chose " + rpc[computer_choice] + ", You win!")
                break
            else:
                print("Computer chose " + rpc[computer_choice] + ", You lose!")
                break

        elif player_choice == 'paper':
            if rpc[computer_choice] == 'rock':
                print("Computer chose " + rpc[computer_choice] + ", You win!")
                break
            else:
                print("Computer chose " + rpc[computer_choice] + ", You lose!")
                break

        elif player_choice == 'scissors':
            if rpc[computer_choice] == 'paper':
                print("Computer chose " + rpc[computer_choice] + ", You win!")
                break
            else:
                print("Computer chose " + rpc[computer_choice] + ", You lose!")
                break
                