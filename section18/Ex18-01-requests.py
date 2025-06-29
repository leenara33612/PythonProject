"""
파일명: Ex18-01-requests.py

requests 라이브러리
    Http 요청을 보내기 위한 간편하고 인기있는 라이브러리,
    이를 사용하여 웹페이지 데이터를 가져오거나,
    API와 상호 작용 할 수 있다

라이브러리 설치 방법
pip install requests

https://n.news.naver.com/article/657/0000039979?cds=news_media_pc&type=editn

URL(Uniform Resource Locator)
    인터넷에서 웹페이지, 이미지, 동영상 등과 같은 리소스를 찾을 수 있는 주소

프로토콜(protocol)
    네트워크를 통해 통신을 수행하기 위한 표준화된 규칙, 절차, 통신 프로세스

    ex) http/https - 웹 서버 프로토콜
"""

import requests

url = 'https://n.news.naver.com/article/657/0000039979?cds=news_media_pc&type=editn'
response = requests.get(url)
print(response.text)