<script setup lang="ts">
import { GAMES_LIST_URL } from '@/config';
import axios from 'axios';
import GameCard from './particles/GameCard.vue';



const response = await axios.get(GAMES_LIST_URL+'2/20/').then(res => {
    console.log(res.data); return res.data.slice(1, res.data.length);
});

console.log(response);



</script>

<template>
    <div class="plof__wrapper">
        <div class="plof__cards">
            <div class="plof__card" v-for="config in response">
                
                
                    <GameCard :game="config"/>
                 
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
</style>