<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';
</script>

<template>
  <Header />
  <div class="content">
    <Suspense>
      <RouterView />
    </Suspense>
  </div>
  <Footer/>
  
</template>

<style lang="scss" scoped>
  .content {
    min-height: calc(100vh - 126px);
  }
</style>
