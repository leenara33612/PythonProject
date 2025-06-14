"""
파일명: Ex03-02-print.py

print 함수
    텍스트나 값을 화면에 출력하는 가장 기본적인 함수
    - sep: 값 사이 구분자 (기본: 공백)
    - end: 출력 끝 문자 (기본: \n)
    - file: 출력 대상 (기본: sys.stdout)
"""
# 1. 기본 출력
pokemon = '피카츄'
level = 25
print('포켓몬:', pokemon, '레벨:', level)

# 2. sep 매개변수
print('포켓몬:', pokemon, '레벨:', level, sep='-')

# 3. end 매개변수
print('피카츄', end='=>')
print('라이츄', end='=>')
print('파이리')

# 4. file 매개변수
file = open('pokemon.txt', 'w', encoding="UTF-8")
print('name: 피카츄', file=file)
print('type: 전기', file=file)
file.close()






