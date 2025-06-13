<script setup lang="ts">
import Logo from './Logo.vue';

</script>

<template>
    <div class="header__wrapper">
        <div>
            <RouterLink to="/" class="header_logo">
                <Logo/>
                <h1>BGames</h1>
            </RouterLink>
        </div>
        <div class="header__menu">
            <RouterLink to="/" :class="{'header__active': $route.path === '/'}">Магазин</RouterLink>
            <RouterLink to="/library" :class="{'header__active': $route.path === '/library'}">Библиотека</RouterLink>
            <RouterLink to="/community" :class="{'header__active': $route.path === '/community'}">Коммьюнити</RouterLink>
            <RouterLink to="/about" :class="{'header__active': $route.path === '/about'}">О нас</RouterLink>
        </div>
        <div>
             <RouterLink to="/">Войти</RouterLink>
        </div>
    </div>
</template>

<style lang="scss" scoped>
    .header__wrapper {
        background-color: var(--header-color);
        display: flex;
        justify-content: space-between;
        padding: 0 10px;
        align-items: center;
    }

    .header_logo {
        display: flex;
        align-items: center;
        gap: 10px;
        text-decoration: none;
    }

    .header__menu {
        display: flex;
        gap: 15px;
        * {
            text-decoration: none;
        }
        

        .header__active {
            color: var(--selected-text-color);
            
            text-decoration: underline;
        }
    }
</style>