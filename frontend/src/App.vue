<template>
  <div class="container">
    <h1>LLCG 程式碼生成器</h1>
    <textarea v-model="prompt" placeholder="請輸入自然語言描述..." rows="5" cols="60" />
    <button @click="generate">產生程式碼</button>
    <pre>{{ result }}</pre>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const prompt = ref('')
const result = ref('')

const generate = async () => {
  const res = await axios.post('http://localhost:5000/generate', { prompt: prompt.value })
  result.value = res.data.code
}
</script>

<style>
.container {
  margin: 20px;
}
textarea {
  width: 100%;
  font-size: 16px;
}
pre {
  background: #f0f0f0;
  padding: 10px;
}
</style>
