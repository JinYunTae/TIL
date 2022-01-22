def is_user_data_valid(user_data):
    # 여기에 코드를 작성합니다.
    for data in user_data.values() :   # 데이터 딕셔너리의 value들만 순차로 할당
        if data :    # 문자열이 있다면
            continue
        else :    # 문자열이 비었다면
            return False
    return True


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': '',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data1)) 
    # False 

    user_data2 = {
        'id': 'jungsangsu',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data2)) 
    # True