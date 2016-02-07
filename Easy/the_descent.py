import sys
import math
 
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
 
 
# game loop
while True:
    space_x, space_y = [int(i) for i in input().split()]
    mountain_h_list = []
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right
        mountain_h_list.append(mountain_h)
 
    if mountain_h_list[space_x] == max(mountain_h_list):
        print("FIRE")
    else:
        print("HOLD")