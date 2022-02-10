import sys
input = sys.stdin.readline

re = int(input())
cols = []

for n in range(re):
    x, h = map(int, input().split(' '))
    cols.append([x, h])
cols.sort()

xs = []
hs = []
for col in cols:
    xs.append(col[0])
    hs.append(col[1])

# 커지는 동안의 값 구하기
area = 0
next_max = hs.index(max(hs))
max_col = {'x':0, 'h':0}
for i in range(xs.index(max(xs))):
    if max_col['h'] < hs[i]:
        area += max_col['h'] * (xs[i] - max_col['x'])
        max_col['x'], max_col['h'] = xs[i], hs[i]

# 작아지는 동안의 값 구하기 // 끝값에 대한 검증
next_max = hs.index(max(hs[next_max + 1:]))
while next_max != (len(hs) - 1):
    area += hs[next_max] * (xs[next_max] - max_col['x'])
    area += (max_col['h'] - hs[next_max])
    max_col['x'], max_col['h'] = xs[next_max], hs[next_max]
    next_max = hs.index(max(hs[next_max + 1:]))
area += hs[next_max] * (xs[next_max] - max_col['x'])
area += (max_col['h'] - hs[next_max])
area += hs[next_max]

print(area)

'''
pre = {'x':0 ,'h':0}
max = {'x':0 ,'h':0}
new = {'x':0 ,'h':0}
temp_area = 0
area = 0
for col in cols:
    new['x'], new['h'] = col
    if max['h'] <= new['h']:
        temp_area = 0
        area += max['h'] * (new['x'] - max['x'])
        max['x'], max['h'] = new['x'], new['h']
    elif new['h'] < max['h']:
        if new['h'] < pre['h']:
            temp_area += (pre['h'] - new['h'])
            temp_area += new['h'] * (new['x'] - pre['x'])
        else : # 작아지다 중간에 커지지만 max외의 다른 값보다 작을 때 문제 발생
            temp_area = max['h'] - new['h']
            temp_area += new['h'] * (new['x'] - max['x'])
    pre['x'], pre['h'] = new['x'], new['h']
area += (new['h'] + temp_area)
print(area)
'''