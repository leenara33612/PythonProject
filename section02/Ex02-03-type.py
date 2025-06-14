""" 파일명: Ex02-03-type.py

내장 데이터 유형
    Python 변수는 다른 유형의 데이터를 저장할 수 있으며
    다른 유형은 다른 작업을 수행할 수 있다

텍스트 유형(문자열): str
숫자 유형: int(정수), float(실수형)
논리 유형: bool (True/False)

시퀀스 유형: list, tuple, range
매핑 유형: dict
세트 유형: set

바이너리 유형: bytes
없음 유형: None

"""

# str
v_str = 'Hello, World'
print(type(v_str))  # <class 'str'>

# int
v_int = 20
print(type(v_int))  # <class 'int'>

# float
v_float = 20.5
print(type(v_float))    # <class 'float'>

# list
v_list = ['피카츄', '라이츄', '파이리']
print(type(v_list))     # <class 'list'>

# range
v_range = range(6)
print(type(v_range))    # <class 'range'>

# dict
v_dict = {'name': '피카츄', 'Skill': '백만볼트'}
print(type(v_dict))

# bool(논리형) - True or False
v_bool = True
print(type(v_bool))

# NoneType
v_none = None
print(type(v_none))

'''
변수명 = 값
값의 type에 따라 연산이 달라진다

예) 더하기
    숫자 + 숫자 = 숫자
    문자 + 문자 = 문자연결
    문자 + str(숫자) = 문자연결
'''
num1, num2 = 10, 20
result = num1 + num2
print(result)   # 30

name, age = 'Alice', '15'
result = name + age
print(result)






