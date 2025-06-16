<script lang="ts" setup>
import { GET_GAME_BY_ID_URL } from '@/config';
import axios from 'axios';
import { useRoute } from 'vue-router';

import { Swiper, SwiperSlide } from 'swiper/vue';
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';

import SwiperCore from 'swiper';
import { Navigation, Pagination } from 'swiper/modules';
import GameRate from '@/components/particles/GameRate.vue';

SwiperCore.use([Navigation, Pagination]);


const route = useRoute();

const res = await axios.get(GET_GAME_BY_ID_URL + route.params.id + '/').then(res => {
    return res.data
})


</script>

<template>
    <div class="game__wrapper">
        <div class="game">
            <h2>🎮 {{ res.name }}</h2>
            <div class="game__slider">
                <Swiper
                    :slides-per-view="1"
                    :space-between="20"
                    :navigation="true"
                    :loop="true"
                    :pagination="{ clickable: true }"
                    class="category-swiper"
                >
                    <SwiperSlide>
                        <div class="swiper__img">
                            <img :src="res.pic1_url" alt="">
                        </div>
                        
                    </SwiperSlide>
                    <SwiperSlide>
                        <div class="swiper__img">
                            <img :src="res.pic2_url" alt="">
                        </div>
                    </SwiperSlide>
                    <SwiperSlide>
                        <div class="swiper__img">
                            <img :src="res.pic3_url" alt="">
                        </div>
                    </SwiperSlide>
                </Swiper>
            </div>

            

            <div class="game__description">
                <div class="game__download">
                    <h3>{{ res.name }}</h3>
                    <a :href="res.download_url1" download class="game__download-link">
                        <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M480-320 280-520l56-58 104 104v-326h80v326l104-104 56 58-200 200ZM240-160q-33 0-56.5-23.5T160-240v-120h80v120h480v-120h80v120q0 33-23.5 56.5T720-160H240Z"/></svg>
                        Скачать
                    </a>
                </div>
                
                <p>{{ res.long_description }}</p>

                <Suspense>
                    <GameRate :likes="res.likes" :dislikes="res.dislikes" :id="res.id" />
                </Suspense>
                <div class="game__requirements">
                    <div class="game__requirements-block">
                        <p>Системные требования</p>
                        <div class="game__requirements-list">
                            <p>Операционная система: <span class="game__requirements-param">{{ res.os }}</span></p>
                            <p>Процессор: <span class="game__requirements-param">{{ res.cpu }}</span></p>
                            <p>Оперативная память: <span class="game__requirements-param">{{ res.ram }}</span></p>
                            <p>Видеокарта: <span class="game__requirements-param">{{ res.gpu }}</span></p>
                            <p>Жесткий диск: <span class="game__requirements-param">{{ res.size }}</span></p>
                        </div>
                    </div>
                    <div class="game__requirements-block">
                        <p>Информация о игре</p>
                        <div class="game__requirements-list">
                            <p>Год выпуска: <span class="game__requirements-param">{{ res.year }}</span></p>
                            <p>Жанр: <span class="game__requirements-param">{{ res.genre }}</span></p>
                            <p>Разработчик: <span class="game__requirements-param">{{ res.developer }}</span></p>
                            <p>Версия: <span class="game__requirements-param">{{ res.version }}</span></p>
                            <p>Язык интерфейса: <span class="game__requirements-param">{{ res.language }}</span></p>
                            <p>Таблетка: <span class="game__requirements-param">{{ res.tablet }}</span></p>
                        </div>
                    </div>
                    
                </div>
            </div>

        </div>
    </div>
</template>

<style lang="scss" scoped>
.game {
    h2 {

        font-size: 40px;
        text-align: center;
    }
}

.game__download-link {
    display: flex;
    align-items: center;
    gap: 10px;
    text-decoration: none;
    background-color: var(--background-active-start-color);
    padding: 5px 30px;
}

.game__download-link:hover {
    background-color: var(--background-active-end-color);
}

.game__download {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: var(--header-color);
    padding: 10px;
    margin: 20px 0;
}

.game__requirements-block {
    display: flex;
    align-items: center;
    flex-direction: column;

}
.game__requirements-list {
    border: 1px solid #ccc;
    width: 900px;
    padding: 20px;
}
.game__description {
    width: 900px;
    margin: 0 auto;
}
.game__requirements-param {
    font-size: 20px;

}
.game__requirements {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 20px;

}
.category-swiper {
    user-select: none;
        padding-bottom: 40px; // Добавляем место под точки

        img {
            height: 500px;
        }

        .swiper__img {
            display: flex;
            justify-content: center;
            align-items: center;
        }

      .swiper-button-next,
      .swiper-button-prev {
        color: white;
        
        background: rgba(0, 0, 0, 0.3);
        border-radius: 50%;
        width: 40px;
        height: 40px;

        &:after {
          font-size: 20px;
        }
      }

      .swiper-pagination-bullets {
        margin-top: 1rem;
        .swiper-pagination-bullet {
          background: #ccc;
          opacity: 1;

          &-active {
            background: white;
          }
        }
      }

      .swiper-pagination-fraction, .swiper-pagination-custom, .swiper-horizontal > .swiper-pagination-bullets, .swiper-pagination-bullets.swiper-pagination-horizontal {
        margin-top: 20px;
      }

      .card {
        height: 250px;
        border-radius: 12px;
        background-size: cover;
        background-position: center;
        position: relative;
        overflow: hidden;
        display: flex;
        align-items: flex-end;

        .overlay {
          background: linear-gradient(0deg, rgba(0, 0, 0, 0.6), transparent);
          width: 100%;
          padding: 1rem;
          display: flex;
          justify-content: center;

          span {
            background: white;
            color: #162131;
            padding: 0.5rem 1rem;
            font-weight: bold;
            border-radius: 6px;
            text-align: center;
            font-size: 14px;
          }
        }
      }
    }
  

</style>