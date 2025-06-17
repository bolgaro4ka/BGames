<script setup lang="ts">
import { GAMES_LIST_URL, GET_CATS } from '@/config';
import axios from 'axios';
import GameCard from './particles/GameCard.vue';
import { ref, watchEffect } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import type { Ref, RefSymbol } from '@vue/reactivity';
import Logo from './Logo.vue';
import Loader from './Loader.vue';

const props = defineProps(['cat', 'limit', 'cat_id', 'query']);

const route = useRoute();
const router = useRouter();

// page и limit из query или props
const page = ref(Number(route.query.page) || 1);
const limit = ref(Number(route.query.limit) || Number(props.limit) || 10);

const cat_id = ref(Number(route.query.cat_id) || Number(props.cat) || Number(route.query.cat) || -1)
const query = ref(route.query.query || props.query || '')


const pageEl : Ref<HTMLInputElement | null> = ref(null)
const limitEl : Ref<HTMLInputElement | null> = ref(null)
const cat_idEl : Ref<HTMLInputElement | null> = ref(null)
const queryEl : Ref<HTMLInputElement | null> = ref(null)

const len = ref(1);

// Хранилище данных
const response = ref<any[]>([]);
const loading = ref(false);

const cats = await axios.get(GET_CATS).then(res => res.data)

// Загрузка данных при изменении page / cat
watchEffect(async () => {
  loading.value = true;
  page.value = Number(route.query.page) || 1;
  limit.value = Number(route.query.limit) || Number(props.limit) || 10;

  cat_id.value = Number(route.query.cat_id) || Number(props.cat_id) || Number(props.cat) || Number(route.query.cat) || -1
  query.value = route.query.query || props.query || ''

  if (limit.value > 200) {
    limit.value = 200
  }

  console.log('upd', page.value, limit.value, cat_id.value, query.value)

  try {
    const res = await axios.post(GAMES_LIST_URL, {
      page: page.value,
      limit: limit.value,
      category_id: cat_id.value,
      query: query.value
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
    path: route.path,
    query: {
      page: page.value + n,
      limit: limit.value,
      query: query.value,
      cat_id: cat_id.value,

    },
  });
}

function handleFind() {
  if (Number((limitEl.value as HTMLInputElement).value) >= 200) {
    (limitEl.value as HTMLInputElement).value = '200'
  }



  router.push({
    path: route.path,
    query: {
      page: (pageEl.value as HTMLInputElement).value,
      limit: (limitEl.value as HTMLInputElement).value,
      query: (queryEl.value as HTMLInputElement).value,
      cat_id: (cat_idEl.value as HTMLInputElement).value,
    },
  });
}

function handleReset() {
  router.push({
    path: route.path,
    query: {
      page: page.value,
      limit: limit.value,
      query: '',
      cat_id: -1,
    },
  });
}

function scrollToTop() {
  const target = document.getElementById('games');
  if (target) {
    target.scrollIntoView({ behavior: 'smooth' });
  }
}

</script>

<template>
  <div class="plof__wrapper" id="games">
    

    <div class="plof__filter">
        <p>ФИЛЬТР</p>
        <div class="plof__params">
            <div class="plof__param">
                <p>Игр на странице</p>
                <input type="number" ref="limitEl" :value="limit"/>
            </div>
            <div class="plof__param">
                <p>Номер страницы</p>
                <input type="number" ref="pageEl" :value="page"/>
            </div>
            <div class="plof__param">
                <p>Категории</p>

                  <select name="select" ref="cat_idEl" :value="cat_id">
                    <option :value="-1">Не выбрано</option>
                    <option :value="cat.id" v-for="cat in cats">{{ cat.name }}</option>
                </select>
            </div>
            <div class="plof__param">
                <p>Поиск</p>
                <input type="text" ref="queryEl" :value="query">
            </div>
            <div class="plof__actions">
              <button @click="handleFind" class="plof__actions-find">Найти</button>
              <button @click="handleReset" class="plof__actions-reset">Сбросить фильтры</button>
            </div>
        </div>
    </div>
    
    <div v-if="loading" class="plof__loading">
      <Loader/>
    </div>
    <div v-else-if="!loading && response.slice(1).length == 0" class="plof__404">
      <Logo/>
      <p>Игр по запросу не найдено</p>

    </div>
    <div v-else class="plof__cards">
      <div class="plof__card" v-for="config in response.slice(1)" :key="config.id">
        <GameCard :game="config" :cats/>
      </div>
    </div>

    <div class="plof__pagination">
      <div class="plof__pagination--btn no-active"  @click="scrollToTop" title="Вверх">
        <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M440-160v-487L216-423l-56-57 320-320 320 320-56 57-224-224v487h-80Z"/></svg>
      </div>
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
      <div class="plof__pagination--btn no-active"  @click="scrollToTop" aria-label="вверх"  title="Вверх">
        <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M440-160v-487L216-423l-56-57 320-320 320 320-56 57-224-224v487h-80Z"/></svg>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.plof__wrapper {
  margin: 0 auto;
  max-width: 900px;
}

.plof__loading {
  display: flex;
  align-items: center;
  justify-content: center;
}

.plof__filter {
  background-color: var(--second-body-background);
  margin-bottom: 20px;
  padding: 10px;

  .plof__params {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .plof__param {
    display: flex;
    flex-direction: column;
  }

  .plof__param input, .plof__param select, .plof__param option {
    background-color: var(--body-color);
    border: none;
    outline: none;
    padding: 5px 5px;
  }
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

.plof__404 {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  gap: 5px;
}

.plof__actions {
  .plof__actions-find {
    background: linear-gradient(90deg, var(--background-active-start-color) 0%, var(--background-active-end-color) 100%);
    border: none;
    outline: none;
    padding: 10px 20px;
  }

  .plof__actions-reset {
    background-color: var(--body-color);
    border: none;
    outline: none;
    padding: 10px 20px;
  }
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
