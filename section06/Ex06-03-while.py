"""
파일명: Ex06-03-while.py
"""

my_list = []
n = 1
while n != 0:
    n = int(input('정수를 입력하세요(종료는 0입니다.) >>> '))
    my_list.append(n)
    print(f'list의 값은:{my_list}')#n을 입력할때마다의 list값을 보여줌

print(my_list) #while문이 종료된 후의 list값을 보여줌
my_list.pop() #pop: 맨 뒤의 값을 제거
print(my_list)

