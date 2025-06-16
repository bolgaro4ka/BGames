<script setup lang="ts">
import { GAMES_LIST_URL } from '@/config';
import axios from 'axios';
import GameCard from './particles/GameCard.vue';
import { ref, watchEffect } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import type { RefSymbol } from '@vue/reactivity';

const props = defineProps(['cat', 'limit']);

const route = useRoute();
const router = useRouter();

// page и limit из query или props
const page = ref(Number(route.query.page) || 1);
const limit = ref(Number(route.query.limit) || Number(props.limit) || 10);

const len = ref(1);

// Хранилище данных
const response = ref<any[]>([]);
const loading = ref(false);

// Загрузка данных при изменении page / cat
watchEffect(async () => {
  loading.value = true;
  page.value = Number(route.query.page) || 1;
  limit.value = Number(route.query.limit) || Number(props.limit) || 10;

  try {
    const res = await axios.post(GAMES_LIST_URL, {
      page: page.value,
      limit: limit.value,
      category_id: props.cat,
    });
    response.value = res.data;
  } catch (err) {
    console.error('Ошибка при загрузке игр:', err);
  } finally {
    loading.value = false;
    len.value = response.value[0].all_games
  }
});

// Кнопка следующей страницы
function handleClick(n : number) {
  router.push({
    path: '/',
    query: {
      page: page.value + n,
      limit: limit.value,
    },
  });
}
</script>

<template>
  <div class="plof__wrapper">
    

    <div class="plof__filter">
        <p>ФИЛЬТР</p>
        <div class="plof__params">
            <div class="plof__param">
                <p>Кол-во игр на странице</p>
                <input/>
            </div>
            <div class="plof__param">
                <p>Номер страницы</p>
                <input v-model="page"/>
            </div>
            <div class="plof__param">
                <p>Категории</p>
                <p>потом я устал</p>
            </div>
        </div>
    </div>
    
    <div v-if="loading">Загрузка...</div>
    <div v-else class="plof__cards">
      <div class="plof__card" v-for="config in response.slice(1)" :key="config.id">
        <GameCard :game="config" />
      </div>
    </div>

    <div class="plof__pagination">
        <div class="plof__pagination--btn" @click="handleClick(-page + 1)" v-if="page > 4">
        {{ 1  }}
      </div>
      <p v-if="page > 5">...</p>
        <div class="plof__pagination--btn" @click="handleClick(-3)" v-if="(page - 3 > 0) && (page - 3 <= Math.round(Number(len) / Number(limit)))">
        {{ page - 3  }}
      </div>
      <div class="plof__pagination--btn" @click="handleClick(-2)" v-if="(page - 2 > 0) && (page - 2 <= Math.round(Number(len) / Number(limit)))">
        {{ page - 2 }}
      </div>
      <div class="plof__pagination--btn" @click="handleClick(-1)" v-if="(page - 1 > 0) && (page - 1 <= Math.round(Number(len) / Number(limit)))">
        {{ page - 1 }}
      </div>
      <div class="plof__pagination--btn no-active">
        {{ page }}
      </div>
      <div class="plof__pagination--btn" @click="handleClick(1)" v-if="(page + 1 >= 0) && (page + 1 < Math.round(Number(len) / Number(limit)))">
        {{ page + 1 }}
      </div>
      <div class="plof__pagination--btn" @click="handleClick(2)" v-if="(page + 2 >= 0) && (page + 2 < Math.round(Number(len) / Number(limit)))">
        {{ page + 2 }}
      </div>
      <div class="plof__pagination--btn" @click="handleClick(3)" v-if="(page + 3 >= 0) && (page + 3 < Math.round(Number(len) / Number(limit)))">
        {{ page + 3 }}
      </div>
      <p v-if="page < Math.round(Number(len) / Number(limit))-4">...</p>
      <div class="plof__pagination--btn" @click="handleClick(Math.round(Number(len) / Number(limit)) - page)" v-if="page < Math.round(Number(len) / Number(limit))">
        {{ Math.round(Number(len) / Number(limit)) }}
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.plof__wrapper {
  margin: 0 auto;
  max-width: 1200px;
}
.plof__cards {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 20px;
}

.plof__pagination {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    margin: 20px 0;
    
}

.plof__pagination--btn {
    background-color: var(--background-active-start-color);
    width: 50px;
    height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all .3s;
    user-select: none;

    
}

.no-active {
    background-color: var(--second-body-background) !important;
}

.plof__pagination--btn:hover {
    background-color: var(--background-active-end-color);
    cursor: pointer;
}

</style>
