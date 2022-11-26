# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:04:19 2020
Maker : bychoi@deu.ac.kr 
@author: Com
"""

# sample player file which must be made by student 

from player import *
from stone import *
from random import *

class iot6789_student(player):
    def __init__(self, clr):
        super().__init__( clr)  # call constructor of super class, self 제거
        
    def __del__(self):  # destructor
        pass 

    def next(self, board, length):  # override

        # [ 0] [ 1] [ 2]
        # [ 3] (@@) [ 4]
        # [ 5] [ 6] [ 7]
        def search(local_X, local_Y):
            direction_list = ((1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)) # 방향 튜플
            distance_list = [0] * 8   # 기준점과의 거리를 저장할 리스트
            is_reflection_list = [False] * 8    # 돌 놓을 곳이 막히면 반사할지 여부를 저장하는 리스트

            # 주변 8칸 탐색
            for i in range(8):
                dx = direction_list[i][0]
                dy = direction_list[i][1]

                distance = 1  # 기준점과의 거리
                while True:
                    move_X = local_X + (dx*distance)     # X 좌표를 기준점에서 dx 방향으로 d만큼 이동
                    move_Y = local_Y + (dy*distance)     # Y 좌표를 기준점에서 dy 방향으로 d만큼 이동
                    if (not (0 <= move_X < length)) or (not (0 <= move_Y < length)):    # 벽을 만나면 탐색 종료
                        # print([move_X, move_Y], "장외")
                        is_reflection_list[i] = True
                        break
                    
                    move_point = board[move_X][move_Y]      # 이동 후의 지점

                    if move_point == (self._color * -1):    # 상대 돌이 직선으로 이어져 있으면
                        # print([move_X, move_Y], "직선 이동")
                        distance += 1                       # 거리 값 증가
                        continue
                    elif move_point == 0:    # 빈칸일 경우
                        # print([move_X, move_Y], "이곳에 돌을 둘 수 있습니다.")
                        break
                    else:               # 그 외의 경우(내 돌이 놓인 경우)
                        # print([move_X, move_Y], "내 돌이 놓여 있음")
                        is_reflection_list[i] = True
                        break
                
                distance_list[i] = distance  # 구한 거리 값을 리스트에 갱신

            # 최장거리 방향의 인덱스 구하기
            longest_index = distance_list.index(max(distance_list))
            # print("최장거리 방향 인덱스:", longest_index)

            # 반사 이동하기로 한 경우 인덱스 반전
            if (is_reflection_list[longest_index] == True):
                longest_index = 7 - longest_index
                # print("반전된 방향 인덱스:", longest_index)

            # 최장거리 방향 저장
            longest_X, longest_Y = direction_list[longest_index]

            # 바둑판에서 돌을 놓을 x, y 좌표 결정
            result_x = local_X + longest_X * distance_list[longest_index]
            result_y = local_Y + longest_Y * distance_list[longest_index]

            return result_x, result_y, distance_list[longest_index]


        print (" **** Black player : My Turns **** ")
        stn = stone(self._color)  # protected variable \

        x = randint(0,length-1) % length
        y = randint(0,length-1) % length

        max_distance = 0
        for i in range(length):
            for j in range(length):
                if board[i][j] == (self._color * -1):
                    tmp_X, tmp_Y, tmp_distance = search(i, j)
                    # 계산한 위치에 돌을 놓을 수 있으면
                    if (0 <= tmp_X < length) and (0 <= tmp_Y < length) and (board[tmp_X][tmp_Y] == 0) and (tmp_distance > max_distance):
                        x = tmp_X
                        y = tmp_Y
                        max_distance = tmp_distance

        stn.setX(x)
        stn.setY(y)
        print (" === Black player was completed ==== ")
        return stn
        