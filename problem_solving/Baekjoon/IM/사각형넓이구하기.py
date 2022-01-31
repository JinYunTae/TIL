# import sys
# input = sys.stdin.readline

# 네 개의 점 입력
points = []
for i in range(4) :
    points.append(list(map(int, input().split(' '))))

# 사각형의 넓이 계산
areas = []
for point in points :
    areas.append((point[2] - point[0]) * (point[3] - point[1]))
total = sum(areas)
print(total)

# 겹치는 영역을 처리... // 미완
x = []
y = []
for point in points :
    x.append(set(range(point[0], point[2]+1)))
    y.append(set(range(point[1], point[3]+1)))

co_area = []
for i in range(len(areas)-1): # 0 1 2
    for j in range(i+1, len(areas)): # 1 2 3 / 2 3 / 3
        co_x = x[i] & x[j]
        co_y = y[i] & y[j]
        if co_x and co_y :
            co_a = (max(co_x) - min(co_x)) * (max(co_y) - min(co_y))
            co_area.append(co_a)
    print(co_area)
covered = sum(co_area) # 8
print(covered)