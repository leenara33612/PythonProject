"""
파일명: Ex07-04-for.py

<숙제>

이름      국어     영어     수학
홍길동     90      85      95
김철수     98      88      96
마이클     92      90      78
엘리스     88      82      100

변수 하나로 담기
"""
#JSON(JavaScript Object Notation)
students = [
    {'이름': '홍길동', '국어': 90, '영어': 85, '수학': 95},
    {'이름': '김철수', '국어': 98, '영어': 88, '수학': 96},
    {'이름': '마이클', '국어': 92, '영어': 90, '수학': 78},
    {'이름': '엘리스', '국어': 88, '영어': 82, '수학': 100}
]

for student in students:
    '''
    student = students[0]
    student = students[1]
    student = students[2]
    student = students[3]
    '''
    print(f'{student['이름']}', end = ' ')
    print(f'{student['국어']}', end = ' ')
    print(f'{student['영어']}', end = ' ')
    print(f'{student['수학']}')


print('=====================================================================')

for student in students:
    for k, v in student.items():
        print(f'{k}: {v}', end = ' ')
    print()