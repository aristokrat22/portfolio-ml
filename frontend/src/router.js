import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ModelHouseView from '@/views/ModelHouseView.vue'
import ModelCarView from '@/views/ModelCarView.vue'


const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: HomeView },
    { path: '/models/predict-price-car', component: ModelCarView },
    { path: '/models/predict-price-house', component: ModelHouseView },
  ],
  scrollBehavior(to) {
    if (to.hash) {
      return { el: to.hash, behavior: 'smooth' }
    }
    return { top: 0 }
  },
})

export default router