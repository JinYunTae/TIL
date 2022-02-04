import sys
input = sys.stdin.readline
while True:
    try:
        a, b = map(int, input().split(' '))
        print(a + b)
    except:
        break

'''
예제 입력 1 
1 1
2 3
3 4
9 8
5 2
예제 출력 1 
2
5
7
17
7
'''