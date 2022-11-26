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
        cpBoard=[arr[:] for arr in board]
        arr = []
        
        # 수비 깊이 탐색
        def DefendingDFS(grid,y,x,dirY,dirX,count):
            if y+dirY<0 or x+dirX<0 or y+dirY>=len(cpBoard) or x+dirX>=len(cpBoard):
                return
            if grid[y+dirY][x+dirX] == self._color:
                return
            if grid[y+dirY][x+dirX] == 0:
                if grid[y+dirY+dirY][x+dirX+dirX] == self._color*-1 and (y+dirY+dirY>0 or x+dirX+dirX>0 or y+dirY+dirY<len(cpBoard) or x+dirX+dirX<len(cpBoard)) :
                    arr.append([count-2,y+dirY,x+dirX])
                else:
                    arr.append([count,y+dirY,x+dirX])
                return
            if grid[y+(dirY*-1)][x+(dirX*-1)]==self._color:
                #print("Hi",y,x,dirY*-1,dirX*-1,count-1)
                DefendingDFS(grid,y+dirY,x+dirX,dirY,dirX,count-1)
            #grid[y][x] = 0
            DefendingDFS(grid,y+dirY,x+dirX,dirY,dirX,count-2)
        # 공격 깊이 탐색

        def AttackDFS(grid,y,x,dirY,dirX,count):
            if y+dirY<0 or x+dirX<0 or y+dirY>=len(cpBoard) or x+dirX>=len(cpBoard):
                return
            if grid[y+dirY][x+dirX] == self._color:
                print("재귀",y,x,dirY,dirX,count)
                AttackDFS(grid,y+dirY,x+dirX,dirY,dirX,count-1.5)
            if grid[y+dirY][x+dirX] == 0:
                if grid[y+dirY+dirY][x+dirX+dirX] == self._color and (y+dirY+dirY>0 or x+dirX+dirX>0 or y+dirY+dirY<len(cpBoard) or x+dirX+dirX<len(cpBoard)) :
                    arr.append([int(count-4),y+dirY,x+dirX])
                else:
                    if count>=4:
                        arr.append(int(count-10),y+dirY,x+dirX)
                    else:
                        arr.append([int(count),y+dirY,x+dirX])
                return
            



        grid = [arr[:] for arr in cpBoard[:]]
        for i in range(len(cpBoard)):
            for j in range(len(cpBoard[0])):
                if cpBoard[i][j] == self._color * -1:
                    for idx in range(8):
                        xPosition = j+direction[idx][0]
                        yPosition = i+direction[idx][1]
                        if cpBoard[yPosition][xPosition] == -1:
                            DefendingDFS(grid,i,j,direction[idx][1],direction[idx][0],1)
                if cpBoard[i][j] == self._color:
                    for idx in range(8):
                        xPosition = j+direction[idx][0]
                        yPosition = i+direction[idx][1]
                        if cpBoard[yPosition][xPosition] != -1:
                            AttackDFS(grid,i,j,direction[idx][1],direction[idx][0],0)
        
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
        else:
            stn.setX(5)
            stn.setY(6)
        
        print (" === White player was completed ==== ")
        return stn