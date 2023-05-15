

    #IMPORTING LIBRARIES
import time
import random
import presentation



            ######################################################
            ######################################################

    #Functions in pre_game

#Function to present the intro
def intro():
    presentation.p_seq()
    time.sleep(1)
    print("\n\n")

#Function to select and VALIDATE the game mode
def game_mode_select():
    print("\nSelect game mode: ",end='')
    time.sleep(0.5)
    print("1- PvP",end='')
    time.sleep(0.5)
    game_mode = input("\t2- Single Player\n-> ")

    while game_mode != '1' and game_mode != '2':
        game_mode = input("\nThere are only 2 options\n 1- PvP \t2- Single Player\n->")
    return game_mode

#Function to get the names
def get_name1():
    player1_name = input("\nPlayer1 name: ")
    saluting(player1_name)
    return player1_name

def get_name2():
    player2_name = input("\nPlayer2 name: ")
    saluting(player2_name)
    return player2_name
###

#Function to salute the players
def saluting(name):
    saluting_msgs = ["Hello", "Welcome","Hey","Wassup","Hey there", "We've been expecting you","my oh py it's"]
    print(f"\n{saluting_msgs[random.randint(0, len(saluting_msgs)-1)]}, {name}\n")
    


            ######################################################
            ######################################################


    #FUNCTIONS IN PVP MODE


#Function to display the board
def display_board():
        print(f"\n\n\t{board[0]}|{board[1]}|{board[2]}\n"\
                  f"\t-  -  -  -   \n"\
                  f"\t{board[3]}|{board[4]}|{board[5]}\n"\
                  f"\t-  -  -  -   \n"\
                  f"\t{board[6]}|{board[7]}|{board[8]}\n\n")

#Function TO TAKE AND validate player's entry
#try to output "Am I supposed to guess??!"
def choice_validation():
    while True:
        try:
            playersChoice = input("Enter the box number: ")
            if playersChoice == 'steve':
                print("Steve's gonna take care of that for ya!")
                playersChoice = AIchoice_validation()
                return playersChoice
                break
            else:
                playersChoice = int(playersChoice)
                while playersChoice < 1 or playersChoice > 9 or board[playersChoice-1] == ' X ' or board[playersChoice-1] == ' O ':
                    print("WoAhh, you gotta stick to the rules!")
                    playersChoice = int(input("Pick again!! "))
                return playersChoice
                break
        except:
            print("What is that supposed to be!??")
            print("Pick again! ")    

#Main PvP Game sequence
def main_sequence(playerNumber,name1,name2):
    if playerNumber == 1:
        print(f"{name1}'s turn.\nGO!")
    else:
        print(f"{name2}'s turn.\nGO!")
    print("\nWhere do you want to play?")
    playersChoice = choice_validation()
    board[(playersChoice-1)] = avatar[playerNumber-1]
    display_board()


#Function to switch players after each turn
def player_switcher():
        if turnCounter % 2 == 0:
            playerNumber = 2
        else:
            playerNumber = 1
        return playerNumber

#Function that checks if any player achieved a win condition after each turn
def winner_checker():
        if board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8]\
           or board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8]\
           or board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
            winner = True
            return winner


            ######################################################
            ######################################################

    #FUNCTIONS IN SP MODE
        
#Main single player game sequence 
def single_player_sequence(playerNumber,name):
    if playerNumber == 1:
        print(f"{name}, GO")
        print("\nWhere do you want to play?")
        playersChoice = choice_validation()
    else:
        print("Steve the AI, GO!")
        playersChoice = AIchoice_validation()
    board[(playersChoice-1)] = avatar[playerNumber-1]
    display_board()



#Function to randomly choose and validate a box
def AIchoice_validation():
    print("chooosing...")
    time.sleep(1.5)
    while True:
        try:
            choice = random.randint(1, 9)
            while choice < 1 or choice > 9 or board[choice-1] ==  ' X ' or board[choice-1] == ' O ':
                choice = random.randint(1, 9)
            return choice
            break
        except:
            None        

            ######################################################
            ######################################################
        



def Score_Board_display(name1,name2):
    total1 = 0
    total2 = 0
    dash = '-'
    counter = 1
    
    
    if name1[0] != name2[0]:
        print("\t\t\t    .Score Board.\n")
        
        for score in range(len(score_board1)):
            print(f"\t\t\t          | {name_list1[score][0].upper()} | {name_list2[score][0].upper()} |\n\t\t\t{dash*20}")
            print(f"\t\t\t|Game #{counter}  | {score_board1[score]} | {score_board2[score]} |\n\t\t\t{dash*20}")
            total1 += score_board1[score]
            total2 += score_board2[score]
            counter += 1
        print(f"\t\t\t|Total    | {total1} | {total2} |\n\t\t\t{dash*20}")

    

    else:
        print("\t\t\t     .Score Board.\n")
        
        for score in range(len(score_board1)):
            print(f"\t\t\t          | {name1[0].upper()} | {name2[0].lower()} |\n\t\t\t{dash*20}")
            print(f"\t\t\t|Game #{counter}  | {score_board1[score]} | {score_board2[score]} |\n\t\t\t{dash*20}")
            total1 += score_board1[score]
            total2 += score_board2[score]
            counter += 1
        print(f"\t\t\t|Total    | {total1} | {total2} |\n\t\t\t{dash*20}")
            
              
                  
              
        
#DEFINITIONS


board = [' 1 ', ' 2 ', ' 3 ',
         ' 4 ', ' 5 ', ' 6 ',
         ' 7 ', ' 8 ', ' 9 ']

score_board1 = []
score_board2 = []
name_list1 = []
name_list2 = []






avatar = [' X ', ' O ']

turnCounter = 1
score = 0
