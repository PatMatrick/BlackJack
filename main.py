###HELLO
import time



cards = {"Ace_Club": 10, "Ace_Heart": 10, "Ace_Spade": 10, "Ace_Diamond": 10, "King_Club": 10, "King_Heart": 10,
         "King_Spade": 10, "King_Diamond": 10, "Queen_Club": 10, "Queen_Heart": 10, "Queen_Spade": 10, "Queen_Diamond": 10,
         "Jack_Club": 10, "Jack_Heart": 10, "Jack_Spade": 10, "Jack_Diamond": 10, "10_Club": 10, "10_Heart": 10, "10_Spade": 10,
         "10_Diamond": 10, "9_Club": 9, "9_Heart": 9, "9_Spade": 9, "9_Diamond": 9, "8_Club": 8, "8_Heart": 8,
         "8_Spade": 8, "8_Diamond": 8, "7_Club": 7, "7_Heart": 7, "7_Spade": 7, "7_Diamond": 7, "6_Club": 6, "6_Heart": 6,
         "6_Spade": 6, "6_Diamond": 6, "5_Club": 5, "5_Heart": 5, "5_Spade": 5, "5_Diamond": 5, "4_Club": 4,
         "4_Heart": 4, "4_Spade": 4, "4_Diamond": 4, "3_Club": 3, "3_Heart": 3, "3_Spade": 3, "3_Diamond": 3,
         "2_Club": 2, "2_Heart": 2, "2_Spade": 2, "2_Diamond": 2}

class Player:
    def __init__(self, name):
        self.currentscore = 0
        self.chips = 0
        self.wins = 0

class Computer:
    def __init__(self, name):
        self.currentscore = 0
        self.chips = 0
        self.wins = 0



def startup():
    print("Enter your name to begin.")
    option = input("->")
    global PlayerIG
    global ComputerIG
    PlayerIG = Player(option)
    ComputerIG = Computer
    game()

def start():
    print("Hello and welcome to Blackjack!")
    print("1.) Begin game")
    print("2.) Quit")
    option = input("-> ")
    if option.strip() == "1":
        startup()
    if option.strip() == "2":
        sys.exit()


def game():
    print("Player Wins: " + str(PlayerIG.wins))
    print("Player Chips: " + str(PlayerIG.chips))
    print("\n")
    print("Computer Wins: " + str(ComputerIG.wins))
    print("Computer Chips: " + )

start()