<script setup lang="ts">
import Hero from '@/components/Hero.vue';
import PaginationLisfOfGames from '@/components/Games.vue';
import Categories from '@/components/Categories.vue';
import GamesLen from '@/components/GamesLen.vue';

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
      <GamesLen/>
    </Suspense>
    <Suspense>
      <PaginationLisfOfGames style="margin-top: 50px"/>
      <template #fallback>Loading...</template>
    </Suspense>
  </main>
</template>
