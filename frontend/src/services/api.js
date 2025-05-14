// frontend/src/services/api.js
import axios from 'axios';

const API_URL = 'http://localhost:5000';

export default {
  // 챗봇에 메시지 전송
  sendMessage(userInput) {
    return axios.post(`${API_URL}/chat`, { user_input: userInput });
  },
  
  // 대화 기록 조회
  getHistory() {
    return axios.get(`${API_URL}/api/history`);
  }
};