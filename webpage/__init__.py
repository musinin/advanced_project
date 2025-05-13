from flask import Flask

from .views import main_view

def create_app():           # Flask가 웹 애플리케이션을 시작할 때 자동으로 호출하는 함수

    app = Flask(__name__)   # web application 만들기
    app.config['SECRET_KEY'] = 'chatbot-algi'

    app.register_blueprint(main_view.main_bp)

    return app