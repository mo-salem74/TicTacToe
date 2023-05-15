import time
#TIC TAC TOE w/both modes working
import Func_Def

win_condition = None
repeater = ''
win_counter1 = 0
win_counter2 = 0

Func_Def.intro()

while repeater.lower() != 'n':
    # Game mode select
    gameMode = Func_Def.game_mode_select()
    
    #Multiplayer
    if gameMode == '1':
        print(f"\t\tWELCOME TO PVP MODE, LET'S START")

        name1 = Func_Def.get_name1()
        Func_Def.name_list1.append(name1)
            
        name2 = Func_Def.get_name2()
        Func_Def.name_list2.append(name2)
            
        Func_Def.display_board()
        
        for turns in range(9):
            Func_Def.main_sequence(Func_Def.player_switcher(), name1, name2)
            win_condition = Func_Def.winner_checker()
            
            if win_condition == True:
                # if player1 won
                if Func_Def.player_switcher() == 1:
                    print(f'{name1} wins!!\n')
                    Func_Def.score_board1.append(1)
                    Func_Def.score_board2.append(0)
                    win_counter1 += 1
                # if player2 won
                elif Func_Def.player_switcher() == 2:
                    print(f'{name2} wins!!\n')
                    Func_Def.score_board1.append(0)
                    Func_Def.score_board2.append(1)
                    win_counter2 += 1
                
                
                break
            Func_Def.turnCounter += 1
        else:
            print("It's a Tie  ¯\_(ツ)_/¯ ")
            Func_Def.score_board1.append(0)
            Func_Def.score_board2.append(0)

    #Single player        
    elif gameMode == '2':
        print(f"\tWELCOME TO SINGLE PLAYER MODE, SHALL YOU DO THE HONORS?")
        name1 = Func_Def.get_name1()
        Func_Def.name_list1.append(name1)
        
        name2 = "Steve the AI"
        Func_Def.name_list2.append(name2)
        Func_Def.display_board()
        for turns in range(9):
            Func_Def.single_player_sequence(Func_Def.player_switcher(),name1)
            win_condition = Func_Def.winner_checker()
            if win_condition == True:
                #if player 1 won
                if Func_Def.player_switcher() == 1:
                    print(f"{name1} wins!!")
                    Func_Def.score_board1.append(1)
                    Func_Def.score_board2.append(0)
                # if AI won
                else:
                    print(f"Steve the AI wins!!")
                    Func_Def.score_board1.append(0)
                    Func_Def.score_board2.append(1)
                break
            Func_Def.turnCounter += 1
        else:
            print("It's a Tie  ¯\_(ツ)_/¯ ")
            Func_Def.score_board1.append(0)
            Func_Def.score_board2.append(0)
            
    Func_Def.Score_Board_display(name1,name2)
    time.sleep(1)
    print("\n\nDo you wanna play again?")
    repeater = input("Enter N to stop\n\t->")
    Func_Def.board = [' 1 ',' 2 ',' 3 ',' 4 ',' 5 ',' 6 ',' 7 ',' 8 ',' 9 ']
    Func_Def.turnCounter = 1



print("\t\t\t    Hope to cya soon!")
