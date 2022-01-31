# 첫번째 수를 입력받습니다.
first = int(input())
# 2보다 큰 수에서 두번째 수가 절반보다 작으면 길이가 무조건 3이 됩니다.
# 혹시모를 경우에 대비하기 위해 절반보다 1작고 정수로 반환되는 몫을 이용합니다.
second = first // 2

# 최대길이를 비교하기 위한 변수입니다.
max_len = 0 # 비교에 영향을 주지 않는 최대값은 2입니다.
# 첫번째와 2번째 수 사이의 범위만 검사하면 됩니다.
for num in range(second, first+1):
    li = [first, num]
    next = first - num
    while next >= 0: # 다음 값이 음수가 아니라면
        li.append(next) # 목록에 추가하고
        next = li[-2] - li[-1] # 그 다음값을 계산합니다.
    cnt = len(li) # 계산된 목록의 길이를 구합니다.
    if max_len < cnt: # 길이가 이전 최대값보다 크다면
        record = li[:] # 목록을 기록합니다.
        max_len = cnt # 최대 길이를 갱신합니다.

print(max_len)
print(*record)