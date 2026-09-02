<script setup>
import { ref, reactive } from 'vue'
import { api } from '@/api'

const form = reactive({
  study_hours: null,
  class_attendance: null,
  sleep_hours: null,
  sleep_quality: '',
  study_method: '',
  facility_rating: '',
})

const result = ref(null)
const error = ref(null)
const loading = ref(false)

async function submitForm() {
  error.value = null
  result.value = null
  loading.value = true
  try {
    const { data } = await api.post('/models/predict-price-car', form)
    result.value = data.predicted_score
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="max-w-md mx-auto p-6">
    <h1 class="text-2xl font-bold mb-4">Предсказание оценки за экзамен</h1>

    <form @submit.prevent="submitForm" class="space-y-4">
      <div>
        <label class="block text-sm font-medium mb-1">Часы подготовки</label>
        <input type="number" v-model.number="form.study_hours" min="0.08" max="7.91" step="any" required
          class="w-full border rounded px-3 py-2" />
        <p class="text-xs text-gray-500 mt-1">0.08 – 7.91</p>
      </div>

      <div>
        <label class="block text-sm font-medium mb-1">Посещаемость, %</label>
        <input type="number" v-model.number="form.class_attendance" min="40.6" max="99.4" step="any" required
          class="w-full border rounded px-3 py-2" />
        <p class="text-xs text-gray-500 mt-1">40.6 – 99.4</p>
      </div>

      <div>
        <label class="block text-sm font-medium mb-1">Часы сна</label>
        <input type="number" v-model.number="form.sleep_hours" min="4.1" max="9.9" step="any" required
          class="w-full border rounded px-3 py-2" />
        <p class="text-xs text-gray-500 mt-1">4.1 – 9.9</p>
      </div>

      <div>
        <label class="block text-sm font-medium mb-1">Качество сна</label>
        <select v-model="form.sleep_quality" required class="w-full border rounded px-3 py-2">
          <option disabled value="">выбери</option>
          <option value="poor">poor</option>
          <option value="average">average</option>
          <option value="good">good</option>
        </select>
      </div>

      <div>
        <label class="block text-sm font-medium mb-1">Метод обучения</label>
        <select v-model="form.study_method" required class="w-full border rounded px-3 py-2">
          <option disabled value="">выбери</option>
          <option value="coaching">coaching</option>
          <option value="online videos">online videos</option>
          <option value="mixed">mixed</option>
          <option value="self-study">self-study</option>
          <option value="group study">group study</option>
        </select>
      </div>

      <div>
        <label class="block text-sm font-medium mb-1">Оценка условий</label>
        <select v-model="form.facility_rating" required class="w-full border rounded px-3 py-2">
          <option disabled value="">выбери</option>
          <option value="low">low</option>
          <option value="medium">medium</option>
          <option value="high">high</option>
        </select>
      </div>

      <button type="submit" :disabled="loading"
        class="w-full bg-blue-600 text-white py-2 rounded disabled:opacity-50">
        {{ loading ? 'Считаю...' : 'Предсказать' }}
      </button>
    </form>

    <div v-if="result !== null" class="mt-4 text-lg font-semibold">
      Предсказанная оценка: {{ result.toFixed(2) }}
    </div>
    <div v-if="error" class="mt-4 text-red-600">Ошибка: {{ error }}</div>
  </div>
</template>