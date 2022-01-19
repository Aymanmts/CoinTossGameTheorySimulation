# Coin Toss Game Theory Simulation
This is a fun little Monte Carlo based simulation program, I built during my Simulation class at Georgia Tech.

The parameters setup for this simulation are that there are 3 entities Player A, Player B, and a Collective Pot (House).

Player A and B have the agency to roll a 6-sided dice each. Based on the value born from each roll, the players must either contribute to the house pot, take from the pot, or do nothing. The players act sequentially, with the game only ending after any one of the players is not able to contribute to the pot anymore. I took this premise and, inspired by game theoretic repeated games, added to it by enabling cheating in the games with the possibility to play repeated games with player memory induced or forgotten between games.

The key areas we want to study here are the expected number and distribution of cycles the game will last for. More generally we want to program a way to simulate this game and make it available to use so that other interested parties can also understand these in a packaged format. To that effect, I have developed 3 scripts where a user is able to simulate these games and obtain both detailed and summarized outputs. The simulation scripts cover a few variations. Included in the package are:
  - Simulations related to the initial problem described in the question document with an option for the user to choose their own initial player and house pots (hereby referred to as the vanilla algorithm).

  - Simulations related to extensions of the vanilla game inspired by game theory. In this variation a player will potentially cheat and get caught with a certain probability value set by the user. In these games a player can cheat, to obtain a higher payout, but if caught they will be punished with a penalty and the game will end. Players however can continue to play in subsequent games under this simulation (hereby referred to as the memory-less algorithm). The user can define the size of the initial player and house pot along with the probability of getting caught.

  - Simulations identical to the aforementioned memory-less games, except in these simulations if the player gets caught, they are no longer able to play in subsequent games (hereby referred to as memory-induced games).

## Description.

  This Readme will help you run the simulation scripts developed to explore the interaction between two players engaged in a game of chance with predefined payouts, with extension scripts inspired by game theory where players cheat in repeated memory-less and memory-induced games.

## Setup.

  Install Dependencies:

  Navigate to Dependencies folder. Example command cd Dependencies
  Run the following statement to install your relevant python libraries to run the project:
	pip install -r requirements.txt

## Run the simulation wrapper script.
  To run the simulation scripts run the following commands from the home directory:
	1. Use this to move from the Dependencies folder to the home folder
    		cd ..
    	2. Use this command to run the script
		python run.py


## Description of files
	1. run.py - Main wrapper script to run the user's choice of simulation programs
	2. chance_model_vanilla.py - Simulation program based on the description given in the question paper.
	3. chance_model_with_cheat_memoryless.py - Simulation program with an extension that enables player cheating in memory less games.
	4. chance_model_with_cheat_memory.py - Simulation program with an extension that enables player cheating in a 1 shot game if cheating is discovered.
	5. Dependencies folder - stores python requirements.txt for recreation of program
	6. Outputs folder - Stores the outputs of the models along with some appendix simulations run by me for reference.
