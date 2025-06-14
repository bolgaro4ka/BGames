<script setup lang="ts">

const props = defineProps(['game']);

console.log(props.game);

</script>

<template>
    <div class="game-card__wrapper">
        <div class="game-card">
            <RouterLink :to="'/game/' + props.game.id">
                <img :src="props.game.image_url">
                <h2 class="game-card__title">🎮 {{props.game.name}}</h2>
                <p class="game-card__description">{{props.game.short_description}}</p>
            </RouterLink>

            <div class="game-card__actions">
                <a :href="props.game.download_url1" class="game-card__download">
                    <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M480-320 280-520l56-58 104 104v-326h80v326l104-104 56 58-200 200ZM240-160q-33 0-56.5-23.5T160-240v-120h80v120h480v-120h80v120q0 33-23.5 56.5T720-160H240Z"/></svg>
                    <p>Скачать</p>
                </a>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
    
    
    .game-card {
        background-color: var(--background-card-color);
        height: 500px;
        width: 440px;
        justify-content: space-between;
        display: flex;
        flex-direction: column;
        * {
            text-decoration: none;
        }

        .game-card__title {
            padding: 10px;
        }

        .game-card__description {
            padding: 10px;
        }
        

        img {
            width: 100%;
        }

        .game-card__download {
            background-color: var(--background-active-start-color);
            padding: 10px;
            display: flex;
            justify-content: center;
            align-items: center;
            
            color: var(--text-color);
        }

    }
</style>