from flask import Blueprint, request, jsonify, session
from db.data_util import save_log, get_chat_history

data_bp = Blueprint('data', __name__, url_prefix="/history")


# ------------- 사용자의 대화 기록을 조회하는 API -----------

@data_bp.route('/', methods=['GET'])
def get_history():
    user_id = session.get('user_id', 'anonymous')   # 세션에서 사용자 ID 가져오기 (실제 환경에서는 인증 시스템 연동 필요)
    # 기록 조회
    history = get_chat_history(user_id)
    return jsonify({'history': history})

# ----------------- 대화 기록을 저장하는 API ----------------
@data_bp.route('/save', methods=['POST'])
def save_history():
    user_id = session.get('user_id', 'anonymous')
    data = request.json
    user_input = data.get('user_input', '')
    bot_response = data.get('bot_response', '')
    save_log(user_id, user_input, bot_response)
    return jsonify({'success': True})
