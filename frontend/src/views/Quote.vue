<template>
  <div class="quote-container">
    <h1>오늘의 명언</h1>
    <div class="button-group">
      <button @click="$router.back()" class="chat-btn">챗봇가기</button>
    </div>

    <blockquote class="quote">
      "{{ currentQuote.text }}"
    </blockquote>
    <p class="author">- {{ currentQuote.author }}</p>

    <div class="button-group">
      <button @click="nextQuote" class="next-btn">다음 명언 보기</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'QuotePage',
  data() {
    return {
      quotes: [
        { text: "행복은 결코 외부에서 오지 않는다. 그것은 우리 내면의 상태다.", author: "달라이 라마" },
        { text: "성공의 비결은 목적의 일관성에 있다.", author: "벤자민 디즈레일리" },
        { text: "실패는 성공으로 가는 가장 빠른 길이다.", author: "토마스 왓슨" },
        { text: "작은 기회로부터 종종 위대한 업적이 시작된다.", author: "데모스테네스" },
        { text: "자신을 믿어라. 당신이 할 수 있다고 생각하든 할 수 없다고 생각하든, 당신 말이 맞다.", author: "헨리 포드" }
      ],
      currentIndex: 0
    };
  },
  computed: {
    currentQuote() {
      return this.quotes[this.currentIndex];
    }
  },
  methods: {
    nextQuote() {
      this.currentIndex = (this.currentIndex + 1) % this.quotes.length;
    }
  }
}
</script>

<style scoped>
.quote-container {
  max-width: 700px;
  margin: 40px auto;
  padding: 24px;
  background: #f8f6f5;
  border-radius: 10px;
  box-shadow: 0 8px 20px rgba(139, 99, 62, 0.76);
  text-align: center;
  font-family: 'Nanum Gothic', sans-serif;
}

h1 {
  font-weight: 700;
  font-size: 1.8rem;
  margin-bottom: 28px;
  color: #856453d8;
}

.quote {
  font-style: italic;
  font-size: 1.6rem;
  color: #8b6d5c;
  margin-bottom: 20px;
  line-height: 1.4;
}

.author {
  font-weight: 600;
  color: #a67c52;
  margin-bottom: 35px;
}

.chat-btn {
  background: #2b8a3e; /* 초록 느낌 */
  color: #fff;
  border: none;
  border-radius: 6px;
  padding: 8px 18px;
  font-size: 0.8rem;
  cursor: pointer;
  transition: background 0.2s;
  margin-bottom: 10px;
}

.chat-btn:hover {
  background: #226c2c;
}

.next-btn {
  background-color: #8b5e3c; /* 나무 느낌 브라운 */
  color: #fff;
  border: none;
  border-radius: 6px;
  padding: 10px 20px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.next-btn:hover {
  background-color: #6d4b2a;
}

.button-group {
  text-align: right;
  margin-bottom: 16px; /* 버튼 사이 적당한 간격 */
}


</style>
