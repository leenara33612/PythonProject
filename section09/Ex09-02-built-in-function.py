"""
파일명: Ex09-02-built-in-function.py
"""

'''
eval() 함수
    매개변수로 받은 expresstion(=식)을
    문자열로 받아서 실행하는 함수
'''

expr = input('계산식을 입력하세요 >>>')
result = eval(expr)
print(f'{expr} = {result}')