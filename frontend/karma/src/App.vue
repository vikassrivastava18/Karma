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
import ToastComponent from './components/ToastComponent.vue';
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

    main {
        margin: 0;
        padding: 0px;
        padding-bottom: 30px;
        /* min-height: 100vh; */
        background-color: #8EC5FC;
        background-image: linear-gradient(62deg, #8EC5FC 0%, #E0C3FC 100%);
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
