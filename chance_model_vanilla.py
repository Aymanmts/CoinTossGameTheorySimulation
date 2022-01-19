#%%Import Libraries
import numpy as np
import random as r
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys
from tqdm import tqdm


#%% Initialize

class PlayGames():

    def __init__(self):
        self.gameends = [] #initialize list to track number of rounds played at the end of every game
        self.games_to_play = None #initialize number of times to simulate
        self.maximum_rounds = 10000000 #per game set the maximum number of rounds
        self.payoutA = [] #initialize list to track Player A's payout at the end of of every game
        self.payoutB = [] #initialize list to track Player B's payout at the end of of every game
        self.payoutH = [] #initialize list to track the house's payout at the end of of every game

        self.initialpot = None #Initialize the initial house pot size
        self.playerpot = None #Initialize the initial player pot size

        self.game_type = None #Initialize the announcments txt file
        self.dist_type = None #Initialize the summary pdf file

    def play(self):
        self.game_type = '''Outputs/Vanilla_Model/Announcements_NumGames-{}_InitialPlayerPotSize-{}_InitalHousePot-{}.txt'''.format(self.games_to_play,self.playerpot,self.initialpot) #Create logging (announcments) file
        self.dist_type = '''Outputs/Vanilla_Model/Rounds_Distribution_NumGames-{}_InitialPlayerPotSize-{}_InitalHousePot-{}.pdf'''.format(self.games_to_play,self.playerpot,self.initialpot) #Create distribution summary pdf

        self.games_to_play = int(self.games_to_play)
        self.games_to_play = self.games_to_play + 1


        file = open(self.game_type, "w")

        for trials in tqdm(range(1,self.games_to_play)): #Set number of games to play
            print("\nTrial: ",trials, file = file) #Print trial name
            PlayerAPot = self.playerpot # Player A's initial pot
            PlayerBPot = self.playerpot # Player B's initial pot
            Pot=self.initialpot # House initial pot

            gameover = "No" # Set iniital condition that keeps each individual game running.

            for rounds in range(1,(self.maximum_rounds+1)): # set the maximum number of rounds a game will go on for

                    if gameover == "No": # Check if the game is still active and initiate the following loop.

                        print("\n Round: ",rounds, file = file) # Announce the start of a round

                        PlayerA_Roll = r.randint(1,6) # Player A rolls a 6 sided die and obtains a score
                        print("Player A Rolls: ",PlayerA_Roll, file = file) # Announce the roll player A got

                        # Set the payoffs for Player A based on the outcome of their roll

                        #If player rolls a 1 - nothing happens
                        if PlayerA_Roll == 1:
                            Pot = Pot-0
                            PlayerAPot = PlayerAPot

                        #If player rolls a 2 - they recieve eveything from the pot
                        elif PlayerA_Roll == 2:
                            PlayerAPot = PlayerAPot + Pot
                            Pot = Pot - Pot

                        #If player rolls a 3 - they recieve half the value of the pot (rounded down)
                        elif PlayerA_Roll == 3:
                            PlayerAPot = PlayerAPot + math.floor(Pot*0.5)
                            Pot = Pot - math.floor(Pot*0.5)

                        #If player rolls a 4, 5, 6 and they have at least 1 item to give - they give 1 item to the pot
                        elif (PlayerA_Roll == 4 or PlayerA_Roll == 5 or PlayerA_Roll == 6) and PlayerAPot>0:
                            PlayerAPot = PlayerAPot - 1
                            Pot = Pot + 1

                        #If they have nothing to give the game is over
                        else:
                            gameover = "Yes"
                            print("Is the game over ",gameover,file=file)
                            self.gameends.append(rounds) #Track which round the game ended
                            self.payoutA.append(PlayerAPot) #Track Player A's payout at the end of the game
                            self.payoutB.append(PlayerBPot) #Track Player B's payout at the end of the game
                            self.payoutH.append(Pot) #Track the house's payout at the end of the game

                        print("\t Player A's Pot", PlayerAPot, file = file) #At the end of player A's roll announce their pot
                        print("\t Player B's Pot", PlayerBPot, file = file) #At the end of player A's roll announce player B's pot
                        print("\t Collective Pot", Pot, file = file) #At the end of player A's roll announce the house pot
                        print("\t Is Game Over after A moves?", gameover, file = file) #Announce if the game is over
                        print("\t number of games played so far:",len(self.gameends), file = file) #At the end of player A's roll announce which round the game is still on



                        if gameover == "No": # After Player A rolls check if the game is still active and initiate the following loop.

                            PlayerB_Roll = r.randint(1,6) # Player B rolls a 6 sided die and obtains a score
                            print("Player B Rolls: ",PlayerB_Roll, file = file) # Announce the roll player B got

                        #If player rolls a 1 - nothing happens
                            if PlayerB_Roll == 1:
                                Pot = Pot-0
                                PlayerBPot = PlayerBPot

                         #If player rolls a 2 - they recieve eveything from the pot
                            elif PlayerB_Roll == 2:
                                PlayerBPot = PlayerBPot + Pot
                                Pot = Pot - Pot

                        #If player rolls a 3 - they recieve half the value of the pot (rounded down)
                            elif PlayerB_Roll == 3:
                                PlayerBPot = PlayerBPot + math.floor(Pot*0.5)
                                Pot = Pot - math.floor(Pot*0.5)

                        #If player rolls a 4, 5, 6 and they have at least 1 item to give - they give 1 item to the pot
                            elif (PlayerB_Roll == 4 or PlayerB_Roll == 5 or PlayerB_Roll == 6) and PlayerBPot>0:
                                PlayerBPot = PlayerBPot - 1
                                Pot = Pot + 1

                            else:
                                gameover = "Yes"
                                print("Is the game over ",gameover,file = file)
                                self.gameends.append(rounds)
                                self.payoutA.append(PlayerAPot) #Track Player A's payout at the end of the game
                                self.payoutB.append(PlayerBPot) #Track Player B's payout at the end of the game
                                self.payoutH.append(Pot) #Track the house's payout at the end of the game

                            print("\t Player A's Pot", PlayerAPot, file = file) #At the end of player B's roll announce their pot
                            print("\t Player B's Pot", PlayerBPot, file = file) #At the end of player B's roll announce player A's pot
                            print("\t Collective Pot", Pot, file = file) #At the end of player B's roll announce the house pot
                            print("\t Is Game Over after B moves?", gameover, file = file) #Announce if the game is over
                            print("\t number of games played so far:",len(self.gameends), file = file) #At the end of player B's roll announce which round the game is still on
                        else:
                            break

                    else:
                        break
            #print(self.gameends) # At the end of each game trial output the list of game trials played so far and the rounds each of them ended at

        #Descriptive Stats

        print("number of games played:", len(self.gameends), file = file)
        print("size of initial player pot:", self.playerpot, file = file)
        print("size of initial house pot:", self.initialpot, file = file)
        print("\naverage number of rounds the game lasts for:", round(np.mean(self.gameends),2), file = file)
        print("variance of the number of rounds the game lasts for:", round(np.var(self.gameends),2), file = file)
        print("maximum number of game rounds in the distribution:", np.max(self.gameends), file = file)
        print("minimum number of game rounds in the distribution:", np.min(self.gameends), file = file)


        print("\naverage payout for Player A $:", round(np.mean(self.payoutA),2), file = file)
        print("variance of the payout for Player A $:", round(np.var(self.payoutA),2), file = file)
        print("maximum payout for Player A in the distribution $:", np.max(self.payoutA), file = file)
        print("minimum payout for Player A in the distribution $:", np.min(self.payoutA), file = file)

        print("\naverage payout for Player B $:", round(np.mean(self.payoutB),2), file = file)
        print("variance of the payout for Player B $:", round(np.var(self.payoutB),2), file = file)
        print("maximum payout for Player B in the distribution $:", np.max(self.payoutB), file = file)
        print("minimum payout for Player B in the distribution $:", np.min(self.payoutB), file = file)

        print("\naverage payout for House $:", round(np.mean(self.payoutH),2), file = file)
        print("variance of the payout for House $:", round(np.var(self.payoutH),2), file = file)
        print("maximum payout for House in the distribution $:", np.max(self.payoutH), file = file)
        print("minimum payout for House in the distribution $:", np.min(self.payoutH), file = file)

    def plot(self):
        
        with PdfPages(self.dist_type) as pdf:

            # Build out pdf summary
            txt = ''' \nNumber of games played:{}
            size of initial player pot: {}
            size of initial house pot: {}
            \naverage number of rounds the game lasts for: {}
            variance of the number of rounds the game lasts for: {}
            maximum number of game rounds in the distribution: {}
            minimum number of game rounds in the distribution: {}'''.format(len(self.gameends),self.playerpot,self.initialpot,round(np.mean(self.gameends),2),round(np.var(self.gameends),2),np.max(self.gameends),np.min(self.gameends))

            ys = self.gameends
            l = len(ys)
            xs = [x+1 for x in range(0,l)]

            fig = plt.figure(figsize=(16,25))
            plt.plot(xs, ys)
            plt.xlabel('Number of Games')
            plt.ylabel('Number of Rounds')
            plt.title('Distribution of Rounds Over Multiple Games')
            plt.text(0.05,0.95,txt, transform=fig.transFigure,size=10)
            pdf.savefig()
            plt.close()

            txt = ''' \nNumber of games played:{}
            average payout for Player A: ${}
            variance of the payout for Player A: ${}
            maximum payout for Player A in the distribution  ${}
            minimum payout for Player A in the distribution ${}'''.format(len(self.payoutA),round(np.mean(self.payoutA),2),round(np.var(self.payoutA),2),np.max(self.payoutA),np.min(self.payoutA))

            ys = self.payoutA
            l = len(ys)
            xs = [x+1 for x in range(0,l)]

            firstPage = plt.figure(figsize=(16,16))
            firstPage.clf()
            plt.plot(xs, ys)
            plt.xlabel('Number of Games')
            plt.ylabel('Payout ($)')
            plt.title('''Player A's Payout Over Multiple Games''')
            firstPage.text(0.05,0.95,txt, transform=firstPage.transFigure,size=10)
            pdf.savefig()
            plt.close()

            txt = ''' \nNumber of games played:{}
            average payout for Player B: ${}
            variance of the payout for Player B: ${}
            maximum payout for Player B in the distribution ${}
            minimum payout for Player B in the distribution ${}'''.format(len(self.payoutB),round(np.mean(self.payoutB),2),round(np.var(self.payoutB),2),np.max(self.payoutB),np.min(self.payoutB))

            ys = self.payoutA
            l = len(ys)
            xs = [x+1 for x in range(0,l)]

            secondPage = plt.figure(figsize=(16,16))
            secondPage.clf()
            plt.plot(xs, ys)
            plt.xlabel('Number of Games')
            plt.ylabel('Payout ($)')
            plt.title('''Player B's Payout Over Multiple Games''')
            secondPage.text(0.05,0.95,txt, transform=secondPage.transFigure,size=10)
            pdf.savefig()
            plt.close()

            txt = ''' \nNumber of games played:{}
            average payout for House: ${}
            variance of the payout for House: ${}
            maximum payout for House in the distribution ${}
            minimum payout for House in the distribution ${}'''.format(len(self.payoutH),round(np.mean(self.payoutH),2),round(np.var(self.payoutH),2),np.max(self.payoutH),np.min(self.payoutH))

            ys = self.payoutA
            l = len(ys)
            xs = [x+1 for x in range(0,l)]

            thirdPage = plt.figure(figsize=(16,16))
            thirdPage.clf()
            plt.plot(xs, ys)
            plt.xlabel('Number of Games')
            plt.ylabel('Payout ($)')
            plt.title('''House's Payout Over Multiple Games''')
            thirdPage.text(0.05,0.95,txt, transform=thirdPage.transFigure,size=10)
            pdf.savefig()
            plt.close()
#%%
if __name__ == '__main__':
    while True:
        try:
            games = input("How many games would you like to simulate?\n(please note any iterations over 100,000 will lead to a big announcments file) ")
            games = int(games)

            ppot = input("Size of each player's pot?")
            ppot = int(ppot)

            hpot = input("Size of house pot?")
            hpot = int(hpot)

        except ValueError:
            print("ERROR - Please check to see if you inputted valid integer number.")
            continue
        else:
            break


    start = PlayGames()


    start.games_to_play = games
    start.playerpot = ppot
    start.initialpot= hpot
    print("Simulating Games ...")

    start.play()

    stroutput = '''\nOutputting game announcments - please refer to {} for an exciting play by play of the games. NO TIVO NEEDED!'''.format(start.game_type)

    print(stroutput)


    start.plot()
    stroutput = '''\nOutputting summarized outputs to a PDF - please refer to {} for some wacky graphs'''.format(start.dist_type)
    print(stroutput)

#%%
