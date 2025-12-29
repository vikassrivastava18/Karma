<template>
    <HeaderComponent />

    <main>
        <RouterView />
    </main>

    <ToastComponent />
    
    <ErrorToastComponent />    
</template>

<script>
import HeaderComponent from './components/HeaderComponent.vue';
import ToastComponent from './components/SuccessToastComponent.vue';
import ErrorToastComponent from './components/ErrorToastComponent.vue';

export default {
    name: 'App',
    methods: {

    },
    components: {
        HeaderComponent,
        ToastComponent,
        ErrorToastComponent
    }
}

</script>

<style>
    * {
        font-family: Raleway, sans-serif;
    }

    h1 {
        margin-block: 0 10px;
    }

    html, main, body {
        margin: 0px;
        width: 100vw;
    }

    .icon {
        height: 20px;
    }

    .title {
        font-weight: 800;
        font-size: 22px;
    }

    .content {
        color: #808080;
        hyphens: auto;
        text-overflow: ellipsis;
        overflow: hidden;
        display: -webkit-box;
        -webkit-line-clamp: 4;
        -webkit-box-orient: vertical;
    }

    .user-prio-wrapper {
        padding-top: 8px;
        display: flex;
        justify-content: space-between;
    }

    .user {
        color: #3742fa;
        font-weight: 700;
    }

</style>
