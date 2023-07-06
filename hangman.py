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
