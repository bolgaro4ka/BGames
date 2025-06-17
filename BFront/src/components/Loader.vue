<script setup lang="ts"></script>

<template>
    <div class="blogo__wrapper">
        <div class="blogo__canvas">
            <div class="square square-1"></div>
            <div class="square square-2"></div>
            <div class="square square-3"></div>
            <div class="square square-4"></div>
        </div>
    </div>
</template>

<style scoped lang="scss">
    @keyframes base-anim-1 {
        0% {
            background-color: green;
        }

        25% {
            background-color: var(--text-color);
        }
        50% {
            background-color: var(--text-color); 

        }
        75% {
             background-color: var(--text-color);
        }
        100% {
            background-color: var(--background-active-start-color);
        }
    }

    @keyframes base-anim-2 {
        0% {
            background-color: var(--text-color);
        }

        25% {
            background-color: var(--background-active-start-color);
        }
        50% {
            background-color: var(--text-color); 

        }
        75% {
             background-color: var(--text-color);
        }
        100% {
            background-color: var(--text-color);
        }
    }

    @keyframes base-anim-3 {
        0% {
            background-color: var(--text-color);
        }

        25% {
            background-color: var(--text-color);
        }
        50% {
            background-color: var(--background-active-start-color); 

        }
        75% {
             background-color: var(--text-color);
        }
        100% {
            background-color: var(--text-color);
        }
    }

    @keyframes base-anim-4 {
        0% {
            background-color: var(--text-color);
        }

        25% {
            background-color: var(--text-color);
        }
        50% {
            background-color: var(--text-color); 

        }
        75% {
             background-color: var(--background-active-start-color);
        }
        100% {
            background-color: var(--text-color);
        }
    }

    .blogo__canvas {
        display: flex;
        flex-wrap: wrap;
        width: 123px;
        height: 123px;
        justify-content: center;
        align-items: center;
        gap: 3px;
        margin: 10px 0;

        .square {
            width: 60px;
            height: 60px;
            background-color: var(--text-color);
        }
    }

    .square-1 {
        animation: base-anim-1 2s;
        animation-iteration-count: infinite;
    }
    .square-2 {
        animation: base-anim-2 2s;
        animation-iteration-count: infinite;
    }
    .square-3 {
        animation: base-anim-3 2s;
        animation-iteration-count: infinite;
    }
    .square-4 {
        animation: base-anim-4 2s;
        animation-iteration-count: infinite;
    }


    
</style>