import time
import random

rpc = {
    1: 'rock',
    2: 'paper',
    3: 'scissors'
}

player_score = 0
computer_score = 0
draw_score = 0

print('\n!!---Rock Paper Scissors---!!')
print('!!---A Perry and Tarun Collab---!!\n')
player_name = input("Enter your name player: ")
print(player_name + ", WELCOME TO DIE!")

while True:
    player_choice = input("\nChoose your move(rock, paper, scissors) or 'quit': ")
    computer_choice = random.randint(1, 3)
    print('\n')

    if player_choice.lower().strip() == 'quit':
        break

    print('----> Rock')
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
""")

    time.sleep(.5)
    print('----> Paper')
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
    
    time.sleep(.5)
    print('----> Scissors')
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

    time.sleep(.5)
    print('----> Shoot')
    time.sleep(.5)
    print('\n')

    for key, value in rpc.items():
        if player_choice.lower().strip() == rpc[computer_choice]:
            print(f"{player_name} chose same as computer: It's a tie.")
            draw_score = draw_score + 1
            break
        elif player_choice.lower().strip() == 'rock':
            if rpc[computer_choice] == 'scissors':
                print("Computer chose " + rpc[computer_choice] + ", You win!")
                player_score = player_score + 1
                break
            else:
                print("Computer chose " + rpc[computer_choice] + ", You lose!")
                computer_score = computer_score + 1
                break

        elif player_choice.lower().strip() == 'paper':
            if rpc[computer_choice] == 'rock':
                print("Computer chose " + rpc[computer_choice] + ", You win!")
                player_score = player_score + 1
                break
            else:
                print("Computer chose " + rpc[computer_choice] + ", You lose!")
                computer_score = computer_score + 1
                break

        elif player_choice.lower().strip() == 'scissors':
            if rpc[computer_choice] == 'paper':
                print("Computer chose " + rpc[computer_choice] + ", You win!")
                player_score = player_score + 1
                break
            else:
                print("Computer chose " + rpc[computer_choice] + ", You lose!")
                computer_score = computer_score + 1
                break

print('___Thanks for Playing!!!___')
print('--- Scoreboard ---')
print(player_name + ' - ' + str(player_score))
print('Computer - ' + str(computer_score))
print('Draw - ' + str(draw_score))            
                