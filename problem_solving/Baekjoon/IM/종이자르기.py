# 가로, 세로, 자르는 수의 정보를 입력받습니다.
width, heigth = map(int, input().split(' '))
n_cut = int(input())
length = [[width], [heigth]]

# 자르는 수만큼 반복합니다.
for cut in range(n_cut):
    direction, l_num = map(int, input().split(' ')) # 자르는 방향과 점선의 번호를 정합니다.
    target = length[not direction] # (가로는 세로) / (세로는 가로) 길이가 바뀝니다.
    cutted = target[0] # 이미 잘린 길이의 초기값을 설정합니다.
    sect = 0 # 자를 영역의 인덱스를 찾기 위한 변수입니다.
    for i in range(len(target)): # 구성된 영역의 수만큼 반복합니다.
        # 자를 번호가 잘린 길이보다 크다면
        if l_num > cutted:
            sect = i + 1 # 다음 영역으로 넘어갑니다.
            cutted += target[i + 1] # 다음 영역의 길이를 추가합니다.
        # 자를 번호가 잘린 길이보다 작다면
        else :
            cutted -= target[i] # 해당 영역의 길이를 제거합니다.
            break # 반복을 종료합니다.
        
    target.insert(sect, abs(l_num - cutted)) # 잘린 영역의 위치에 잘린 길이를 넣습니다.
    # [[10][8]] -> [[4, 10][8]]
    target[sect + 1] -= abs(l_num - cutted) # 잘린 영역의 길이를 나머지 길이로 바꿉니다.
    # [[4,10][8]] -> [[4, 6][8]]

print(max(length[0]) * max(length[1]))