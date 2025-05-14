from flask import Blueprint, request, jsonify, session
from ...db.data_util import save_chat_history, get_chat_history

data_bp = Blueprint('data', __name__, url_prefix="/history")

@data_bp.route('/', methods=['GET'])
def get_history():
    """사용자의 대화 기록을 조회하는 API"""
    # 세션에서 사용자 ID 가져오기 (실제 환경에서는 인증 시스템 연동 필요)
    user_id = session.get('user_id', 'anonymous')
    
    # 기록 조회
    history = get_chat_history(user_id)
    return jsonify({'history': history})

@data_bp.route('/save', methods=['POST'])
def save_history():
    """대화 기록을 저장하는 API"""
    user_id = session.get('user_id', 'anonymous')
    chat_data = request.json
    
    success = save_chat_history(user_id, chat_data)
    return jsonify({'success': success})
