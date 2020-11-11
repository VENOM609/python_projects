# printing of the sudoku board to the console
import numpy as np

board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]
# print(np.matrix(board))
# print(len(board))
def print_board(bo):
    
    for i in range(len(bo)):
        if i % 3 == 0 and  i !=0:
            print('- - - - - - - - - - -')

        for  j in range(len(bo)):
            if j % 3 == 0 and j !=0:
                print('|', end=" ")
            if j == 8:
                print(bo[i][j])
            else:
                print(bo[i][j], end=" ")

def find_empty(bo):
    # empty = []
    for x in range(len(bo)):
        for y in range(len(bo)):
            if bo[x][y] == 0:
                return (x ,y)
                return True

    # to see the empty positions in the board
    #             empty.append([i,j])
    # return empty
                


# print(find_empty(board))

#print(find_empty(board))

def valid(bo, x , y , num):
    for i in range(len(bo)):
        if bo[x][i] == num:
            return False
    for i in range(len(bo)):
        if bo[i][y] == num:
            return False

    x0_box = (x//3)*3
    y0_box = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if bo[x0_box+i][y0_box+j] == num:
                return False

    return True

#valid(board, 0, 2, 5 )

def solve(bo):
    # print_board(bo)...............................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................
    found = find_empty(bo)
    if not found:
        return True
    else:
        x, y = found

    for num in range(1,10):
            if valid(bo,x, y, num):
                bo[x][y] = num
                if solve(bo):
                    return True
                    
                bo[x][y]= 0
    return
    
print_board(board)
print('========================')
solve(board)
print_board(board)