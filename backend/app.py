# backend/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from dotenv import load_dotenv

from api.controllers.main_view import main_bp

# 환경 변수 로드
load_dotenv()

# Flask 앱 생성 함수
def create_app():
    app = Flask(__name__, 
                static_folder='static', 
                template_folder='templates')
    
    # CORS 설정 - Vue.js 프론트엔드와 통신 허용
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})

    @app.route('/')
    def home():
        return 'Hello, Flask!'
    
    # API 라우트 설정
    @app.route('/api/test', methods=['GET'])
    def test_api():
        return jsonify({"message": "Flask API 연결 성공!"})
    
    # 여기에 추가 API 엔드포인트 정의
    
    return app

# 앱 실행
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)