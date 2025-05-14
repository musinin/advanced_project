```
[advanced_project]
webpage/
│											
├── views/           	< route 파일이 들어갈 폴더 >
│     ├── main_view.py          # 기본 route 설정
│     └── data_view.py          # 데이터 페이지 route 설정
│
├── templates/       	        < HTML 템플릿 폴더 >
│     ├── page_modules/	  < 공통으로 사용되는 css, js 사용 Code >
│     ├── data/               < 페이지 사용 HTML >
│     ├── base.html	            # 홈페이지 베이스 부모 HTML
│     └── index.html	   	    # 첫 화면 웹페이지 템플릿
│
├── static/          		< 파일 폴더 >
│     ├── css/                < css 파일 폴더>
│     ├── js/                  < js 파일 폴더 >
│     └── images/             < 이미지 폴더 >
│
├── db/			        <필요한 데이터 보관 (.py, .css...) > 
│     ├── data_util.py	   # 데이터베이스 연동
│     └── ex.css		   # 수집한 데이터
│
├── model/                  < DB 연동 자동화 코드 폴더 >
│     └── gemini_chat.py 	  # 챗봇 모델
│
├── __init__.py      		# Flask 애플리케이션 초기화
├── .env                     # API 키 보관
└── requirements.txt          # 필요한 import  
```