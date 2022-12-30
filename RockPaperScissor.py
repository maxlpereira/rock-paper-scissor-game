import random

def rockpaperscissor():   
    
    r = 'rock'
    p = 'paper'
    s = 'scissor'
    
    choices = [r, p, s]
    
    user_choice = input(f'Please, select {r}, {p} or {s}: ')
    if user_choice not in choices:
        return 'Invalid input'
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        return 'Tie \U0001F91D'
    elif ((user_choice == r and computer_choice == s) or (user_choice == p and computer_choice == r) or (user_choice == s and computer_choice == p)):
        return f'You choose {user_choice} and I choose {computer_choice}, then you won \U0001F973'
    else:
        return f'You choose {user_choice} and I choose {computer_choice}, then you lose \U0001F480'
    
while True:
    print(rockpaperscissor())
    a = input('Let\'s play again? (Yes/No): ')
    if a == "No" or a == "no":
        break
    else:
        continue