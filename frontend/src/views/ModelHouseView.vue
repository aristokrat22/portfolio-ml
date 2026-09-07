<script setup>
import { ref, reactive } from 'vue'
import { api } from '@/api'

const form = reactive({
  rooms: 1,
  year_built: 2020,
  has_balcony: 1,
  is_first_floor: 0,
  is_last_floor: 0,
  area_total: null,
  area_living: null,
  area_kitchen: null,
  bathroom_type: '',
  balcony_type: '',
  condition: '',
  street: ''
})

const bathroomOptions = ['Два', 'Раздельный', 'Совмещенный', 'Три']
const balconyOptions = ['Два', 'Есть', 'Лоджия', 'Нет']
const conditionOptions = ['Вторичное', 'Новое']

const streetOptions = [
  
  'Бобруйская ул', 'Богдана Хмельницкого ул', 'Болеслава Берута ул', 'Ботаническая ул', 'Братская ул',
  'Брестская ул', 'Брикета ул', 'Брилевская ул', 'Броневой переулок', 'Будённого ул', 'Бумажкова ул',
  'Бурдейного ул', 'Быховская ул', 'Валентия Ваньковича ул', 'Варвашени ул', 'Васнецова ул', 'Великоморская ул',
  'Велозаводская ул', 'Веры Хоружей ул', 'Весенняя ул', 'Виктора Турова ул', 'Виталия Цвирко ул',
  'Владимира Оловникова ул', 'Владислава Голубка ул', 'Владислава Сырокомли ул', 'Водолажского ул',
  'Войсковый переулок', 'Волгоградская ул', 'Володарского ул', 'Волоха ул', 'Воронянского ул', 'Восточная ул',
  'Всеволода Игнатовского ул', 'Выготского ул', 'Высокая ул', 'Газеты Звязда пр', 'Газеты Правда пр', 'Гало ул',
  'Гамарника ул', 'Гастелло ул', 'Гая ул', 'Гвардейская ул', 'Геологическая ул', 'Герасименко ул', 'Германовская ул',
  'Героев 120-й Дивизии ул', 'Гикало ул', 'Гинтовта ул', 'Глаголева ул', 'Голодеда ул', 'Голубева ул',
  'Горный переулок', 'Горовца ул', 'Городецкая ул', 'Городской Вал ул', 'Грекова ул', 'Грибоедова ул',
  'Гризодубовой ул', 'Грицевца ул', 'Громова ул', 'Грушевская ул', 'Гурского ул', 'Гуртьева ул',
  'Данилы Сердича ул', 'Двинская ул', 'Декабристов ул', 'Денисовская ул', 'Дзержинского пр', 'Димитрова ул',
  'Днепровская ул', 'Долгиновский проезд', 'Долгиновский тракт', 'Долгобродская ул', 'Дорошевича ул',
  'Дубравинский переулок', 'Дунина-Марцинкевича ул', 'Ежи Гедройца ул', 'Ельских ул', 'Ермака ул',
  'ЖК Вивальди', 'ЖК Левада', 'Жасминовая ул', 'Железнодорожная ул', 'Жилуновича ул', 'Жлобинская ул',
  'Жореса Алфёрова ул', 'Жудро ул', 'Жукова пр', 'Жуковского ул', 'Заводской район', 'Запорожская ул',
  'Заславская ул', 'Захарова ул', 'Зацень ул', 'Зелёный Луг-3', 'Змитрока Бядули ул', 'Зои Космодемьянской ул',
  'Игоря Лученка ул', 'Игуменский тракт', 'Илимская ул', 'Ильменская ул', 'Ильянская ул', 'Индустриальная ул',
  'Первомайская ул', 'Пермская ул', 'Петра Глебки ул', 'Петра Мстиславца ул', 'Петра Румянцева ул',
  'Пильницкая ул', 'Пимена Панченко ул', 'Пионерская ул', 'Пирогова ул', 'Платонова ул', 'Плеханова ул',
  'Победителей пр', 'Подлесная ул', 'Полевая ул', 'Пономаренко ул', 'Пономарёва ул', 'Прилукская ул',
  'Притыцкого ул', 'Программистов ул', 'Прушинских ул', 'Пугачёвская ул', 'Пулихова ул', 'Путейская ул',
  'Пуховичская ул', 'Пушкина пр', 'Рабкоровская ул', 'Радищева ул', 'Радужная ул', 'Разинская ул',
  'Раковская ул', 'Ратомская ул', 'Рафиева ул', 'Репина ул', 'Ржавецкая ул', 'Рогачёвская ул',
  'Розы Люксембург ул', 'Рокоссовского пр', 'Романовская Слобода ул', 'Ротмистрова ул', 'Руссиянова ул',
  'Рыбалко ул', 'Садовая ул', 'Свердлова ул', 'Связистов ул', 'Седова ул', 'Седых ул', 'Селицкого ул',
  'Семёнова ул', 'Серафимовича ул', 'Сергея Есенина ул', 'Серова ул', 'Скрипникова ул', 'Скрыганова ул',
  'Славинского ул', 'Слесарная ул', 'Слободская ул', 'Слободской проезд', 'Смирнова ул', 'Смолячкова ул',
  'Сморговский тракт', 'Снежный переулок', 'Советский район', 'Солтыса ул', 'Сосновый Бор ул',
  'Средиземноморский квартал', 'Стадионная ул', 'Станислава Монюшко ул', 'Станиславского ул', 'Стариновская ул',
  'Старовиленская ул', 'Старовиленский тракт', 'Стахановская ул', 'Степана Злобина ул', 'Степянская ул',
  'Столетова ул', 'Сторожовская ул', 'Сурганова ул', 'Сухаревская ул', 'Тарханова ул', 'Ташкентская ул',
 
]

const result = ref(null)
const pricePerMeter = ref(null)
const error = ref(null)
const loading = ref(false)

async function submitForm() {
  error.value = null
  result.value = null
  pricePerMeter.value = null
  loading.value = true
  try {
    const { data } = await api.post('/models/predict-price-house', form)
    result.value = data.predicted_price
    pricePerMeter.value = data.price_per_meter
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="max-w-md mx-auto p-6 pt-20 pb-32">
    <h1 class="text-2xl font-bold mb-4">Предсказание цены квартиры</h1>

    <form @submit.prevent="submitForm" class="space-y-4">
      <div>
        <label class="block text-sm font-medium mb-1">Количество комнат</label>
        <input type="number" v-model.number="form.rooms" min="1" max="5" step="1" required
          class="w-full border rounded px-3 py-2" />
        <p class="text-xs text-gray-500 mt-1">1 – 5</p>
      </div>

      <div>
        <label class="block text-sm font-medium mb-1">Год постройки</label>
        <input type="number" v-model.number="form.year_built" min="1959" max="2029" step="1" required
          class="w-full border rounded px-3 py-2" />
        <p class="text-xs text-gray-500 mt-1">1959 – 2029</p>
      </div>

      <div>
        <label class="block text-sm font-medium mb-1">Общая площадь (кв. м)</label>
        <input type="number" v-model.number="form.area_total" min="5.1" max="638.9" step="0.1" required
          class="w-full border rounded px-3 py-2" />
        <p class="text-xs text-gray-500 mt-1">5.1 – 638.9</p>
      </div>

      <div>
        <label class="block text-sm font-medium mb-1">Жилая площадь (кв. м)</label>
        <input type="number" v-model.number="form.area_living" min="5.0" max="773.0" step="0.1" required
          class="w-full border rounded px-3 py-2" />
        <p class="text-xs text-gray-500 mt-1">5.0 – 773.0</p>
      </div>

      <div>
        <label class="block text-sm font-medium mb-1">Площадь кухни (кв. м)</label>
        <input type="number" v-model.number="form.area_kitchen" min="1.0" max="83.6" step="0.1" required
          class="w-full border rounded px-3 py-2" />
        <p class="text-xs text-gray-500 mt-1">1.0 – 83.6</p>
      </div>

      <div>
        <label class="block text-sm font-medium mb-1">Балкон</label>
        <select v-model.number="form.has_balcony" required class="w-full border rounded px-3 py-2">
          <option :value="1">Есть</option>
          <option :value="0">Нет</option>
        </select>
      </div>

      <div>
        <label class="block text-sm font-medium mb-1">Первый этаж?</label>
        <select v-model.number="form.is_first_floor" required class="w-full border rounded px-3 py-2">
          <option :value="1">Да</option>
          <option :value="0">Нет</option>
        </select>
      </div>

      <div>
        <label class="block text-sm font-medium mb-1">Последний этаж?</label>
        <select v-model.number="form.is_last_floor" required class="w-full border rounded px-3 py-2">
          <option :value="1">Да</option>
          <option :value="0">Нет</option>
        </select>
      </div>

      <div>
        <label class="block text-sm font-medium mb-1">Санузел</label>
        <select v-model="form.bathroom_type" required class="w-full border rounded px-3 py-2">
          <option disabled value="">выбери</option>
          <option v-for="item in bathroomOptions" :key="item" :value="item">{{ item }}</option>
        </select>
      </div>

      <div>
        <label class="block text-sm font-medium mb-1">Тип балкона</label>
        <select v-model="form.balcony_type" required class="w-full border rounded px-3 py-2">
          <option disabled value="">выбери</option>
          <option v-for="item in balconyOptions" :key="item" :value="item">{{ item }}</option>
        </select>
      </div>

      <div>
        <label class="block text-sm font-medium mb-1">Состояние</label>
        <select v-model="form.condition" required class="w-full border rounded px-3 py-2">
          <option disabled value="">выбери</option>
          <option v-for="item in conditionOptions" :key="item" :value="item">{{ item }}</option>
        </select>
      </div>

      <div>
        <label class="block text-sm font-medium mb-1">Улица / Адрес</label>
        <input 
          list="street-list" 
          v-model="form.street" 
          placeholder="Начните вводить или выберите..." 
          required 
          class="w-full border rounded px-3 py-2" 
        />
        <datalist id="street-list">
          <option v-for="item in streetOptions" :key="item" :value="item"></option>
        </datalist>
      </div>

      <button type="submit" :disabled="loading"
        class="w-full bg-blue-600 text-white py-2 rounded disabled:opacity-50">
        {{ loading ? 'Считаю...' : 'Предсказать цену' }}
      </button>
    </form>

    <div v-if="result !== null" class="mt-4 p-3 bg-green-50 border border-green-200 rounded space-y-1">
      <div class="text-lg font-semibold text-green-800">
        Стоимость: ${{ result.toLocaleString('en-US') }}
      </div>
      <div v-if="pricePerMeter" class="text-sm text-green-700">
        Цена за кв. м: ${{ pricePerMeter.toLocaleString('en-US') }}
      </div>
    </div>

    <div v-if="error" class="mt-4 text-red-600">Ошибка: {{ error }}</div>
  </div>
</template>