#Rock Paper Scissors game
from random import randint
playing = input('Would you like to play Rock Paper Scissors? yes or no\n').lower()
if playing[0] == 'y':
    times = input('How many times would you like to play?\n')
    counter = int(times)
    final_score = 0
    while counter >= 1:
        pdecision = input('Choose Rock, Paper, or Scissors:\n').title()
        if pdecision == 'Quit':
            break
        if pdecision:
            decision = randint(1,9)
            if decision<=3:
                decision ='Rock'
            elif decision<=6:
                decision ='Paper'
            elif decision<=9:
                decision ='Scissors'
        if decision == pdecision:
            print(f'I choose {decision} too\nIts a Tie')
        elif decision == 'Rock' and pdecision == 'Paper':
            print(f'I choose {decision}\nYou Win!!!')
            final_score += 1
        elif decision == 'Rock' and pdecision == 'Scissors':
            print(f'I choose {decision}\nYou Lose')
            final_score -= 1    
        elif decision == 'Paper' and pdecision == 'Scissors':
            print(f'I choose {decision}\nYou Win!!!')
            final_score += 1
        elif decision == 'Paper' and pdecision == 'Rock':
            print(f'I choose {decision}\nYou Lose')
            final_score -= 1
        elif decision == 'Scissors' and pdecision == 'Rock':
            print(f'I choose {decision}\nYou Win!!!')
            final_score += 1
        elif decision == 'Scissors' and pdecision == 'Paper':
            print(f'I choose {decision}\nYou Lose')
            final_score -= 1
        counter -= 1
    if final_score == 0:
        print("\nIt's a tie overall")
    elif final_score > 0:
        print('\nYou beat me... this time')
    else:
        print('\nI win :-P'*3)
else:
    print('Ok, Bye')