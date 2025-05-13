from flask import Blueprint, render_template, request, jsonify, session
from ..model.gemini_chat import chat_with_gemini

main_bp = Blueprint('main', __name__, url_prefix="/")


@main_bp.route('/')
def index():
    session['history'] = []
    return render_template('index.html')

@main_bp.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("user_input", "")
    history = session.get('history', [])

    response = chat_with_gemini(user_input, history)

    # 대화 기록 업데이트
    history.append({"user": user_input, "bot": response})
    session['history'] = history

    return jsonify({'response': response})