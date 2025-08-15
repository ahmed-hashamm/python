import random
def roll_dice():
    val1 = random.randint(1,6) 
    val2 = random.randint(1,6)
    return (val1, val2)
    

def main():
    while True: 
        user_input = input("Do you want to roll the dice? (y/n): ").strip().lower()
        
        if user_input == "n":
            print("Thank you for playing!")
            break  # Exit the loop/game
        elif user_input == "y":
            dice_values = roll_dice()
            print(f"You rolled: {dice_values}")
        else:
            print("Invalid input! Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()