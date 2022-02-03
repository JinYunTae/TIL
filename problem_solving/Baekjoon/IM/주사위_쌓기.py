# 주사위의 수와 각 눈을 입력받습니다.
n_dice = int(input())
dice = []
for n in range(n_dice):
    dice.append(list(map(int, input().split(' '))))

sum_max = 0 # 최종값을 저장하기 위한 변수입니다.

# 첫 주사위에 맞춰 각 주사위의 옆면을 분리합니다.
for j in range(6):
    top = dice[0][j] # dot을 첫 주사위의 각 눈으로 만들기 위한 초기화입니다.
    max_side = [] # 각 주사위별 옆면의 최대값을 저장하는 리스트입니다.
    # 주사위의 수만큼 반복합니다.
    for i in range(n_dice):
        side = dice[i][:] # i번째 주사위의 눈을 복사합니다.
        bot = top # bot을 이전 주사위의 top으로 변경합니다.
        b_ind = dice[i].index(bot) # 옆면에서 bot의 인덱스를 찾습니다.
        side.remove(bot) # 눈 목록에서 bot을 제거합니다.
        # top의 값을 찾습니다.
        if b_ind == 0 or b_ind == 5:
            top = dice[i][5 - b_ind]
        elif b_ind < 3 :
            top = dice[i][b_ind + 2]
        else :
            top = dice[i][b_ind - 2]
        side.remove(top) # 눈 목록에서 top을 제거합니다.
        max_side.append(max(side)) # i번째 주사위 옆면의 최대값을 리스트에 저장합니다.
    # 최대 눈들의 합을 갱신합니다.
    if sum_max < sum(max_side):
        sum_max = sum(max_side)
    
print(sum_max)
'''
예제 입력 1 
5
2 3 1 6 5 4
3 1 2 4 6 5
5 6 4 1 3 2
1 3 6 2 4 5
4 1 6 5 2 3
예제 출력 1 
29
'''