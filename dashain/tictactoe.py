import random
board=[]
row=[]

def show():
    for i in board:
        print(' '.join(row))    
   
    
def filled():    
    for row in board:
        for item in row:
            if item == '_':
                return False
    return True

def win(player):
    win=None
    n=len(board)
    for i in range(n):
        win=True
        for j in range(n):
            if board[i][j]!=player:
                win=False
                break
        if win:
            return win
    for i in range(n):
        win=True
        for j in range(n):
            if board[j][i]!=player:
                win =False
                break
            if win:
                return win
    win=True
    for i in range(n):
        if board[i][i]!=player:
            win=False
            break
    if win:
        return win
    win=True
    for i in range(n):
        if board[i][n-1-i]!=player:
            win = False
            break
    if win:
        return win
    return False
 
def start():
    for i in range(3):
        for j in range(3):
        row.append("_")
        board.append(row)
    a=random.randint(0,1)
    player='X' if a==1 else 'O' 
    while True:
        print(f"Player {player} turn.")
        show()
        r,c=list(map(int,input("Enter row and column number to fix spot:").split()))
        print()
        board[r][c]=player
        if win(player):
            print(f"Player {player} wins the game!")
            break
        if filled():
            print("Match Draw.")
            break
        player="X" if player =="O" else "O"
    print()
    show()

        
start()