import os
from dotenv import load_dotenv

# .env 파일의 환경변수 불러오기
load_dotenv()

class Config:
    DB_HOST = os.getenv('DB_HOST')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME')
    DB_PORT = int(os.getenv('DB_PORT', 3306))  # 기본값 3306

# 사용 예시
# from config import Config
# print(Config.DB_HOST)
