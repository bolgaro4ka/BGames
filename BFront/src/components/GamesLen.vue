<script setup lang="ts">
import { GET_LEN_GAMES } from '@/config';
import axios from 'axios';


const res = await axios.get(GET_LEN_GAMES).then(res => res.data)

</script>

<template>
    <div class="lg__wrapper">
        <div class="lg">
            <p>В нашем каталоге {{ res.len }} игр</p>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.lg {
    text-align: center;
    background-color: var(--second-body-background);
    padding-bottom: 5px;
}
</style>