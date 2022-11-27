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
        direction = ((1,1),(1,-1),(-1,1),(-1,-1),(0,1),(0,-1),(1,0),(-1,0))     # 주변 8방향
        cpBoard=[arr[:] for arr in board]
        arr = []
        
        # 인덱스 오류 메소드
        def IsIndexOutCheck(y,x):
            if y<0 or x<0 or y>=len(cpBoard) or x>=len(cpBoard[0]):
                return True

        # 수비 깊이 탐색
        def DefendingDFS(grid,y,x,dirY,dirX,count):
            # 보드 바깥이면 종료
            if IsIndexOutCheck(y+dirY,x+dirX):
                return
            # 나의 돌을 발견한다면 종료
            if grid[y+dirY][x+dirX] == self._color:
                return
            # 빈공간이면
            if grid[y+dirY][x+dirX] == 0:
                # 상대방 돌과 돌 사이에 빈공간이 있다면 우선순위 높임
                if y+dirY+dirY>0 and x+dirX+dirX>0 and y+dirY+dirY<len(cpBoard) and x+dirX+dirX<len(cpBoard):
                    if grid[y+dirY+dirY][x+dirX+dirX] == self._color*-1:
                        arr.append([count-4,y+dirY,x+dirX])
                arr.append([count,y+dirY,x+dirX])
                return
            # 상대방 돌의 내가 놓을려는 방향 반대편에 나의 돌이 존재한다면 우선순위 낮춤
            if not IsIndexOutCheck(y+dirY*-1,x+dirX*-1):
                if grid[y+dirY*-1][x+dirX*-1]==self._color:
                    DefendingDFS(grid,y+dirY,x+dirX,dirY,dirX,count-1)
            # 상대방 돌을 계속 발견시
            DefendingDFS(grid,y+dirY,x+dirX,dirY,dirX,count-2)
        
        # 공격 깊이 탐색
        def AttackDFS(grid,y,x,dirY,dirX,count):
            # 보드 바깥이면 종료
            if IsIndexOutCheck(y+dirY,x+dirX):
                return
            # 보드 바깥이 아니면서 내 뒤에 상대방 돌이 있을 시 우선순위 낮춤
            if not IsIndexOutCheck(y+dirY*-1,x+dirX*-1):
                if grid[y+dirY*-1][x+dirX*-1]==self._color*-1:
                    AttackDFS(grid,y+dirY,x+dirX,dirY,dirX,count-1)
            # 현재 돌 위치의 주변에 보드 바깥 부분이 있다면
            if IsIndexOutCheck(y+dirY*-1,x+dirX*-1):
                AttackDFS(grid,y+dirY,x+dirX,dirY,dirX,count-1)
            # 같은방향에 나의돌을 발견한다면
            if grid[y+dirY][x+dirX] == self._color:
                AttackDFS(grid,y+dirY,x+dirX,dirY,dirX,count-1.5)
            # 같은방향에 상대방 돌을 발견한다면
            if grid[y+dirY][x+dirX] == self._color*-1:
                arr.append([count+0.5,y+dirY,x+dirX])
                return
            # 빈공간 발견 시
            if grid[y+dirY][x+dirX] == 0:
                # 빈공간의 현재 방향에서 한칸 더 뒤에 나의 돌을 발견한다면
                if y+dirY+dirY>0 and x+dirX+dirX>0 and y+dirY+dirY<len(cpBoard) and x+dirX+dirX<len(cpBoard) :
                    if grid[y+dirY+dirY][x+dirX+dirX] == self._color:
                        arr.append([count-2,y+dirY,x+dirX])
                # 승리
                if count<=-4: 
                    arr.append([count-100,y+dirY,x+dirX])
                else:
                    arr.append([count,y+dirY,x+dirX])
                return
            

        for i in range(len(cpBoard)):
            for j in range(len(cpBoard[0])):
                if cpBoard[i][j] == self._color * -1:
                    for idx in range(8):
                        xPosition = j+direction[idx][0]
                        yPosition = i+direction[idx][1]
                        if IsIndexOutCheck(yPosition,xPosition):
                            continue
                        if cpBoard[yPosition][xPosition] == -1:
                            DefendingDFS(cpBoard,i,j,direction[idx][1],direction[idx][0],1)
                if cpBoard[i][j] == self._color:
                    for idx in range(8):
                        xPosition = j+direction[idx][0]
                        yPosition = i+direction[idx][1]
                        if IsIndexOutCheck(yPosition,xPosition):
                            continue
                        if cpBoard[yPosition][xPosition] != -1:
                            AttackDFS(cpBoard,i,j,direction[idx][1],direction[idx][0],0)
        if not arr:
            for i in range(len(cpBoard)):
                for j in range(len(cpBoard[0])):
                    if cpBoard[i][j] == self._color * -1:
                        for idx in range(8):
                            xPosition = j+direction[idx][0]
                            yPosition = i+direction[idx][1]
                            if not IsIndexOutCheck(yPosition,xPosition):
                                arr.append([1,yPosition,xPosition])
        arr.sort()
        idx = 0
        while True:
            if board[arr[idx][1]][arr[idx][2]] == 0:
                break
            idx+=1
        stn.setX(arr[idx][1])
        stn.setY(arr[idx][2])
        print(arr[idx])
                                
                            

        print (" === White player was completed ==== ")
        return stn