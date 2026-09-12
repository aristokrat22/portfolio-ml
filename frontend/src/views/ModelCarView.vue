<script setup>
import { ref, reactive } from 'vue'
import { api } from '@/api'

const form = reactive({
  brand: '',
  model: '',
  regdate: 2018,
  mileage: null,
  capacity: 2.0,
  engine: '',
  gearbox: '',
  body_type: '',
  drive: ''
})

const engineOptions = ['Бензин', 'Дизель', 'Гибрид', 'Электро']
const gearboxOptions = ['Механика', 'Автомат', 'Робот', 'Вариатор']
const bodyTypeOptions = ['Седан', 'Внедорожник', 'Универсал', 'Хэтчбек', 'Купе', 'Минивэн', 'Лифтбек', 'Пикап']
const driveOptions = ['Передний', 'Задний', 'Полный']

const result = ref(null)
const error = ref(null)
const loading = ref(false)

async function submitForm() {
  error.value = null
  result.value = null
  loading.value = true
  try {
    const { data } = await api.post('/models/predict-price-car', form)
    result.value = data.predicted_price
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="max-w-md mx-auto p-6 pt-20 pb-32">
    <router-link 
      to="/" 
      class="inline-flex items-center gap-1.5 text-sm font-medium text-slate-500 hover:text-slate-900 mb-4 transition"
    >
      ← На главную
    </router-link>

    <h1 class="text-2xl font-bold mb-6">Предсказание цены автомобиля</h1>

    <form @submit.prevent="submitForm" class="space-y-4">
      <div>
        <label class="block text-sm font-medium mb-1">Марка авто</label>
        <input 
          type="text" 
          v-model="form.brand" 
          placeholder="Например: Volkswagen, BMW, Geely..." 
          required 
          class="w-full border rounded px-3 py-2" 
        />
      </div>

      <div>
        <label class="block text-sm font-medium mb-1">Модель</label>
        <input 
          type="text" 
          v-model="form.model" 
          placeholder="Например: Passat, X5, Coolray..." 
          required 
          class="w-full border rounded px-3 py-2" 
        />
      </div>

      <div>
        <label class="block text-sm font-medium mb-1">Год выпуска</label>
        <input 
          type="number" 
          v-model.number="form.regdate" 
          min="1970" 
          max="2026" 
          step="1" 
          required 
          class="w-full border rounded px-3 py-2" 
        />
        <p class="text-xs text-gray-500 mt-1">1970 – 2026</p>
      </div>

      <div>
        <label class="block text-sm font-medium mb-1">Пробег (км)</label>
        <input 
          type="number" 
          v-model.number="form.mileage" 
          min="0" 
          max="1000000" 
          step="100" 
          required 
          class="w-full border rounded px-3 py-2" 
        />
      </div>

      <div>
        <label class="block text-sm font-medium mb-1">Объем двигателя (л)</label>
        <input 
          type="number" 
          v-model.number="form.capacity" 
          min="0.5" 
          max="8.0" 
          step="0.1" 
          required 
          class="w-full border rounded px-3 py-2" 
        />
        <p class="text-xs text-gray-500 mt-1">Например: 1.6, 2.0, 3.0</p>
      </div>

      <div>
        <label class="block text-sm font-medium mb-1">Тип двигателя / топлива</label>
        <select v-model="form.engine" required class="w-full border rounded px-3 py-2">
          <option disabled value="">выбери</option>
          <option v-for="item in engineOptions" :key="item" :value="item">{{ item }}</option>
        </select>
      </div>

      <div>
        <label class="block text-sm font-medium mb-1">Коробка передач</label>
        <select v-model="form.gearbox" required class="w-full border rounded px-3 py-2">
          <option disabled value="">выбери</option>
          <option v-for="item in gearboxOptions" :key="item" :value="item">{{ item }}</option>
        </select>
      </div>

      <div>
        <label class="block text-sm font-medium mb-1">Тип кузова</label>
        <select v-model="form.body_type" required class="w-full border rounded px-3 py-2">
          <option disabled value="">выбери</option>
          <option v-for="item in bodyTypeOptions" :key="item" :value="item">{{ item }}</option>
        </select>
      </div>

      <div>
        <label class="block text-sm font-medium mb-1">Привод</label>
        <select v-model="form.drive" required class="w-full border rounded px-3 py-2">
          <option disabled value="">выбери</option>
          <option v-for="item in driveOptions" :key="item" :value="item">{{ item }}</option>
        </select>
      </div>

      <button 
        type="submit" 
        :disabled="loading"
        class="w-full bg-blue-600 hover:bg-blue-700 text-white py-2.5 rounded font-medium disabled:opacity-50 transition"
      >
        {{ loading ? 'Считаю...' : 'Предсказать цену' }}
      </button>
    </form>

    <div v-if="result !== null" class="mt-6 p-4 bg-green-50 border border-green-200 rounded-lg space-y-1">
      <div class="text-xs font-semibold text-green-700 uppercase tracking-wide">Результат оценки:</div>
      <div class="text-2xl font-bold text-green-800">
        ${{ result.toLocaleString('en-US') }}
      </div>
    </div>

    <div v-if="error" class="mt-4 p-3 bg-red-50 border border-red-200 text-red-600 rounded">
      Ошибка: {{ error }}
    </div>
  </div>
</template>