"""
파일명: Ex02-05-String.py

문자열(String, str)
    문자들의 순서가 있는 나열
    작은따옴표(') 또는 큰따옴표(")로 표현
    문자열은 변경불가능(immutable)
"""
# 1. 문자열 인덱싱
'''
       | h | e | l | l | o |
index    0   1   2   3   4
역순     -5  -4  -3  -2  -1
'''
str1 = 'hello'
print('1번째 문자:', str1[0])
print('마지막 문자:', str1[4])
print('-1번째 문자:', str1[-1])

# 2. 문자열 슬라이싱
str2 = 'Python Programming'
print('처음부터 4글자:', str2[0:4])
print('처음부터 4글자:', str2[:4])
print('7번째 문자부터:', str2[7:])
print('마지막 5글자:', str2[-5:])

# 4. 문자열 메서드(함수)
str3 = '     P y t h o n     '
print('원본:', str3)
print('공백제거:', str3.strip())
print('모두 대문자:', str3.upper())
print('모두 소문자:', str3.lower())
print('문자 교체:', str3.replace('P', 'J'))
print('문자 사이까지 공백제거:', str3.replace(' ', ''))

# 문자열 길이 len()
print('문자열 길이:', len('Hello'))




















