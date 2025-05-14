```
[advanced_project]
│
├─ backend/                      [ Flask 백엔드 ]
│   ├─ api/                         < API 모듈 폴더>
│   │   ├─ controllers/             < API 컨트롤러>
│   │   │   ├─ main_view.py            # 기본 route 설정 챗봇 대화 API
│   │   │   └─ data_view.py            # 데이터 페이지 route 설정 대화 기록 API
│   │   │
│   │   ├─ models/                  < 학습모델 폴더 >
│   │   │   └─ gemini_chat.py          # 챗봇 엔진
│   │   │
│   │   ├─ utils/                   # 유틸리티 함수
│   │   │
│   │   └─ __init__.py              # API 블루프린트 통합
│   │
│   ├─ db/                          < 필요한 데이터베이스 연동 보관 > 
│   │   └─ data_util.py                # 데이터베이스 연동
│   │
│   ├─ __init__.py                  # Flask 앱 초기화
│   ├─ app.py                       # Flask 메인 앱 파일
│   ├─ config.py                    # 설정 파일
│   ├─ .env                         # 환경변수 파일 (API_KEY...)
│   └─ requirements.txt             # 필요한 Python 패키지
│
│
├─ frontend/                    [ Vue.js 프론트엔드 ]
│   ├─ src/                         < Vue 소스 코드 >
│   │   ├─ assets/                  < 이미지 및 스타일 >
│   │   ├─ components/              < Vue 컴포넌트 >
│   │   ├─ views/                   < Vue 뷰 페이지 >
│   │   │
│   │   ├─ router/                  < Vue 라우터 설정 >
│   │   ├─ services/                < API 연결 서비스 >
│   │   ├─ store/                   < Vuex 상태관리 >
│   │   │
│   │   ├─ App.vue                  # 루트 컴포넌트
│   │   └─ main.js                  # Vue 진입점
│   │
│   ├─ public/                      < 정적 파일 >
│   ├─ babel.config.js 
│   ├─ package.json                 # npm 패키지 정보
│   └─ vue.config.js                # Vue 설정 파일
│
│
├─ notebook
├─ .gitignore
└─ README.md

```
