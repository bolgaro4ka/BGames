<script setup lang="ts">
import { GET_GAME_BY_ID_URL } from '@/config';
import { Swiper, SwiperSlide } from 'swiper/vue';
import axios from 'axios';
import { ref, type Ref } from 'vue';
import SearchResults from './SearchResults.vue';

function getRandomInt(min: number, max: number) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

const res = await axios.get(GET_GAME_BY_ID_URL + getRandomInt(34, 1600) + '/').then(res => {
    return res.data
})

const games = [
    {id: 91, image: '/trend_games/91.jpg',},
    {id: 97, image: '/trend_games/97.avif',},
    {id: 49, image: '/trend_games/49.jpg'},
    {id: 78, image: '/trend_games/78.jpg'},
    {id: 2417, image: '/trend_games/2417.jpg'},
    {id:2558,image: '/trend_games/2558.jpg'},
    {id:2222, image: '/trend_games/2222.avif'},
    {id:4, image: '/trend_games/4n.jpg'},
]

interface Game {
    id: number;
    image: string;
}

const game: Ref<Game> = ref(games[getRandomInt(0, games.length - 1)] as Game);

const query = ref('');

</script>

<template>
    <div class="hero__wrapper">
        <div class="hero__menu">
            <div class="hero__menu-content">
                <div class="hero__links">
                    <RouterLink to="/">Магазин</RouterLink>
                    <RouterLink to="/">Новое</RouterLink>
                    <RouterLink to="/">Категории</RouterLink>
                    <RouterLink to="/">Новости</RouterLink>
                </div>
                <div class="hero__search">
                    <input type="text" placeholder="Поиск" v-model="query">
                    <button><svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M784-120 532-372q-30 24-69 38t-83 14q-109 0-184.5-75.5T120-580q0-109 75.5-184.5T380-840q109 0 184.5 75.5T640-580q0 44-14 83t-38 69l252 252-56 56ZM380-400q75 0 127.5-52.5T560-580q0-75-52.5-127.5T380-760q-75 0-127.5 52.5T200-580q0 75 52.5 127.5T380-400Z"/></svg></button>
                </div>
                <Suspense>
                    <SearchResults :query/>
                </Suspense>
            </div>
        </div>
        <div class="hero">
            <RouterLink :to="'/game/' + game.id">
                <img :src="game.image" alt="">
            </RouterLink>
        </div>
    </div>
</template>

<style scoped lang="scss">
.hero__wrapper {
    width: 100%;
    margin-top: 30px;
}

.hero {
    display: flex;
    justify-content: center;
    img {
        width: 900px;
    }
}

.hero__links {
    display: flex;
    gap: 15px;

    * {
        text-decoration: none;
    }
    
}

.hero__menu {
   width: 100%;
   display: flex;
   justify-content: center;
   
}

.hero__menu-content {
    background: linear-gradient(90deg, var(--background-active-start-color) 0%, var(--background-active-end-color) 100%);
    position: absolute;
    
    opacity: .9;
    top: 130px;
    width: 600px;
    margin: 0 auto;
    display: flex;
    padding: 0 10px;
    justify-content: space-between;
    align-items: center;
    z-index: 10;
}

.hero__search {
    display: flex;
    align-items: center;
    justify-content: center;
    button {
        background-color: transparent;
        border: none;
    }

    input {
        border: none;
        padding: 5px 10px;
        border-radius: 5px;
        background-color: var(--background-field-color);
        outline: none;
    }

    input::placeholder {
        color: var(--text-color);
    }
}
</style>

