<script setup lang="ts">
import Hero from '@/components/Hero.vue';
import Games from '@/components/Games.vue';
import Categories from '@/components/Categories.vue';
import GamesLen from '@/components/GamesLen.vue';
import { useRoute } from 'vue-router';

const route = useRoute();

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
      <Games style="margin-top: 50px" :page="route.query.page" :limit="route.query.limit"/>
      <template #fallback>Loading...</template>
    </Suspense>
  </main>
</template>
