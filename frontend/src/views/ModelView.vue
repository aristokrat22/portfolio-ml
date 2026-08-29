<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { api } from '@/api'

const route = useRoute()
const message = ref(null)
const error = ref(null)

onMounted(async () => {
  try {
    const { data } = await api.get(`/models/${route.params.modelId}`)
    message.value = data.message
  } catch (e) {
    error.value = e.message
  }
})
</script>

<template>
  <div class="min-h-screen flex items-center justify-center">
    <div class="text-center">
      <h1 class="text-2xl font-bold mb-4">{{ route.params.modelId }}</h1>
      <p v-if="message">{{ message }}</p>
      <p v-else-if="error" class="text-red-500">Ошибка: {{ error }}</p>
      <p v-else>Загрузка...</p>
    </div>
  </div>
</template>