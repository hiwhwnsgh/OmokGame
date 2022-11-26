# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:37:40 2020
Maker : bychoi@deu.ac.kr 

@author: Com
"""

# sample player file which must be made by student 

from player import *
from stone import *
from random import *

class iot12345_student(player):
    def __init__(self, clr):
        super().__init__( clr)  # call constructor of super class
    def __del__(self):  # destructor
        pass 
    def next(self, board, length):  # override
        print (" **** White player : My Turns **** ")
        stn = stone(self._color)  # protected variable
        direction = ((1,1),(1,-1),(-1,1),(-1,-1),(0,1),(0,-1),(1,0),(-1,0))
        idx = 0
        cpBoard=[arr[:] for arr in board]
        arr = []
        def dfs(grid,y,x,dirY,dirX,count):
            if y+dirY<0 or x+dirX<0 or y+dirY>=len(cpBoard) or x+dirX>=len(cpBoard):
                return
            if grid[y+dirY][x+dirX] == 1:
                return
            if grid[y+dirY][x+dirX] == 0:
                if grid[y+dirY+dirY][x+dirX+dirX] == -1 and (y+dirY<0 or x+dirX+dirX<0 or y+dirY+dirY>=len(cpBoard) or x+dirX+dirX>=len(cpBoard)) :
                    arr.append([count-3,y+dirY,x+dirX])
                else:
                    arr.append([count,y+dirY,x+dirX])
                return
            if grid[y+(dirY*-1)][x+(dirX*-1)]==1:
                dfs(grid,y+dirY,x+dirX,dirY,dirX,count-1)
            grid[y][x] = 0
            dfs(grid,y+dirY,x+dirX,dirY,dirX,count-2)
        for i in range(len(cpBoard)):
            for j in range(len(cpBoard[0])):
                if cpBoard[i][j] == -1:
                    for _ in range(8):
                        grid = [arr[:] for arr in cpBoard[:]]
                        xPosition = j+direction[idx][0]
                        yPosition = i+direction[idx][1]
                        if cpBoard[yPosition][xPosition] == -1:
                            dfs(grid,i,j,direction[idx][1],direction[idx][0],1)
                        idx +=1
                idx = 0
        if arr:
            arr.sort()
            print(arr)
            i = 0
            while True:
                if board[arr[i][1]][arr[i][2]] == 0:
                    break
                i+=1
            stn.setX(arr[i][1])
            stn.setY(arr[i][2])
        # 첫 수
        else:
            for i in range(len(cpBoard)):
                for j in range(len(cpBoard[0])):
                    if cpBoard[i][j] == -1:
                        if i+1<0 or j+1<0 or i+1>=len(cpBoard) or j+1>=len(cpBoard):
                            stn.setX(i+1)
                            stn.setY(j+1)
                        elif i-1<0 or j-1<0 or i-1>=len(cpBoard) or j-1>=len(cpBoard):
                            stn.setX(i-1)
                            stn.setY(j-1)
                        elif i+1<0 or j-1<0 or i+1>=len(cpBoard) or j-1>=len(cpBoard):
                            stn.setX(i+1)
                            stn.setY(j-1)
                        else:
                            stn.setX(i-1)
                            stn.setY(j+1)
        print (" === White player was completed ==== ")
        return stn