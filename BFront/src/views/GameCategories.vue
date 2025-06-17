<script setup lang="ts">
import Games from '@/components/Games.vue';
import { GET_CAT_BY_ID } from '@/config';
import axios from 'axios';
import { useRoute } from 'vue-router';


const route = useRoute();

const cat = await axios.get(GET_CAT_BY_ID + route.params.cat + '/').then(res => res.data)

</script>

<template>
    <div class="cat-view__wrapper">
        <div class="cat-view">
            <h2>Игры в категории {{cat.name}} ({{cat.short_name}})</h2>
            <p>{{ cat.description }}</p>
            <Games :cat="route.params.cat"/>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.cat-view {
    margin: 0 auto;
    max-width: 900px;
    h2 {
        text-align: center;
        font-size: 40px;
    }
    p {
        margin: 20px 0;
    }
}
</style>