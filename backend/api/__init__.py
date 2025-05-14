from flask import Blueprint

# API 블루프린트 생성 - 모든 API 라우트를 /api 하위에 등록
api_bp = Blueprint('api', __name__, url_prefix='/api')

# 컨트롤러 등록
from .controllers.main_view import main_bp
from .controllers.data_view import data_bp

# 하위 블루프린트 등록
api_bp.register_blueprint(main_bp)
api_bp.register_blueprint(data_bp)
