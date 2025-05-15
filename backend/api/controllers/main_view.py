from flask import Blueprint, render_template, request, jsonify, session
from ..models.gemini_chat import chat_with_gemini
from ..models.gemini_chat import generate_dummy_resp
from db.data_util import save_log

main_bp = Blueprint('main', __name__, url_prefix="/")

@main_bp.route('/')
def index():
    session['history'] = []
    return render_template('index.html')

@main_bp.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("user_input", "")
    user_id = session.get('user_id', 'guest')  # 임시 user_id, 실제 로그인 연동시 수정
    history = session.get('history', [])
    response = generate_dummy_resp(user_input)
    save_log(user_id, user_input, response)
    history.append({"user": user_input, "bot": response})
    session['history'] = history
    return jsonify({'response': response})