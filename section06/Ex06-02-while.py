"""
파일명: Ex06-02-while.py
"""

my_list = []
n = int(input('정수를 입력하세요(종료는 0입니다) >>> '))
while n != 0:
    my_list.append(n) # append: 끝에 항목 추가
    n = int(input('정수를 입력하세요(종료는 0입니다) >>> '))

print(my_list)
