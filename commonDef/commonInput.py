######## 입력인 필요한 경우 다른 모듈에서 사용할 방법
# import commonDef.commonInput as comInput
# input_arr = comInput.sysInputArr() # input 배열


import sys

def sysInputArr() :
    # 배열 입력을 띄어 쓰기로 입력 후 엔터
    print('띄어쓰기를 구분으로 데이터를 입력하시오 : ')
    input_arr = [int(x) for x in sys.stdin.readline().split()]
    return input_arr

# 배열 여러개를 보내야 할 때(백준 문제)
# def sysInputArr() :
#     size = int(input('입력받을 데이터 크기:'))
#     for i in range(size):
#         # 배열 입력을 띄어 쓰기로 입력 후 엔터
#         print('띄어쓰기를 구분으로 데이터를 입력하시오 : ')
#         input_arr = [int(x) for x in sys.stdin.readline().split()]