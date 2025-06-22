"""
파일명: Ex12-02-module.py

모듈 사용법
    from 모듈명 import 함수(또는 변수)
    from 모듈명 import 함수1, 함수2
    from 모듈명 import *(전체 추가)
"""

from converter import kilometer_to_miles

miles = kilometer_to_miles(150)
print(f'150Km = {miles}miles')