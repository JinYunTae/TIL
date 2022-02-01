# 스위치 수, 스위치 상태, 학생 수를 입력받습니다.
n_sw = int(input())
sw_state = list(map(int, input().split(' ')))
n_st = int(input())

for i in range(n_st): # 학생 수 만큼 반복합니다.
    st_sw = list(map(int, input().split(' ')))
    sw = st_sw[1] - 1 # 입력받은 스위치의 인덱스를 계산합니다.
    
    # 만약 남자라면
    if st_sw[0] == 1:
        for i in range(1, n_sw + 1): # 전체 스위치에 대해
            if i % st_sw[1] == 0: # 만약 스위치 번호가 입력받은 수의 배수라면
                sw = i - 1 # 해당 스위치의 인덱스를 계산합니다.
                sw_state[sw] = (sw_state[sw] + 1) % 2 # 스위치를 전환합니다.
    
    # 만약 여자라면
    elif st_sw[0] == 2:
        width = 0 # 전환 폭을 초기화합니다.
        while True:
            # 폭이 인덱스 범위를 넘어선다면
            if sw - width < 0 or sw + width > n_sw - 1:
                width -= 1 # 이전 범위로 축소하고
                break # 폭 계산을 종료합니다.
            
            # 양 옆의 값이 같다면
            elif sw_state[sw - width] == sw_state[sw + width]:
                width += 1 # 폭을 한칸 더 넓힙니다.

            # 그 외의 경우 (인덱스 범위를 넘어서지 않았지만 양 옆의 값이 다르다면)
            else :
                width -= 1 # 이전 범위로 축소하고
                break # 폭 계산을 종료합니다.
        
        for i in range(sw - width, sw + width + 1): # 전환 범위 내의 스위치 값을 전환합니다.
            sw_state[i] = (sw_state[i] + 1) % 2

# 출력문
for i in range(1, n_sw + 1):
    # 전체 스위치에 대해
    if i % 20 == 0: # 스위치의 개수가 20개라면
        print(sw_state[i-1]) # 출력하고 개행합니다.
    
    # 마지막 스위치라면
    elif i == n_sw:
        print(sw_state[i-1]) # 출력하고 개행합니다.
    
    # 그 외의 스위치는(20번째도 아니고 마지막도 아닌 경우)
    else : 
        print(sw_state[i-1], end=' ') # 출력하고 한 칸을 띄웁니다.
'''
예제입력
8
0 1 0 1 0 0 0 1
2
1 3
2 3
예제출력
1 0 0 0 1 1 0 1
'''