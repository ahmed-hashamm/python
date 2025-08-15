import random
def main():
    playing = True
    cpu_num = random.randint(1,100)
    while playing:
        user_guess = input("Guess a number bw 1-100 : ")
        if not user_guess.isdigit():
            print("invalid input")
            continue
        user_guess = int(user_guess)
        if user_guess < 1 or user_guess > 100:
            print("invalid number")
            continue
        if user_guess > cpu_num:
                print("Too high!")
        elif user_guess < cpu_num:
            print("Too Low!")
        else:
            print(f"You guessed correct!\nThe number is {cpu_num}")
            playing = False
            
if __name__ == "__main__":
    main()

