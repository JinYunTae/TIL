def is_id_valid(user_data):
    # 여기에 코드를 작성합니다.
    '''
    if user_data.get('id') :    # 아이디가 빈 값이 아니라면
        if user_data.get('id')[-1] in map(str, range(0, 10)) :    # 끝이 0~9?
            # 정수화는 제약이 있다 => 0~9를 문자열화 해야 광범위 적용 가능
            return True
        else :
            return False
    else :    # 아이디가 빈 값이면 False
        return False
    '''
    user_id = user_data.get('id')    # 반복적으로 사용하는 내용은 변수화도 좋다
    if user_id :    # 아이디를 이용한다는 것을 알기 쉽다
        # 정수화는 제약이 있다 => 0~9를 문자열화 해야 광범위 적용 가능
        if user_id[-1] in map(str, range(0, 10)) :    # 끝이 0~9?, 훨씬 간결
            return True
        else :
            return False
    else :    # 아이디가 빈 값이면 False
        return False


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': 'jungsangsu5',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data1)) 
    # True
    
    user_data2 = {
        'id': 'kimssafy!',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data2)) 
    # False