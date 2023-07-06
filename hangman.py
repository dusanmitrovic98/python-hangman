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
