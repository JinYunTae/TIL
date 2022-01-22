import json


def over(scores):
    # 여기에 코드를 작성합니다.
    cnt = 0
    for score in scores :    # 각 요소를 순차로 할당
        if score >= 60 :    # 요소가 60점 이상이면
            cnt += 1    # 카운트 증가
    return cnt


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(over(scores)) # 3
