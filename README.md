# advanced_project


## 프로젝트 개요

이 프로젝트는 데이터를 수집하고, 해당 데이터를 바탕으로 인공지능 모델을 학습시켜 **특정 분야에 특화된 챗봇**을 만드는 것을 목표로 합니다.  
백엔드는 Python의 Flask 프레임워크로, 프론트엔드는 Vue.js로 구성되어 있으며, 데이터 분석을 위한 Jupyter Notebook 환경도 포함되어 있습니다.

---

## 주요 기능

- 다양한 도메인의 데이터를 수집하고 전처리
- 머신러닝/딥러닝 모델 학습을 통한 챗봇 구축
- 사용자의 질의에 대해 자연스러운 응답 생성
- Vue.js 기반 웹 인터페이스에서 대화 가능
- 향후 데이터 시각화 및 분석 기능 포함 예정

---

## 🛠 사용 기술 스택

- **백엔드**: Python, Flask
- **프론트엔드**: Vue.js (Vite 예상)
- **AI/ML**: OpenAI API, Gemini API 등
- **데이터 분석**: Jupyter Notebook, Pandas, Scikit-learn
- **기타**: dotenv, Axios, Chart.js, Plotly 등

---

## 프로젝트 구조


```
[advanced_project]
│
├─ backend/                         [ Flask 기반 백엔드 API ]
│   ├─ api/                         # API 모듈 폴더
│   │   ├─ controllers/             # API 컨트롤러
│   │   │   ├─ main_view.py         # 기본 route 설정 챗봇 대화 API
│   │   │   └─ data_view.py         # 데이터 페이지 route 설정 대화 기록 API
│   │   │
│   │   ├─ models/                  # 학습모델 폴더 >
│   │   │   └─ gemini_chat.py       # 챗봇 엔진
│   │   │
│   │   ├─ utils/                   # 유틸리티 함수
│   │   │
│   │   └─ __init__.py              # API 블루프린트 통합
│   │
│   ├─ db/                          # 필요한 데이터베이스 연동 보관 > 
│   │   └─ data_util.py             # 데이터베이스 연동
│   │
│   ├─ __init__.py                  # Flask 앱 초기화
│   ├─ app.py                       # Flask 메인 앱 파일
│   ├─ config.py                    # 설정 파일
│   ├─ requirements.txt             # 필요한 Python 패키지
│   └─ .env                         # 환경변수 파일 (API_KEY...)
│                                     .env 파일은 보안상 .gitignore에 포함
│
├─ frontend/                        [ Vue.js 프론트엔드 ]
│   ├─ src/                         # Vue 소스 코드 >
│   │   ├─ assets/                  # 이미지 및 스타일 >
│   │   │
│   │   ├─ components/              # Vue 컴포넌트 >
│   │   │   └─ ChatBot.vue          # UI(화면)와 동작을 담당
│   │   │
│   │   ├─ services/                # API 연결 서비스 >
│   │   │   └─ api.js               # API 요청 함수
│   │   │
│   │   ├─ views/                   # Vue 뷰 페이지 >
│   │   ├─ router/                  # Vue 라우터 설정 >
│   │   ├─ store/                   # Vuex 상태관리 >
│   │   │
│   │   ├─ App.vue                  # 루트 컴포넌트
│   │   └─ main.js                  # Vue 진입점
│   │
│   ├─ public/                      # 정적 파일 >
│   ├─ babel.config.js 
│   ├─ package.json                 # npm 패키지 정보
│   └─ vue.config.js                # Vue 설정 파일
│
│
├─ notebook                         # 데이터 분석 및 학습용 Jupyter 노트북
├─ .gitignore
└─ README.md                        # 프로젝트 설명 파일

```

---

## 설치 및 실행 방법


### 1. 사전 준비
- Python 3.11 이상 설치
- Node.js 설치 (프론트엔드 실행용)

### 2. 백엔드 실행

```bash
# 가상환경 생성 및 활성화 (Windows 기준)
python -m venv venv
venv\Scripts\activate

# 필수 패키지 설치
cd backend
pip install -r requirements.txt

# Flask 서버 실행
python app.py
```

### 3. 프론트엔드 실행

```bash
# frontend 폴더로 이동
cd ../frontend

# 필요한 패키지 설치
npm install

# 개발 서버 실행
npm run dev
```
---




