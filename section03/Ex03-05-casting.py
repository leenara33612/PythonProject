"""
파일명: Ex03-05-casting.py

형변환(casting)
    변수에 유형을 지정하려는 경우 형변환으로 가능
    주요 함수: int(), float(), str(), list(), tuple()
"""
# 1. 정수 형변환
str_num1 = '15'
str_num2 = '20'

result = str_num1 + str_num2
print(result)

result = int(str_num1) + int(str_num2)
print(f'형변환 후: {result}')

# 2. 실수 형변환
x = float('1.52654')
y = float(3)
print(x)
print(y)

z = int(3.141592)
print(z)

result = int(10) / int(3)
print(result)


# 3. 문자 형변환
strX = str(1)
strY = str(2)
result = strX + strY
print(result)

# 4. 아스키코드 변환
ch1 = ord('A')
print(ch1)
ch2 = chr(65)
print(ch2)


























