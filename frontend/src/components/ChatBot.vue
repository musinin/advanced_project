<template>
  <div class="chatbot-container">
    <h1>하루하루</h1>
    <div class="chat-box" ref="chatBox">
      <div v-for="(msg, i) in messages" :key="i" :class="['chat-message', msg.type]">
        <b>{{ msg.type === 'user' ? '나' : '챗봇' }}:</b> {{ msg.text }}
      </div>
    </div>
    <form @submit.prevent="sendMessage" class="chat-form">
      <input
        v-model="userInput"
        type="text"
        placeholder="메시지를 입력하세요"
        autocomplete="off"
        required
        class="chat-input"
        :disabled="isLoading"
        @keyup.enter="sendMessage"
      />
      <button type="submit" class="chat-btn" :disabled="isLoading">보내기</button>
    </form>
  </div>
</template>

<script>
import api from '@/services/api'; // axios로 Flask API 연결

export default {
  name: 'ChatBot',
  data() {
    return {
      messages: [],
      userInput: '',
      isLoading: false
    };
  },
  methods: {
    async sendMessage() {
      if (!this.userInput.trim() || this.isLoading) return;
      this.isLoading = true;  // 전송 중 비활성화
      this.messages.push({ type: 'user', text: this.userInput });

      try {
        const res = await api.sendMessage(this.userInput);
        this.messages.push({ type: 'bot', text: res.data.response });
      } catch (e) {
        this.messages.push({ type: 'bot', text: '오류가 발생했습니다.' });
      }
      this.userInput = '';
      this.isLoading = false; // 응답 오면 다시 활성화
      this.$nextTick(() => {
        const box = this.$refs.chatBox;
        box.scrollTop = box.scrollHeight;
      });
    }
  }
};
</script>

<style scoped>
.chatbot-container {
  max-width: 500px;
  margin: 40px auto;
  padding: 24px;
  border-radius: 12px;
  background: #fff;
  box-shadow: 0 4px 24px rgba(0,0,0,0.08);
}
h1 {
  font-size: 1.5rem;
  margin-bottom: 16px;
  text-align: center;
}
.chat-box {
  height: 300px;
  overflow-y: auto;
  border: 1px solid #eee;
  border-radius: 8px;
  padding: 12px;
  background: #f9f9f9;
  margin-bottom: 18px;
}
.chat-message {
  margin-bottom: 10px;
  line-height: 1.6;
}
.chat-message.user {
  text-align: right;
  color: #2b8a3e;
}
.chat-message.bot {
  text-align: left;
  color: #3b3b3b;
}
.chat-form {
  display: flex;
  gap: 8px;
}
.chat-input {
  flex: 1;
  padding: 8px 12px;
  border-radius: 6px;
  border: 1px solid #ccc;
  font-size: 1rem;
}
.chat-btn {
  background: #2b8a3e;
  color: #fff;
  border: none;
  border-radius: 6px;
  padding: 8px 18px;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.2s;
}
.chat-btn:hover {
  background: #226c2c;
}
</style>
