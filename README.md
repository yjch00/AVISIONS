# AVISIONS search engine code

[AVISIONS 홈페이지] : https://avisi0ns.github.io/

위 홈페이지에서 확인할 수 있는 '체험하기'는 16가지의 시나리오를 바탕으로 사용자가 쉽게 체험할 수 있도록 만든 데모 서비스입니다.
현 github는 미리 구성되어 있는 16가지의 시나리오가 아닌 사용자가 직접 강의계획서, 채용 페이지 내용을 변경하고 유사도를 측정할 수 있는 기능을 위한 페이지입니다.
현 페이지를 통해 사용자는 직접 체험 가능한 실제 구현 코드 및 설명서를 확인할 수 있습니다.


## 1. 파일 구성 및 순서

AVISIONS는 채용 정보와 강의계획서 사이의 텍스트 유사도를 구하기 위해 구글, 네이버 등의 검색 사이트에서 볼 수 있는 search engine 코드를 이용하고 있습니다.
우선 searchengine의 주된 구성요소는 4개의 python파일과 3개의 doc폴더 속에 있는 txt 문서입니다.
- doc 폴더 속 query.txt에는 채용 정보가 저장되어 있습니다. 직접 채용 정보를 추가, 수정, 제거할 수 있습니다.
- doc 폴더 속 document.txt에는 강의계획서가 저장되어 있습니다. 직접 강의계획서를 추가, 수정, 제거할 수 있습니다. 
- make_index.py -> QueryResult.py -> evaluate.py 앞의 세 가지 python파일을 실행해 아래와 같은 결과를 얻을 수 있습니다. 
 ![코딩 결과](https://user-images.githubusercontent.com/98640306/154388949-a1d32a2c-ad97-4033-8c76-e0ebee21784b.PNG)
 
 ## 2. 추가 사항
 
 
 
 ## 3. 참고 자료
