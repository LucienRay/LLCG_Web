<template>
  <div class="container">
    <h1>LLCG 程式碼生成器</h1>

    <textarea
        v-model="prompt"
        :disabled="isLoading"
        placeholder="請輸入自然語言描述..."
        rows="5"
        cols="60"
    ></textarea>

    <button @click="generate" :disabled="isLoading">
      {{ isLoading ? '產生中...' : '產生程式碼' }}
    </button>

    <pre>{{ result }}</pre>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const prompt = ref('')
const result = ref('')
const isLoading = ref(false)

const generate = async () => {
  isLoading.value = true
  result.value = '' // 清空前次內容（可選）
  try {
    const res = await axios.post('http://localhost:5000/generate', {
      prompt: prompt.value
    })
    result.value = res.data.code
  } catch (err) {
    result.value = '# 發生錯誤，請稍後再試'
    console.error(err)
  } finally {
    isLoading.value = false
  }
}
</script>

<style>
.container {
  margin: 20px;
  font-family: Arial, sans-serif;
}
textarea {
  width: 100%;
  font-size: 16px;
  margin-bottom: 10px;
}
textarea[disabled] {
  background-color: #eee;
}
button {
  padding: 8px 16px;
  font-size: 16px;
  margin-bottom: 10px;
}
button[disabled] {
  opacity: 0.6;
  cursor: not-allowed;
}
pre {
  background: #000000;
  color: #ffffff;
  padding: 10px;
  text-align: left;
  white-space: pre-wrap;
}
</style>
