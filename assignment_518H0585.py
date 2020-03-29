import random
import sys
random.seed(518H0585)
grid=[[]]

number=[0,1,2,3,4,5,6,7,8]
# 2 standan 3x3 Latin Square
standan1= [[((j//2+1 if j%2 else 3-j//2) + i) % 3  for j in range(3)] for i in range(3)]    
standan2= [[2,1,0],[1,0,2],[0,2,1]] 

def checkGrid(grid):
  for row in range(0,9):
      for col in range(0,9):
        if grid[row][col] == 0:
            return False
  return True 
  
def permLexicographic(A):
    Lexico = []
    for p in range(6):
        p = len(A)-1
        while p>0 and A[p-1]>A[p]:
            p -= 1
        A[p:] = reversed(A[p:])
        if p>0:
            q = p
            while A[p-1]>A[q]:
                q += 1
            A[p-1], A[q] = A[q], A[p-1]
        Lexico.extend(A)
    return Lexico
# Crearte 12 Latin Square  
def Latin_Square(grid):
    a = []
    a.extend(permLexicographic(standan1))
    a.extend(permLexicographic(standan2))
    square=[]
    index=0
    r=0
    for j in range(12):
        square.append([])
        for i in range(0+r ,3+r):
            square[index].extend(a[i])
        r = r + 3
        index = index + 1
    return square
#Convertion to Base 10

def BuilSudoku(grid):
    sudoku=[]
    b = []
    b.extend(Latin_Square(grid))
    square = []
    temp = []
    row = []
    grid=[]
    random.shuffle(b)
    for i in range(0,9):
        square.append([])
        square[i].extend(b[i])
    for i in range(0,9):
        grid.append([])
        if i==2 or i==4 or i==6:
            for j in range(0,9):
                grid[i].append(2*3 + square[i][j] + 1)
        if i==1 or i==3 or i==8:
            for j in range(0,9):
                grid[i].append(2*2 + square[i][j])
        if i==0 or i==7 or i==5:
            for j in range(0,9):
                grid[i].append(2 + square[i][j] - 1) 
    for t in range(0,3):
        if t == 0:
            for j in range(0,3):
                row.append([])
                if j==0:
                    for i in range(0,3):
                        row[j].extend(grid[i][0:3]) 
                if j==1:
                    for i in range(0,3):
                        row[j].extend(grid[i][3:6])
                if j==2:
                    for i in range(0,3):
                        row[j].extend(grid[i][6:9])
        if t == 1:
            for j in range(3,6):
                row.append([])
                if j==3:
                    for i in range(3,6):
                        row[j].extend(grid[i][0:3]) 
                if j==4:
                    for i in range(3,6):
                        row[j].extend(grid[i][3:6])
                if j==5:
                    for i in range(3,6):
                        row[j].extend(grid[i][6:9])
        if t == 2:
            for j in range(6,9):
                row.append([])
                if j==6:
                    for i in range(6,9):
                        row[j].extend(grid[i][0:3]) 
                if j==7:
                    for i in range(6,9):
                        row[j].extend(grid[i][3:6])
                if j==8:
                    for i in range(6,9):
                        row[j].extend(grid[i][6:9])        
    # Swap column
    for i in range(0,9):
        temp.append([])
        if i==1:
            temp[i].extend(row[3])
        elif i==3:
            temp[i].extend(row[1])
        elif i==6:
            temp[i].extend(row[2])
        elif i==2:
            temp[i].extend(row[6])
        elif i==5:
            temp[i].extend(row[7])
        elif i==7:
            temp[i].extend(row[5])
        else:
            temp[i].extend(row[i])
    sudoku.extend(temp)
    return sudoku
def Crearte_block(grid):
    #swap column to create block
    sudoku=[]
    sudoku.extend(BuilSudoku(grid))
    block=[]
    for t in range(0,3):
        if t==0:
            for j in range(0,3):
                block.append([])
                if j==0:
                    for i in range(0,3):
                        block[j].extend(sudoku[i][0:3]) 
                if j==1:
                    for i in range(0,3):
                        block[j].extend(sudoku[i][3:6])
                if j==2:
                    for i in range(0,3):
                        block[j].extend(sudoku[i][6:9])
        if t==1:
            for j in range(3,6):
                block.append([])
                if j==3:
                    for i in range(3,6):
                        block[j].extend(sudoku[i][0:3]) 
                if j==4:
                    for i in range(3,6):
                        block[j].extend(sudoku[i][3:6])
                if j==5:
                    for i in range(3,6):
                        block[j].extend(sudoku[i][6:9])
        if t==2:
            for j in range(6,9):
                block.append([])
                if j==6:
                    for i in range(6,9):
                        block[j].extend(sudoku[i][0:3]) 
                if j==7:
                    for i in range(6,9):
                        block[j].extend(sudoku[i][3:6])
                if j==8:
                    for i in range(6,9):
                        block[j].extend(sudoku[i][6:9])
    return block

# Crearte hole
def Digginghole(n):
    grid=[]
    grid.extend(Crearte_block(grid))
    if checkGrid(grid)==True:
        if n%9==0 and n<=54:
            for j in range(0,9):
                random.shuffle(number)
                for i in range(0,n//9):
                    t=number[i]
                    grid[j].pop(t)
                    grid[j].insert(t,0)
            #return grid
        else:
            print("Invalid input")
    return grid

def print_Sudoku(n):
    grid=[]
    grid.extend(Digginghole(n))
    row=[]
    for t in range(0,3):
        if t == 0:
            for j in range(0,3):
                row.append([])
                if j==0:
                    for i in range(0,3):
                        row[j].extend(grid[i][0:3]) 
                if j==1:
                    for i in range(0,3):
                        row[j].extend(grid[i][3:6])
                if j==2:
                    for i in range(0,3):
                        row[j].extend(grid[i][6:9])
        if t == 1:
            for j in range(3,6):
                row.append([])
                if j==3:
                    for i in range(3,6):
                        row[j].extend(grid[i][0:3]) 
                if j==4:
                    for i in range(3,6):
                        row[j].extend(grid[i][3:6])
                if j==5:
                    for i in range(3,6):
                        row[j].extend(grid[i][6:9])
        if t == 2:
            for j in range(6,9):
                row.append([])
                if j==6:
                    for i in range(6,9):
                        row[j].extend(grid[i][0:3]) 
                if j==7:
                    for i in range(6,9):
                        row[j].extend(grid[i][3:6])
                if j==8:
                    for i in range(6,9):
                        row[j].extend(grid[i][6:9]) 
    return row

def main():
    paramters = sys.argv
    if paramters[1] == '9':
        with open("output.txt.","a") as f:
            q=[]
            q.extend(print_Sudoku(9))
            for i in range(0,9):
                f.write(str(q[i]).strip('[]'))
                f.write('\n')
        f.close()
    if paramters[1] =='18':
        with open("output.txt.","a") as f:
            q=[]
            q.extend(print_Sudoku(18))
            for i in range(0,9):
                f.write(str(q[i]).strip('[]'))
                f.write('\n')
        f.close()  
    if paramters[1] =='27' :
        with open("output.txt.","a") as f:
            q=[]
            q.extend(print_Sudoku(27))
            for i in range(0,9):
                f.write(str(q[i]).strip('[]'))
                f.write('\n')
        f.close() 
    if paramters[1] =='36' :
        with open("output.txt.","a") as f:
            q=[]
            q.extend(print_Sudoku(36))
            for i in range(0,9):
                f.write(str(q[i]).strip('[]'))
                f.write('\n')
        f.close()
    if paramters[1] == '45':
        with open("output.txt.","a") as f:
            q=[]
            q.extend(print_Sudoku(45))
            for i in range(0,9):
                f.write(str(q[i]).strip('[]'))
                f.write('\n')
        f.close() 
    if paramters[1] == '54':
        with open("output.txt.","a") as f:
            q=[]
            q.extend(print_Sudoku(54))
            for i in range(0,9):
                f.write(str(q[i]).strip('[]'))
                f.write('\n')
        f.close()   
if __name__=='__main__':
    main()
