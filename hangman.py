import random

def get_random_word():
    word_list = ["apple", "banana", "cherry", "dragonfruit", "elderberry", "fig", "grapefruit", "honeydew", "kiwi",
                 "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine",
                 "watermelon"]
    return random.choice(word_list)

def display_hangman(tries):
    stages = [  # Final state: Head, torso, both arms, and both legs
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # Head, torso, both arms, and one leg
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # Head, torso, both arms
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # Head, torso, one arm
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # Head and torso
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # Head
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # Initial empty state
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play_hangman():
    word = get_random_word().upper()
    word_letters = set(word)
    guessed_letters = set()
    incorrect_letters = set()
    tries = 6

    print("Welcome to Hangman!")
    print("Guess the word by guessing one letter at a time.")
    print("You have 6 tries to save the hangman!")
    print()

    while True:
        # Display the hangman and guessed letters
        print(display_hangman(tries))
        print("Guessed letters:", ' '.join(sorted(guessed_letters)))
        print()

        # Display the current word progress
        word_progress = ''.join(letter if letter in guessed_letters else '_' for letter in word)
        print("Word:", word_progress)
        print()

        # Get user input
        guess = input("Enter a letter: ").upper()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again!")
            continue

        if guess.isalpha() and len(guess) == 1:
            guessed_letters.add(guess)

            if guess in word_letters:
                print("Good guess!")
                if set(word_progress) == word_letters:
                    print("Congratulations! You've guessed the word:", word)
                    break
            else:
                print("Oops! That letter is not in the word.")
                incorrect_letters.add(guess)
                tries -= 1

                if tries == 0:
                    print(display_hangman(tries))
                    print("Sorry, you've run out of tries!")
                    print("The word was:", word)
                    break
        else:
            print("Invalid input. Please enter a single letter.")

        print()

play_hangman()
                
