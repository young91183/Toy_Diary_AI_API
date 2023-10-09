# Toy Porject를 위한 AI 감정분류 API (Falsk)  

### * 특이사항  
- 2023/10/01 spell_checker의 버전이 변경됨에 따라 정상작동 되지 않는 오류가 있습니다.  
  때문에 evaluate.py의 text = correct_spelling(text)를 주석처리 후 사용하시기 바랍니다.  
  오류 해결 시 README.md 수정 예정입니다.  
  
## Purpose of API use  
사용자의 일기를 분석해 7가지 감정을 반환
- 행복  
- 보통  
- 슬픔  
- 분노  
- 놀람  
- 불쾌함  
- 두려움  
  
flask_api.py를 작동시키면 POST 형식을 통해 API를 사용 가능
사용 예시를 위해 다음 주소에 배포 중   
(POST Man 등을 활용해 Test 가능)  
http://43.200.6.162:5000/predict

### - 사용 방법
● request (POST) :  
{  
  "text" : "오늘은 너무 짜증이 났다."  
}  
  
● response :  
{  
    "emotion": "분노"  
}  
  
  
## Modeling  
전체 모델링 프로세스는 Modeling.ipynb 파일에서 수행
  
  
## Environment Setting  
- Git pull을 받기 전 반드시 git-lfs를 설치 후 pull 진행  
  (model.pth의 용량이 300MB이상이여서 lfs저장소에 위치해 있기 때문)
- 라이브러리 및 패키지 설치 코드는 Modeling.ipynb 상단에 위치  
- Python version : 3.7.16 (가상환경 이용 시 참고)  
- pip install -r requirements.txt 명령어를 통해 필요한 라이브러리를 설치
  
  
#### ※ 본 API는 Spring으로 제작 된 다른 API와 연동되어 일부 기능을 추가하기 위해 제작 된 API입니다.
연계 된 API 주소 : https://github.com/toy-f-rebellion/toy_back  

