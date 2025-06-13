import './assets/main.css'
import 'swiper/css';

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'
import { BASE_URL } from './config/index'

const app = createApp(App)

app.config.globalProperties.axios = axios

axios.defaults.baseURL = BASE_URL
axios.defaults.headers.post['Authorization'] = 'Bearer ' + localStorage.getItem('jwt')
axios.defaults.headers.get['Authorization'] = 'Bearer ' + localStorage.getItem('jwt')


app.use(createPinia())
app.use(router)

app.mount('#app')
