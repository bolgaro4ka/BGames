<script lang="ts" setup>
import { Swiper, SwiperSlide } from 'swiper/vue';
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';

import SwiperCore from 'swiper';
import { Navigation, Pagination } from 'swiper/modules';

SwiperCore.use([Navigation, Pagination]);

const categories = [
  { title: 'Хоррор', image: 'horror.webp', id: 13 },
  { title: 'Стратергия', image: 'strategy.webp', id: 8  },
  { title: 'Симулятор', image: 'simulation.webp' , id: 2 },
  { title: 'Экшен', image: 'action.webp', id: 5  },
  { title: 'Спортивные', image: 'sports.webp', id: 14  },
  { title: 'Логические', image: 'logic.webp', id: 12  },
  { title: 'Приключения', image: 'open-world.webp', id: 6  },
  { title: 'Гонки', image: 'racing.webp', id: 9  },
  { title: 'RPG', image: 'rpg.webp', id: 3  },
  { title: 'Шутеры', image: 'shooter.webp', id: 11  },
  { title: 'Без рубрики', image: 'no_rub.webp', id: 7  },
  { title: 'Аркады', image: 'arcade.webp', id: 1  },
  { title: 'Горячая новинка', image: 'new.webp', id: 4  },
  { title: 'Драки', image: 'fighting_martial_arts.webp', id: 10  },
  { title: 'Квесты', image: 'quest.webp', id: 15  },
  { title: 'VR', image: 'vr.webp', id: 16  },
];
</script>

<template>
  <div class="categories__wrapper">
    <div class="categories">
      <p class="title">КАТЕГОРИИ</p>
      <Swiper
        :slides-per-view="4"
        :space-between="20"
        :navigation="true"
        :loop="true"
        :pagination="{ clickable: true }"
        class="category-swiper"
      >
        <SwiperSlide v-for="(cat, index) in categories" :key="index">
          <RouterLink :to="'/cat/' + cat.id + '/'">
            <div class="card" :style="{ backgroundImage: `url(/categories/${cat.image})` }">
              <div class="overlay">
                <span>{{ cat.title }}</span>
              </div>
            </div>
          </RouterLink>
        </SwiperSlide>
      </Swiper>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.categories__wrapper {
  background: var(--second-body-background);
  padding: 2rem;
  color: white;

  .categories {
    width: 900px;
    margin: 0 auto;
    .title {
      font-weight: bold;
      margin-bottom: 1rem;
    }

    .category-swiper {
        padding-bottom: 40px; // Добавляем место под точки
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
  }
}
</style>
