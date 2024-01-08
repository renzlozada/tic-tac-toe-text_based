from logo import logo, congrats
import os
import time

print(logo)
game_start = input("Please enter anything to start!")
print("Player 1 symbol: X")
print("Player 2 symbol: O")
pos = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def display_board():
    os.system('cls')
    board = f'\n' \
           f' {pos[0]} | {pos[1]} | {pos[2]} \n' \
           f'-----------\n' \
           f' {pos[3]} | {pos[4]} | {pos[5]} \n' \
           f'-----------\n' \
           f' {pos[6]} | {pos[7]} | {pos[8]} \n'
    print(board)


in_game = True
player1_turn = True
ans1 = ans2 = []
while in_game:
    display_board()
    print(f"Ans1 count: {len(ans1)}")
    print(f"Ans2 count: {len(ans2)}")
    try:
        if player1_turn:
                print("Player 1 Turn | Symbol : X")
                place1 = int(input("Please enter a number between 1-9: "))
                if place1 in ans2:
                    print("Invalid! Position taken by player 2")
                    time.sleep(2)
                else:
                    ans1.append(place1)
                    pos[place1 - 1] = "X"
                    player1_turn = False
                    
        else: # Player 2 Turn
            print("Player 2 Turn | Symbol : O")
            place2 = int(input("Please enter a number between 1-9: "))
            if place2 in ans1:
                    print("Invalid! Position taken by player 1")
                    time.sleep(2)
            else:
                ans1.append(place2)
                pos[place2 - 1] = "O"
                player1_turn = True
    except ValueError:
        print("Please enter a number only")
        time.sleep(2)
    except IndexError:
        print("Please enter a number ranging 1-9")
        time.sleep(2)        
    
    if pos[0] == pos[1] == pos[2] or pos[3] == pos[4] == pos[5] or pos[6] == pos[7] == pos[8] or \
        pos[0] == pos[3] == pos[6] or pos[1] == pos[4] == pos[7] or pos[2] == pos[5] == pos[8] or \
        pos[0] == pos[4] == pos[8] or pos[2] == pos[4] == pos[6]:
        if player1_turn:
            display_board()
            print("Player 2 won!")
            print(congrats)
            in_game = False
        else:
            display_board()
            print("Player 1 won!")
            print(congrats)
            in_game = False
    elif len(ans1) == len(pos): # TODO: Fix the draw mechanism
        print("It's a draw!")
        in_game = False