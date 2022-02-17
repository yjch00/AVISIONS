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
- 필요한 라이브러리를 모두 다운로드 받은 후 make_index.py -> QueryResult.py -> evaluate.py 앞의 세 가지 python파일을 실행해 아래와 같은 결과를 얻을 수 있습니다. 
![코딩 결과3](https://user-images.githubusercontent.com/98640306/154391500-6e85639a-6e0f-4e8b-acd0-8a267aaaf300.PNG)
 
 현재 doc 폴더에는 네이버, 카카오, MicroSoft, 삼성전자, 하이닉스 등의 총 19가지의 직무의 채용 정보, 서울대학교의 10개 강좌의 강의계획서가 저장되어 있습니다.
 
 
 ## 2. 코드 설명 및 추가 기능

- 질문과 답변

구글, 네이버 등의 검색창에 '질문'을 던지면 검색결과로 '답변'이 돌아옵니다. 이 또한 텍스트 유사도를 바탕으로 미리 저장되어 있던 '답변' 중 '질문'과 가장 가까운 '답변'을 가져오는 것입니다. 이때 '답변'과 '질문' 서로를 더 잘 감지할 수 있게 여러가지 전처리, 별도의 저장 과정이 필요합니다. 이 과정이 make_index.py, QueryResult.py파일에서 발생합니다.
- 텍스트 유사도 계산 방법

텍스트 유사도를 계산하는 방법은 굉장히 다양합니다. 단순히 겹치는 단어를 세는 빈도로는 좋은 성능이 안나올 확률이 높습니다. 희귀하게 나타나는 단어에 더 높은 가중치를 주는 tf-idf, BM25 등 그 외에도 여러가지 방법이 존재합니다. CustomScoring.py을 통해 사용자 정의의 측정 방법을 설정할 수 있습니다. 
- 정답 파일

만약 '질문'에 가장 필요한 '답변'이 무엇인지 정답을 제공한다면 정답과 비교해보아 여러가지 측정 방법을 시행해보며 가장 정답에 근접한 값을 내는 방법을 찾을 수 있습니다. doc 폴더 속의 relevance.txt는 '정답 파일'이라고 생각하시면 됩니다. 현재에 제대로된 정답 데이터는 넣지 않았지만 직접 유사하다고 생각되는 채용 정보와 강의계획서를 match시켜 더욱 텍스트 유사도가 높은 쌍을 찾을 수 있습니다.

 
 ## 3. 참고 자료

[AVISIONS 홈페이지] : https://avisi0ns.github.io/

[서울대학교 수강신청] : https://sugang.snu.ac.kr/

[마이크로소프트 채용] : https://careers.microsoft.com/us/en

[네이버 채용] : https://recruit.navercorp.com/naver/recruitMain

[카카오 채용] : https://careers.kakao.com/krewstory

[SK 하이닉스 채용] : https://recruit.skhynix.com/servlet/mnus_main.view

[whoosh search engine] : https://github.com/mchaput/whoosh

