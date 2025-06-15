"""
파일명: Ex07-03-for-dict.py
# 뭔소린지 모르겠다 복습할것

딕셔너리와 for 문
    딕셔너리의 키, 값들을 반복문으로 처리하는 방법
    - 딕셔너리 직접 반복: 키만 반복
    - .keys(): 모든 키들을 가져옴
    - values(): 모든 값들을 가져옴
    - .items(): 키와 값을 동시에 가져오기
"""

eng_dict = {
    'sun':'태양',
    'moon':'달',
    'star':'별',
    'space':'우주'
}

for word in eng_dict:
    print(f'{word}의 뜻: {eng_dict[word]}')

print()

for k, v in eng_dict.items():
    print(f'{k}의 뜻: {v}')

print()

eng_dict_keys = eng_dict.keys() # 변수에다 key값만 담아서 새로 생성
for k in eng_dict_keys:
    print(f'eng_dict의 key: {k}')

for k in eng_dict.keys():
    print(f'eng_dict의 key: {k}')

print()

eng_dict_values = eng_dict.values() # 변수에다 values값만 담아서 새로 생성
for v in eng_dict_values:
    print(f'end_dict의 value: {v}')

