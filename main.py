def game():
    high = 100
    low = 1
    guesses_needed = 0
    answer = None
    
    while answer != "correct":
        guess = (high + low) // 2
        guesses_needed += 1
        
        answer = input(f"Is the number you're thinking of {guess}? (Enter 'higher', 'lower' or 'correct): ").lower()
        if answer not in {"higher", "lower", "correct"}:
            print("Please enter 'higher', 'lower' or 'correct': ")
        elif answer == "correct":
                if guesses_needed == 1:
                    guess_text = "guess."
                else: 
                    guess_text = "guesses."
                print(f"Great! I guessed your number {guess} with {guesses_needed} {guess_text}")
        elif answer == "higher":
            low = guess + 1
        elif answer == "lower":
            high = guess - 1

if __name__ == "__main__":
    game()