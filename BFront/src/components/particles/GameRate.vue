<script setup lang="ts">
import { POST_DISLIKE, POST_LIKE } from '@/config';
import axios from 'axios';
import { ref } from 'vue';


const props = defineProps(["likes", 'dislikes', 'id'])

const isLikePressed = ref(false);
const isDisLikePressed = ref(false);

async function like() {
    const res = await axios.post(POST_LIKE, {
        id: props.id
    }).then(res => res.data)
    
    if (res) {
        isLikePressed.value = true;
        isDisLikePressed.value = false;
    }
}

async function dislike() {
    const res = await axios.post(POST_DISLIKE, {
        id: props.id
    }).then(res => res.data)
    
    if (res) {
        isLikePressed.value = false;
        isDisLikePressed.value = true;
    }
}
</script>

<template>
    <div class="gr__wrapper">
        <div class="gr">
            <div :class="'gr__rating' + ' ' + ((props.likes - props.dislikes > 0) && 'gr__green') + ' ' + ((props.likes - props.dislikes == 0) && 'gr__netral') + ' ' + ((props.likes - props.dislikes < 0) && 'gr__red')">
                <p v-if="!isLikePressed && !isDisLikePressed">Рейтинг: {{ props.likes - props.dislikes }}</p>
                <p v-else-if="isLikePressed && !isDisLikePressed">Рейтинг: {{ props.likes + 1 - props.dislikes }}</p>
                <p v-else>Рейтинг: {{ props.likes - props.dislikes - 1 }}</p>
            </div>
            <div class="gr__actions">
                <div class="gr__like" @click="like">
                    <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M720-120H280v-520l280-280 50 50q7 7 11.5 19t4.5 23v14l-44 174h258q32 0 56 24t24 56v80q0 7-2 15t-4 15L794-168q-9 20-30 34t-44 14Zm-360-80h360l120-280v-80H480l54-220-174 174v406Zm0-406v406-406Zm-80-34v80H160v360h120v80H80v-520h200Z"/></svg>
                    <p v-if="!isLikePressed">{{ props.likes }}</p>
                    <p v-else>{{ props.likes + 1 }}</p>
                </div>
                <div class="gr__dislike" @click="dislike">
                    <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M240-840h440v520L400-40l-50-50q-7-7-11.5-19t-4.5-23v-14l44-174H120q-32 0-56-24t-24-56v-80q0-7 2-15t4-15l120-282q9-20 30-34t44-14Zm360 80H240L120-480v80h360l-54 220 174-174v-406Zm0 406v-406 406Zm80 34v-80h120v-360H680v-80h200v520H680Z"/></svg>
                    <p v-if="!isDisLikePressed">{{ props.dislikes }}</p>
                    <p v-else>{{ props.dislikes + 1 }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.gr__actions {
    display: flex;
    align-items: center;
    justify-content: end;
    gap: 20px;
}

.gr {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: var(--header-color);
    padding: 10px;
    margin: 20px 0;
}

.gr__red p {
    background-color: red;
}

.gr__green p {
    background-color: var(--background-active-start-color);
}

.gr__rating p {
    padding: 5px;
}

.gr__like, .gr__dislike {
    display: flex;
    gap: 10px;
    transition: all .3s;
}

.gr__like:hover {
    svg, p {
        fill: var(--background-active-start-color);
        color: var(--background-active-start-color);
    }
}

.gr__dislike:hover {
    svg, p {
        fill: red;
        color: red;
    }
}
</style>