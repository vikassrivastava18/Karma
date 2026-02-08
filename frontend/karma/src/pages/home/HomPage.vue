<template>
    <div>
        <TodoComponent @showToast="showToastPopup" />

        <DailyComponent @showToast="showToastPopup" />
        
        <ReflectionComponent @showToast="showToastPopup" />        
    </div>
</template> 

<script setup>
/* eslint-disable */

import { Toast } from 'bootstrap'

import DailyComponent from './components/DailyComponent.vue'
import TodoComponent from './components/TodoComponent.vue';
import ReflectionComponent from './components/ReflectionComponent.vue';
import { onMounted } from 'vue';
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'

const store = useStore()
const router = useRouter()

onMounted(checkAuthentication)

function checkAuthentication () {
    // Redirect to login if the user is not authenticated
    if (!store.state.auth.isAuthenticated) {
        router.push({ path: '/login' })
    }
}

async function showToastPopup() {
        const toastEl = document.getElementById('liveToast')
        const toast = new Toast(toastEl)
        toast.show()
    }

async function getImgUrl(pet) {
        var images = require.context('../../assets/', false, /\.png$/)
        return images('../../assets/' + pet + ".svg")
    }

</script>

<style scoped>    
    .btn {
        float: right;
    }
</style>
