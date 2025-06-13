import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/library',
      name: 'libraty',
      component: () => import('../views/ListGamesView.vue'),
    },
    {
      path: '/community',
      name: 'community',
      component: () => import('../views/ListGamesView.vue'),
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/ListGamesView.vue'),
    },
  ],
})

export default router
