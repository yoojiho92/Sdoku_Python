
from django.http import JsonResponse
from django.shortcuts import render
from random import *
import numpy as np
import json


def getStr(gridList):
    gridList = np.array(gridList)
    str = ""
    for i in range(0,3):
        for j in range (0,3):
            if (i == 2) and (j==2) :
                 str += "%d" % gridList[i][j]
            else :
                str += "%d ," % gridList[i][j]
    return str



grid_1 = np.arange(9).reshape([3,3]) +1

for i in range(0,3):
    for j in range (0,3):
        temp = 0;
        random_a = randint(0,2)
        random_b = randint(0,2)
        temp = grid_1[i][j]
        grid_1[i][j] = grid_1[random_a][random_b]
        grid_1[random_a][random_b] = temp

x1 = [[0, 0, 1],
      [1, 0, 0],
      [0, 1, 0]]

x2 = [[0, 1, 0],
      [0, 0, 1],
      [1, 0, 0]]

grid_1 = np.asmatrix(grid_1)
x1 = np.asmatrix(x1)
x2 = np.asmatrix(x2)

grid_2 = x1 * grid_1
grid_3 = x2 * grid_1

grid_4 = grid_1 * x1
grid_5 = x1 * grid_1 * x1
grid_6 = x2 * grid_1 * x1

grid_7 = grid_1 * x2
grid_8 = x1 * grid_1 * x2
grid_9 = x2 * grid_1 * x2


gridDict = {'grid1' : getStr(grid_1),
            'grid2' : getStr(grid_2),
            'grid3' : getStr(grid_3),
            'grid4' : getStr(grid_4),
            'grid5' : getStr(grid_5),
            'grid6' : getStr(grid_6),
            'grid7' : getStr(grid_7),
            'grid8' : getStr(grid_8),
            'grid9' : getStr(grid_9),}
jsonString = json.dumps(gridDict)


def post_list(request):
    data = [
            {'id': 1, 'title': 'title 1'},
    ]
    return JsonResponse(jsonString, safe=False)

