import { createRouter, createWebHistory } from 'vue-router'
import ChatBot from '@/views/ChatBot.vue'
import QuotePage from '@/views/Quote.vue';  // 새로 만들 화면 컴포넌트

const routes = [
  {
    path: '/',
    name: 'ChatBot',
    component: ChatBot
  },
  {
    path: '/quote',
    name: 'QuotePage',
    component: QuotePage
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
