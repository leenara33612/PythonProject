"""
파일명: Ex07-01-for.py

for 문
    for문은 반복 가능한 객체의 요소들을 하나씩 꺼내서 반복 실행하는 반복문

    ex)
        for 변수 in 반복가능한 객체
            반복 수행할 코드

in 연산자
    특정 값이 컨테이너(리스트, 문자열, 튜플 등) 안에 포함 여부 확인
    True/False 반환

    ex) 값 in 컨테이너 : True or False 반환

반복문에서의 in 연산자
    반복할 요소를 하나씩 꺼내오는 역할

while or for
보통 횟수가 정해져 있으면 for
그외 while
"""

# 1. 리스트를 사용한 반복
fruits = ['사과', '바나나', '딸기', '오렌지']
for fruit in fruits:
    print(fruit, end = ' ') # end = ' ':기본값은 \n(줄바꿈), ' ' 공란으로 변경


