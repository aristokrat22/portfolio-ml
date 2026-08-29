<script setup>
import { useRoute } from 'vue-router'
const route = useRoute()

function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}
</script>

<template>
  <div class="min-h-screen bg-white text-slate-900">
    <nav
      v-if="route.path === '/'"
      class="fixed top-6 left-1/2 -translate-x-1/2 z-50 flex gap-6 bg-slate-950/85 backdrop-blur-md text-white rounded-full px-8 py-3 shadow-lg shadow-black/20 ring-1 ring-white/10"
    >
      <router-link to="/#cv" class="hover:text-sky-400 transition">CV</router-link>
      <router-link to="/#models" class="hover:text-sky-400 transition">Models</router-link>
      <router-link to="/#contacts" class="hover:text-sky-400 transition">Contacts</router-link>
    </nav>

    <nav
      v-else
      class="fixed top-6 left-1/2 -translate-x-1/2 z-50 flex bg-slate-950/85 backdrop-blur-md text-white rounded-full px-8 py-3 shadow-lg shadow-black/20 ring-1 ring-white/10"
    >
      <router-link to="/" class="hover:text-sky-400 transition">← Home</router-link>
    </nav>

    <router-view />

      <button
      @click="scrollToTop"
      class="fixed bottom-6 right-6 bg-white hover:bg-black border-2 border-black rounded-full w-12 h-12 flex items-center justify-center transition shadow-lg group"
      >
      <span class="text-4xl font-black text-black group-hover:text-white transition">↑</span>
    </button>
  </div>
</template>