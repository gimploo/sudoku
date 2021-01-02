#!/usr/bin/python3
'''
   This program creates a sudoku board  
   --> so far it works with board type 4 and lower most of the time
'''

from sys import exit, argv
from random import randint, choice
from time import sleep

def main():

    print("\
    \n=============== Generating a sudoku puzzle lol ========================"\
    ,end='\n\n'\
    )

    if (len(argv) != 2):
        TYPE = int(input('Type of board: '))
    else:
        TYPE = int(argv[1])
    print()

    sudoku_board = create_board(TYPE)
    draw(sudoku_board, TYPE)

def create_board(n, times=100):
    array = [[0]*n for _ in range(n)]    
    numbers = [i for i in range(1,n+1)]
    for row in range(n):
        repeat = list()
        for column in range(n):
            if row == 0:
                output = choice(numbers) 
                while output in repeat:
                    output = choice(numbers)
                array[row][column] = output  
            else:
                output = unique_number(n, repeat, array, row, column) 
                if output is not None:
                    array[row][column] = output            
                else:
                    print('Failure... trying again')
                    draw(array,n)
#                    sleep(3)
                    if times != 0:
                        create_board(n,times-1)
                    else:
                        print('\n* Program stopped\n')
                        exit(1)
                '''
                else:
                    array[row][column] = 'X'
                '''
            repeat.append(array[row][column]) 
    return array        

def unique_number(length,exceptions,board,rowpos=0,columnpos=0):

    column_check = [
        board[rowpos][columnpos] for rowpos in range(rowpos-1,-1,-1)\
        if board[rowpos][columnpos] != 'X'\
    ]

    for number in range(1,length+1):
        if rowpos == 0 :
            if number not in exceptions : 
                return number
        else:
            if number not in column_check and \
                    number not in exceptions :
                return number

def draw(array, length):
    for row in range(length):
        space = 3
        for column in range(length):
            print('',array[row][column],end='')
            if column != length-1:
                print(' |', end='')
                space = space + 4
            else:
                print()
        if row != length - 1:
            print('-'*space,end='')
            print()
        else:
            print()

if __name__ == '__main__':
    main()
