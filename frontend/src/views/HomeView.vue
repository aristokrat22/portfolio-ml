<script setup>
import { ref, onMounted, onUnmounted} from 'vue'
import { api } from '@/api'
import photo from '@/assets/photo.jpg'

// Импорт локальных иконок
import pythonIcon from '@/assets/icons/python.svg'
import dockerIcon from '@/assets/icons/docker.svg'
import githubIcon from '@/assets/icons/github.svg'
import postgresIcon from '@/assets/icons/postgres.svg'

const rawIcons = [
  { name: 'Python', src: pythonIcon },
  { name: 'Docker', src: dockerIcon },
  { name: 'PostgreSQL', src: postgresIcon },
  { name: 'GitHub', src: githubIcon }
]
const techIcons = ref([...rawIcons])


let shuffleTimer = null

function shuffleIcons() {
  techIcons.value = [...techIcons.value].sort(() => Math.random() - 0.5)
}

onMounted(() => {
  shuffleTimer = setInterval(shuffleIcons, 3000)
})

onUnmounted(() => {
  if (shuffleTimer) clearInterval(shuffleTimer)
})


</script>

<template>
<section id="cv" class="min-h-screen relative flex flex-col pt-16 pb-16 border-b-2 bg-teal-800 text-white px-4">
  
  <div class="w-full max-w-4xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-6 sm:gap-12 mt-12 sm:mt-0">
    
    <div class="flex-shrink-0">
      <img 
        :src="photo" 
        alt="Photo" 
        class="w-20 h-20 sm:w-28 sm:h-28 rounded-full object-cover border-4 border-white shadow-lg" 
        style="object-position: center 40%;" 
      />
    </div>

    <div class="flex-grow text-center sm:text-left">
      <h2 class="text-3xl font-bold mb-4">Resume</h2>
      <ul class="space-y-1.5 text-base sm:text-lg inline-block text-left sm:block">
        <li>- Python (core)</li>
        <li>- SQL (Postgres)</li>
        <li>- ML (CatBoost, MLflow)</li>
        <li>- Backend (FastAPI)</li>
        <li>- Frontend (Vite, Vue.js)</li>
        <li>- Docker (Dockerfile, Docker-compose)</li>
        <li>- Git</li>
      </ul>
    </div>
  </div>

<TransitionGroup 
    tag="div" 
    name="shuffle"
    class="absolute bottom-[10%] left-0 right-0 flex justify-center items-center gap-3 sm:gap-5 px-4"
  >
    <div 
      v-for="icon in techIcons" 
      :key="icon.name"
      class="w-12 h-12 sm:w-16 sm:h-16 rounded-xl bg-teal-900/60 p-2 sm:p-2.5 flex items-center justify-center border border-teal-600/40 shadow-sm transition-transform duration-700 ease-in-out cursor-pointer"
      :title="icon.name"
    >
      <img 
        :src="icon.src" 
        :alt="icon.name" 
        :class="['w-full h-full object-contain', icon.name === 'GitHub' ? 'brightness-0 invert' : '']" 
      />
    </div>
  </TransitionGroup>
</section>


<section id="models" class="min-h-screen flex items-center justify-center scroll-mt-24 border-b-2 border-slate-900 bg-white text-slate-900 py-12">
    <div class="w-[90%] max-w-4xl h-[85vh] mx-auto flex items-center justify-center">
      <!-- Внутренняя рамка: контент поднят вверх через items-start pt-10 sm:pt-14 -->
      <div class="border-4 border-double border-slate-900 w-full h-full flex items-start justify-center p-6 sm:p-10 pt-12 sm:pt-16 overflow-y-auto">
        <div class="font-mono w-full max-w-xl">
          
          <!-- Заголовок -->
          <h2 class="text-2xl sm:text-3xl font-bold mb-2 flex items-center gap-2">
            <span>ML-models</span> <span>📁</span>
          </h2>

          <!-- Пунктирная ветка дерева, начинающаяся прямо под папкой -->
          <div class="ml-4 pl-6 sm:pl-8 border-l-2 border-dashed border-slate-400 mt-6 space-y-16 pt-10">
            
            <!-- Модель 1: Predict-price-house -->
            <div class="relative">
              <!-- Горизонтальный отвод от пунктира -->
              <span class="absolute -left-[25px] sm:-left-[33px] top-3 w-4 sm:w-6 border-t-2 border-dashed border-slate-400"></span>

              <div class="space-y-3">
                <router-link to="/models/predict-price-house" class="text-lg sm:text-xl font-bold text-slate-900 hover:text-blue-600 transition inline-flex items-center gap-2">
                  <span>Pred.-price-house</span>
                  <span>🏠</span>
                </router-link>

                <!-- Кнопки: Try it + GitHub -->
                <div class="flex items-center gap-3 pt-1">
                  <router-link 
                    to="/models/predict-price-house"
                    class="inline-flex items-center gap-1.5 px-4 py-1.5 bg-emerald-500 hover:bg-emerald-600 text-white text-xs sm:text-sm font-semibold rounded-lg shadow-sm hover:shadow transition transform active:scale-95"
                  >
                    <span>▶</span> Try it
                  </router-link>

                  <a 
                    href="https://github.com/aristokrat22/portfolio-ml" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-slate-100 hover:bg-slate-200 border border-slate-300 text-slate-700 text-xs sm:text-sm font-medium rounded-lg transition"
                  >
                    <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24">
                      <path d="M12 2C6.48 2 2 6.58 2 12.25c0 4.53 2.87 8.37 6.84 9.73.5.1.68-.22.68-.49 0-.24-.01-.87-.01-1.71-2.78.62-3.37-1.36-3.37-1.36-.45-1.18-1.11-1.5-1.11-1.5-.91-.64.07-.63.07-.63 1 .07 1.53 1.05 1.53 1.05.89 1.57 2.34 1.11 2.91.85.09-.67.35-1.11.63-1.37-2.22-.26-4.56-1.14-4.56-5.05 0-1.12.39-2.03 1.03-2.75-.1-.26-.45-1.3.1-2.71 0 0 .84-.28 2.75 1.05a9.3 9.3 0 0 1 5 0c1.9-1.33 2.75-1.05 2.75-1.05.55 1.41.2 2.45.1 2.71.64.72 1.03 1.63 1.03 2.75 0 3.92-2.34 4.78-4.57 5.04.36.32.68.94.68 1.9 0 1.37-.01 2.48-.01 2.82 0 .27.18.6.69.49A10.03 10.03 0 0 0 22 12.25C22 6.58 17.52 2 12 2z"/>
                    </svg>
                    <span>GitHub</span>
                  </a>
                </div>
              </div>
            </div>

            <!-- Модель 2: Predict-price-car -->
            <div class="relative">
              <!-- Горизонтальный отвод от пунктира -->
              <span class="absolute -left-[25px] sm:-left-[33px] top-3 w-4 sm:w-6 border-t-2 border-dashed border-slate-400"></span>

              <div class="space-y-3">
                <router-link to="/models/predict-price-car" class="text-lg sm:text-xl font-bold text-slate-900 hover:text-blue-600 transition inline-flex items-center gap-2">
                  <span>Pred.-price-car</span>
                  <span>🚗</span>
                </router-link>

                <!-- Кнопки: Try it + GitHub -->
                <div class="flex items-center gap-3 pt-1">
                  <router-link 
                    to="/models/predict-price-car"
                    class="inline-flex items-center gap-1.5 px-4 py-1.5 bg-emerald-500 hover:bg-emerald-600 text-white text-xs sm:text-sm font-semibold rounded-lg shadow-sm hover:shadow transition transform active:scale-95"
                  >
                    <span>▶</span> Try it
                  </router-link>

                  <a 
                    href="https://github.com/aristokrat22/portfolio-ml" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-slate-100 hover:bg-slate-200 border border-slate-300 text-slate-700 text-xs sm:text-sm font-medium rounded-lg transition"
                  >
                    <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24">
                      <path d="M12 2C6.48 2 2 6.58 2 12.25c0 4.53 2.87 8.37 6.84 9.73.5.1.68-.22.68-.49 0-.24-.01-.87-.01-1.71-2.78.62-3.37-1.36-3.37-1.36-.45-1.18-1.11-1.5-1.11-1.5-.91-.64.07-.63.07-.63 1 .07 1.53 1.05 1.53 1.05.89 1.57 2.34 1.11 2.91.85.09-.67.35-1.11.63-1.37-2.22-.26-4.56-1.14-4.56-5.05 0-1.12.39-2.03 1.03-2.75-.1-.26-.45-1.3.1-2.71 0 0 .84-.28 2.75 1.05a9.3 9.3 0 0 1 5 0c1.9-1.33 2.75-1.05 2.75-1.05.55 1.41.2 2.45.1 2.71.64.72 1.03 1.63 1.03 2.75 0 3.92-2.34 4.78-4.57 5.04.36.32.68.94.68 1.9 0 1.37-.01 2.48-.01 2.82 0 .27.18.6.69.49A10.03 10.03 0 0 0 22 12.25C22 6.58 17.52 2 12 2z"/>
                    </svg>
                    <span>GitHub</span>
                  </a>
                </div>
              </div>
            </div>

          </div>

        </div>
      </div>
    </div>
  </section>

<section id="contacts" class="min-h-screen flex items-center justify-center bg-slate-800 text-white">
  <div class="w-[80%] mx-auto text-center">
    <h2 class="text-3xl font-bold mb-8">Contacts</h2>

    <div class="flex justify-center gap-6">
      <a href="https://instagram.com/a.ristokrat" target="_blank" rel="noopener noreferrer"
         class="w-14 h-14 rounded-full bg-slate-600 hover:bg-pink-500 flex items-center justify-center transition">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6">
          <path d="M7.75 2h8.5A5.75 5.75 0 0 1 22 7.75v8.5A5.75 5.75 0 0 1 16.25 22h-8.5A5.75 5.75 0 0 1 2 16.25v-8.5A5.75 5.75 0 0 1 7.75 2zm0 1.5A4.25 4.25 0 0 0 3.5 7.75v8.5a4.25 4.25 0 0 0 4.25 4.25h8.5a4.25 4.25 0 0 0 4.25-4.25v-8.5a4.25 4.25 0 0 0-4.25-4.25h-8.5zM12 7a5 5 0 1 1 0 10 5 5 0 0 1 0-10zm0 1.5a3.5 3.5 0 1 0 0 7 3.5 3.5 0 0 0 0-7zm5.25-.88a1.13 1.13 0 1 1 0-2.25 1.13 1.13 0 0 1 0 2.25z"/>
        </svg>
      </a>

      <a href="https://t.me/Aristokrat44" target="_blank" rel="noopener noreferrer"
         class="w-14 h-14 rounded-full bg-slate-600 hover:bg-sky-500 flex items-center justify-center transition">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6">
          <path d="M21.94 4.36a1.5 1.5 0 0 0-1.6-.2L2.68 11.4a1.5 1.5 0 0 0 .1 2.8l4.6 1.5 1.78 5.6a1.2 1.2 0 0 0 2.1.36l2.53-2.9 4.6 3.4a1.5 1.5 0 0 0 2.36-.9l3.1-15a1.5 1.5 0 0 0-.31-1.9zM9.4 14.9l-.02.02L8 19l-1.3-4.1L17.9 7.6 9.4 14.9z"/>
        </svg>
      </a>

      <a href="https://github.com/aristokrat22" target="_blank" rel="noopener noreferrer"
         class="w-14 h-14 rounded-full bg-slate-600 hover:bg-slate-600 flex items-center justify-center transition">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6">
          <path d="M12 2C6.48 2 2 6.58 2 12.25c0 4.53 2.87 8.37 6.84 9.73.5.1.68-.22.68-.49 0-.24-.01-.87-.01-1.71-2.78.62-3.37-1.36-3.37-1.36-.45-1.18-1.11-1.5-1.11-1.5-.91-.64.07-.63.07-.63 1 .07 1.53 1.05 1.53 1.05.89 1.57 2.34 1.11 2.91.85.09-.67.35-1.11.63-1.37-2.22-.26-4.56-1.14-4.56-5.05 0-1.12.39-2.03 1.03-2.75-.1-.26-.45-1.3.1-2.71 0 0 .84-.28 2.75 1.05a9.3 9.3 0 0 1 5 0c1.9-1.33 2.75-1.05 2.75-1.05.55 1.41.2 2.45.1 2.71.64.72 1.03 1.63 1.03 2.75 0 3.92-2.34 4.78-4.57 5.04.36.32.68.94.68 1.9 0 1.37-.01 2.48-.01 2.82 0 .27.18.6.69.49A10.03 10.03 0 0 0 22 12.25C22 6.58 17.52 2 12 2z"/>
        </svg>
      </a>
    </div>
  </div>
</section>
</template>