<template>
    <DailyComponent @showToast="showToastPopup" />
        
    <ReflectionComponent @showToast="showToastPopup" />    
</template>

<script setup> 
import { Toast } from 'bootstrap'
import { onMounted } from 'vue';
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'
import DailyComponent from './components/DailyComponent.vue'
import ReflectionComponent from './components/ReflectionComponent.vue';

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



</script>