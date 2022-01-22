import json

import json

def turn(temperatures):
    # 여기에 코드를 작성합니다.
    # 인덱스 0은 최고기온, 1은 최저기온으로 확정되어 있다.
    # 인덱스 확정 없으면 if문 쓰자
    '''
    maximum = []    # 최대값만 저장할 리스트
    minimum = []    # 최소값만 저장할 리스트
    for temperature in temperatures :
        maximum.append(temperature[0])    # 온도 첫 항목(최대값) 저장
        minimum.append(temperature[1])    # 온도 두번째 항목(최소값) 저장
    return {
            'maximum' : maximum, 
            'minimum' : minimum
    }    # 무엇을 위한 딕셔너리인가?
    # 리턴에서 가독성 감소(요소 많으면 어차피 가독성 감소)
    '''

    temp_dic = {'maximum': [], 'minimum' : []}    # 딕셔너리 목적 확실
    for temperature in temperatures :
        temp_dic['maximum'].append(temperature[0])    # 온도 첫 항목(최대값) 저장
        temp_dic['minimum'].append(temperature[1])    # 온도 두번째 항목(최소값) 저장
    return temp_dic    # 무엇을 반환하는지 확실
    # 어차피 더 이상 사용되지 않는 객체는 가비지 컬렉터가 제거
    # 객체 선언의 수가 너무 많지 않다면 신경쓰지 말자

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperatures = [
        [9, 3],
        [9, 0],
        [11, -3],
        [11, 1],
        [8, -3],
        [7, -3],
        [-4, -12]
    ]
    print(turn(temperatures)) 
    # {
    #     'maximum': [9, 9, 11, 11, 8, 7, -4], 
    #     'minimum': [3, 0, -3, 1, -3, -3, -12]
    # }
