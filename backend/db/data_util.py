import sqlite3
import json
import os
from datetime import datetime

# 데이터베이스 파일 경로
DB_PATH = os.path.join(os.path.dirname(__file__), 'chatbot.db')

def initialize_db():
    """데이터베이스 초기화 및 테이블 생성"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # 대화 기록 테이블 생성
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS chat_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT NOT NULL,
        user_input TEXT NOT NULL,
        bot_response TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    conn.commit()
    conn.close()

def get_chat_history(user_id, limit=10):
    """사용자의 대화 기록 조회"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute(
        '''SELECT user_input, bot_response, timestamp 
           FROM chat_history 
           WHERE user_id = ? 
           ORDER BY timestamp DESC LIMIT ?''',
        (user_id, limit)
    )
    
    rows = cursor.fetchall()
    conn.close()
    
    # 기록을 사용하기 쉬운 형태로 변환
    history = [
        {
            "user": row[0],
            "bot": row[1],
            "timestamp": row[2]
        } for row in rows
    ]
    
    return history[::-1]  # 시간순 정렬

def save_chat_history(user_id, chat_data):
    """대화 기록 저장"""
    if not chat_data or 'user' not in chat_data or 'bot' not in chat_data:
        return False
        
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            'INSERT INTO chat_history (user_id, user_input, bot_response) VALUES (?, ?, ?)',
            (user_id, chat_data['user'], chat_data['bot'])
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error saving chat history: {e}")
        conn.close()
        return False

# 데이터베이스 초기화 (앱 시작 시 자동 실행)
initialize_db()
