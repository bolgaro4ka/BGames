<script setup lang="ts">
import Hero from '@/components/Hero.vue';
import PaginationLisfOfGames from '@/components/Games.vue';
import Categories from '@/components/Categories.vue';

</script>

<template>
  <main>
    <Suspense>
      <Hero/>
      <template #fallback>Loading...</template>
    </Suspense>
    <Suspense>
      <Categories/>
    </Suspense>
    <Suspense>
      <PaginationLisfOfGames/>
      <template #fallback>Loading...</template>
    </Suspense>
  </main>
</template>
