import random

PASSWORD = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
            'w', 'x', 'y', 'z']


def crack_password(user_pass):
    guess = ""
    while (guess != user_pass):
        guess = ""
        for letter in range(len(user_pass)):
            r_letter = random.choice(PASSWORD)
            guess = guess + r_letter
    print(f"Found guess {guess}")
    return guess
    