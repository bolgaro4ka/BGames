<script setup lang="ts"></script>

<template>
    <div class="blogo__wrapper">
        <div class="blogo__canvas">
            <div class="square square-gray"></div>
            <div class="square square-gray"></div>
            <div class="square square-gray"></div>
            <div class="square square-green"></div>
        </div>
    </div>
</template>

<style scoped lang="scss">
    .blogo__canvas {
        display: flex;
        flex-wrap: wrap;
        width: 43px;
        height: 43px;
        justify-content: center;
        align-items: center;
        gap: 3px;
        margin: 10px 0;

        .square {
            width: 20px;
            height: 20px;
            background-color: var(--text-color);
        }

        .square-green {
            background-color: green;
        }
    }


</style>