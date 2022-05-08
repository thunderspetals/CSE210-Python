'''
Project: Tic Tac Toe
Author: Annaleisa Perry

Game Rules:
The ninja will drop da bomb on the target drop inside the game grid. Then the next ninja will show their skills.x

-player one uses x's and player two uses o's
-players take turns adding a mark
-first to get 3 in a row vertically, horizontally, or diagonally wins
-if no 3 in a row, it is a draw.

'''

def main():
    whos_da_ninja_now = your_turn("")
    gameGrid = create_gameGrid()
    while not (game_won(gameGrid) or blackout(gameGrid)):
        display_gameGrid(gameGrid)
        ninja_bomb(whos_da_ninja_now, gameGrid)
        whos_da_ninja_now = your_turn(whos_da_ninja_now)
    display_gameGrid(gameGrid)
    print("That was fun! Let's play again!") 

def create_gameGrid():
    gameGrid = []
    for targetDrop in range(9):
        gameGrid.append(targetDrop + 1)
    return gameGrid

def display_gameGrid(gameGrid):
    print()
    print(f"{gameGrid[0]}|{gameGrid[1]}|{gameGrid[2]}")
    print('-----')
    print(f"{gameGrid[3]}|{gameGrid[4]}|{gameGrid[5]}")
    print('-----')
    print(f"{gameGrid[6]}|{gameGrid[7]}|{gameGrid[8]}")
    print()
    
def blackout(gameGrid):
    for targetDrop in range(9):
        if gameGrid[targetDrop] != "x" and gameGrid[targetDrop] != "o":
            return False
    return True 
    
def game_won(gameGrid):
    return (gameGrid[0] == gameGrid[1] == gameGrid[2] or
            gameGrid[3] == gameGrid[4] == gameGrid[5] or
            gameGrid[6] == gameGrid[7] == gameGrid[8] or
            gameGrid[0] == gameGrid[3] == gameGrid[6] or
            gameGrid[1] == gameGrid[4] == gameGrid[7] or
            gameGrid[2] == gameGrid[5] == gameGrid[8] or
            gameGrid[0] == gameGrid[4] == gameGrid[8] or
            gameGrid[2] == gameGrid[4] == gameGrid[6])

def ninja_bomb(whos_da_ninja_now, gameGrid):
    targetDrop = int(input(f"Please choose a targetDrop for da bomb {whos_da_ninja_now} ninja (1-9): "))
    gameGrid[targetDrop - 1] = whos_da_ninja_now

def your_turn(spot_for_drop):
    if spot_for_drop == "" or spot_for_drop == "o":
        return "x"
    elif spot_for_drop == "x":
        return "o"

if __name__ == "__main__":
    main()