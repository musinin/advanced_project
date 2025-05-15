import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('models/gemini-1.5-pro')


def generate_dummy_resp(user_input):
    # 실제 모델 대신 임시 응답 생성
    return f"임시 응답입니다: '{user_input}'에 대한 응답은 여기 들어갑니다."

def chat_with_gemini(user_input, history):
    short_history = history[-3:]  # 최근 3개만 사용
    context = "\n".join([f"User: {h['user']}\nBot: {h['bot']}" for h in short_history])
    prompt = f"{context}\nUser: {user_input}\nBot:"

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        if "429" in str(e):
            return "오늘의 응답은 끝났습니다. (요청 한도를 초과했습니다)"
        else:
            return f"[에러 발생] {e}"
        

