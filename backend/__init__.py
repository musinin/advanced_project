from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

# API 블루프린트 임포트
from .api import api_bp
from .views import main_view

def create_app():   # Flask가 웹 애플리케이션을 시작할 때 자동으로 호출하는 함수
    # 환경 변수 로드
    load_dotenv()
    
    app = Flask(__name__)       # web application 만들기
    app.config['SECRET_KEY'] = 'chatbot-algi'
    
    # CORS 설정
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})
    
    # 웹페이지용 블루프린트
    app.register_blueprint(main_view.main_bp)
    
    # API 블루프린트
    app.register_blueprint(api_bp)
    
    return app
