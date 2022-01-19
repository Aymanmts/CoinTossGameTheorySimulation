#%%
import runpy

#%%

string = '''Hello There! What simulation game would you like to play? Please choose between the 3 simulations on offer 
      1. Vanilla Payout Game - Description: Each player is given an inital pot chosen by you, the user, based on the roll of the dice each player recieves a payout or has to contribute to the pot.
      2. Payout Game with Cheating Memory Less- Description: Same as the vanilla game except the players will cheat now if they have to contribute with an associated chance of getting caught. If they're caught they incur a fine. Games are memoryless.
      3. Payout Game with Cheating Memory- Description: Same as the memoryless except now if any player is caught cheating the other player will refuse to play with them.
      
      Please choose between options 1-3
      Enter your integer value now.
      '''

while True:
    try:
        choice = input(string)
        choice = int(choice)
    
    except ValueError:
        print("ERROR - Please check to see if you inputted a valid integer number.")
        continue
    else:
        break


def call_f(filename):

    return runpy.run_path(filename , run_name='__main__')


if choice == 1:
    res = call_f('chance_model_vanilla.py')
elif choice == 2:
    res = call_f('chance_model_with_cheat_memoryless.py')
elif choice == 3:
    res = call_f('chance_model_with_cheat_memory.py')
else:
    print('Please choose a value between 1 and 3')
