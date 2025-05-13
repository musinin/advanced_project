const form = document.getElementById('chat-form');
const chatBox = document.getElementById('chat-box');
const input = document.getElementById('user_input');

form.onsubmit = async (e) => {
    e.preventDefault();
    const userMsg = input.value.trim();
    if (!userMsg) return;

    // 사용자 메시지 추가
    chatBox.innerHTML += `<div class="message user"><b>나:</b> ${userMsg}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
    input.value = "";

    // 서버에 전송
    const res = await fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_input: userMsg })
    });

    const data = await res.json();

    // 봇 응답 추가
    chatBox.innerHTML += `<div class="message bot"><b>챗봇:</b> ${data.response}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
};
