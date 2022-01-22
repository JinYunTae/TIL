import json


def max_score(scores):
    # 여기에 코드를 작성합니다.
    max_value = scores[0]
    for score in scores :    # 각 요소들을 순차적으로 할당
        if score > max_value : # scores의 첫 요소를 뺄 방법은...
            max_value = score

    return max_value

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(max_score(scores)) # 90
