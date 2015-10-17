__author__ = 'achau1'

from random import randint


def createMineSweeper(row, height, mines):
    n = row * height
    if mines > n:
        print("boo you suck give me a chance of surviving")
        return
    mineField = []
    for _ in range(row):
        minerow = []
        for _ in range(height):
            if randint(0, n) < mines:
                minerow.append("X")
            else:
                minerow.append("O")
        mineField.append(minerow)

    for i in range(row):
        print(mineField[i])
        # for j in range(height):
        #     print(mineField[i][j])
        print("\n")


row = 3
height = 3
mines = 3

createMineSweeper(row, height, mines)
