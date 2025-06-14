<script lang="ts" setup>

const props = defineProps(['game']);

</script>

<template>
    <div class="game-search-card__wrapper">
        <div class="game-search-card">
            <RouterLink :to="'/game/' + props.game.id" class="game-search-card__link">
                <div class="game-search-card__overlay">
                    <img :src="props.game.image_url">
                    <div class="game-search-card__text">
                        <h2 class="game-search-card__title">🎮 {{props.game.name}}</h2>
                    </div>
                </div>
            </RouterLink>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.game-search-card__link {
    text-decoration: none !important;
    font-size: 12px;
}

.game-search-card {
    

.game-search-card__overlay{
    display: flex;
    background-color: var(--search-background-color);
    border-top: 1px solid var(--header-color);
    gap: 10px;
    padding-right: 10px;
    transition: all .3s;
}

.game-search-card__overlay:hover {
    background-color: var(--search-background-color-hover);

    h2 {
        color: var(--search-text-color-hover);
    }
    
}

    

    img {
        height: 50px;
    }
}
</style>