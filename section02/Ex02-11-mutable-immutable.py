"""
파일명: Ex02-11-mutable-immutable.py

데이터 타입의 가변성
    mutable: 객체 생성 후 내용 변경 가능
        값 변경 시 메모리 주소 유지
        ex) list, set, dict
    immutable: 객체 생성 후 내용 변경 불가
        값 변경 시 새 메모리 주소 할당
        ex) int, str, tuple 등

"""
# 1. mutable 예제
pokemon = ['피카츄', '라이츄', '파이리']
print(pokemon)
print('메모리 주소:', id(pokemon))

pokemon[1] = '잠만보'
print(pokemon)
print('메모리 주소:', id(pokemon))


# 2. immutable 예제
level = 25
print('level:', level)
print('메모리 주소:', id(level))

level = 27
print('level:', level)
print('메모리 주소:', id(level))


# 리터럴(Literal) - 소스코드에서 고정된 값









