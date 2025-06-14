<script setup lang="ts">
import { GAME_SEARCH_URL } from '@/config';
import axios from 'axios';
import { reactive, ref, watch } from 'vue';
import GameSearchCard from './particles/GameSearchCard.vue';

const props = defineProps(['query']);

const results = ref({});

watch(props, async () => {
    const res = await axios.post(GAME_SEARCH_URL, {
        "query": props.query,
        "limit": 5
    }).then(res => res.data)

    results.value = res
})

</script>

<template>
    <div class="search-results__wrapper">
        <div class="search-results">
            <GameSearchCard v-for="game in results" :game="game" />
        </div>
    </div>

</template>

<style lang="scss" scoped>
.search-results__wrapper {
    position: absolute;
    top: 28px;
    right: 0;
}
</style>