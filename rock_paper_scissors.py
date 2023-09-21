import random
def play_game():
    elements = ['rock','paper','scissors']
    
    play = True
    
    print('''****** WELCOME TO ROCK PAPER SCISSORS😋😎******
                    READY
                    SET
                    GO!!!''')
    
    print('''SCORES ARE COUNTED AS COMPUTER_SCORE : PLAYER_SCORE''')
    computer_score = 0
    player_score = 0
    while play :
        computer_input = random.choice(elements)
        player = input('(rock/paper/scissors) or quit ? = ')
        if computer_input==player:
            print('TIE!')
            print(f'SCORE: {computer_score}:{player_score}')
        elif player=='rock':
            if computer_input=='paper':
                print('YOUR LOSE!')
                computer_score+=1
                print(f'SCORE: {computer_score}:{player_score}')
            else:
                print('YOU WIN!')
                player_score+=1
                print(f'SCORE: {computer_score}:{player_score}')
        elif player=='paper':
            if computer_input=='rock':
                print('YOU WIN!')
                player_score+=1
                print(f'SCORE: {computer_score}:{player_score}')
            else:
                print('YOU LOSE!')
                computer_score+=1
                print(f'SCORE: {computer_score}:{player_score}')
        elif player=='scissors':
            if computer_input=='rock':
                print('YOU LOSE!')
                computer_score+=1
                print(f'SCORE: {computer_score}:{player_score}')
            else:
                print('YOU WIN!')
                player_score+=1
                print(f'SCORE: {computer_score}:{player_score}')
        elif player=='quit':
            print("IF YOU WANT TO PLAY AGAIN TYPE  'play_game()'  ")
            break
        else:
            print('YOU ENTERED AN INVALID TURN.PLEASE CHECK SPELLING!')
            continue

print("IF YOU ARE READY TO PLAY ROCK/PAPER/SCISSORS TYPE 'play_game()'")

            
    
    