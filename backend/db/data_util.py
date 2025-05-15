import pymysql
from datetime import datetime
from config import Config

# ------------------ DB 불러오기 -------------------
def get_db_connection():
    return pymysql.connect(
        host=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_NAME,
        port=Config.DB_PORT,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

# ------------------ 로그 저장 -------------------
def save_log(user_id, user_input, response):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            sql = '''
                INSERT INTO chat_history 
                (user_id, user_input, bot_response) 
                VALUES (%s, %s, %s)
            '''
            cursor.execute(sql, (user_id, user_input, response))
        conn.commit()
    except Exception as e:
        print(f"로그 저장 오류: {e}")
    finally:
        conn.close()

# ------------------ 대화 기록 조회 -------------------
def get_chat_history(user_id, limit=10):
    
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute('''
                SELECT user_input, bot_response, timestamp 
                FROM chat_history 
                WHERE user_id = %s 
                ORDER BY timestamp DESC 
                LIMIT %s
            ''', (user_id, limit))
            result = cursor.fetchall()
        return result
    finally:
        conn.close()