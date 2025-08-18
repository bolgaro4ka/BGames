<script setup lang="ts">
import { nextTick, ref } from 'vue';
import Logo from './Logo.vue';

const isDisclaimerOpen = ref(false);

function scrollToBottom() {
  const target = document.getElementById('bottom');
  if (target) {
    target.scrollIntoView({ behavior: 'smooth' });
  }
}

function handleOpen() {
    isDisclaimerOpen.value = !isDisclaimerOpen.value
    nextTick(() => scrollToBottom())
    
}
</script>
<template>
    <div class="footer__wrapper">
        <div class="footer">
            <RouterLink class="footer__logo" to="/">
                <Logo/>
                <h1>BGames</h1>
            </RouterLink>

            <div class="footer__content">
                <a href="https://github.com/bolgaro4ka/bgames" target="_blank">
                    GitHub
                </a>
                <RouterLink to="/">
                    На главную
                </RouterLink>
                <RouterLink to="/about">
                    О нас
                </RouterLink>
                <div class="footer__disclaimer" @click="handleOpen" >
                    <p>Правообладателям</p>
                </div>
            </div>
        </div>
        <div class="footer__disclaimer-content" v-if="isDisclaimerOpen">
            <p>Сайт не несёт ответственности за содержание материалов. Если вы являетесь правообладателям и хотите убрать свой материал с нашего сайта, то напишите администрации — <a href="mailto:bolgaro4ka.github@gmail.com">bolgaro4ka.github@gmail.com</a>. Напомним, что ваша собственность находилась в публичном доступе и только поэтому была опубликована на нашем сайте. Сайт некоммерческий, и мы не можем проверить все публикации пользователей.</p>
        </div>
        <div id="bottom"></div>
        
    </div>
</template>
<style lang="scss" scoped>
.footer__wrapper {
    background-color: var(--header-color);
    padding: 0 10px;
}
.footer__logo {
    display: flex;
    text-decoration: none;
    align-items: center;
    gap: 10px;
    
}

.footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.footer__disclaimer-content {
    text-align: center;
    padding: 20px 0;
}

.footer__content {
    display: flex;
    gap: 20px;

    a {
        text-decoration: none;
    }
}

@media screen and (max-width: 570px) {
    .footer {
        flex-direction: column;
        padding-bottom: 10px;
    }

    .footer__content {
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
    }


    
}
</style>