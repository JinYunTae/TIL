import sys
input = sys.stdin.readline

while True:
    A, B = map(int, input().split(' '))
    if A or B :
        print(A + B)
    else :
        break