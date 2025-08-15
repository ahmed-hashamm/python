#ask for user move
#if valid move 
    #genrate cpu move
    #compare both moves
    #define rules
    #if user wins -> winnig message and ask to play again
    #if user loses -> loosing message //

import random
playing = True
Rock = 'R'
Scissors = 'S'
Paper = 'P'
emojis = {Rock : '🪨' , Scissors : '✂️' , Paper : '📃'}
moves = tuple(emojis.keys())
def get_user_move():
    while True:
        user_move = input("Make a move [R/P/S] : ").upper().strip()
        if user_move  in moves:
            return user_move
        else:
            print("invalid move")

def display_choices(user_move, cpu_move):
    print(f"Your choice : {emojis[user_move]}")
    print(f"Cpu choice : {emojis[cpu_move]}")    

def determine_winner(user_move, cpu_move):
        if user_move == cpu_move:
            print(f"its a draw")
        elif (
            (user_move == Rock and cpu_move == Paper) or 
            (user_move == Paper and cpu_move == Scissors) or
            (user_move== Scissors and cpu_move == Rock)):
            print("You loose")
        else:
            print("You win")
                
def play_game():
    while playing:

        user_move = get_user_move()

        cpu_move = random.choice(moves)

        display_choices(user_move,cpu_move)

        determine_winner(user_move, cpu_move)

        should_continue = input("Continue ? [y/n] :").lower()
        if should_continue == 'n':
            break  


play_game()