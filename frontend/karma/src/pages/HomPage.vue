<template>
    <div>
        <TodoComponent @showToast="showToastPopup" />

        <DailyComponent @showToast="showToastPopup" />
        
        <ReflectionComponent @showToast="showToastPopup" />        
    </div>
</template> 

<script>
/* eslint-disable */
// import CustomFetch from '@/CustomFetch';
import { mapState } from 'vuex'
import { Toast } from 'bootstrap'

import DailyComponent from '../components/DailyComponent.vue';
import TodoComponent from '../components/TodoComponent.vue';
import ReflectionComponent from '../components/ReflectionComponent.vue';
import ToastComponent from '../components/ToastComponent.vue';

export default {
    name: 'HomePage',
    computed: {
    },
    components: {
        DailyComponent,
        TodoComponent,
        ReflectionComponent,
        ToastComponent,      
    },
    data() {
        return {
        }
    },
    mounted() {
        // Check if the user is authenticated
        if (!this.$store.state.auth.isAuthenticated) {
            this.$router.push({ path: '/login' });
        }       
    },

    methods: {
        showToastPopup() {
            const toastEl = document.getElementById('liveToast')
            const toast = new Toast(toastEl)
            toast.show()
        },

        getImgUrl(pet) {
            var images = require.context('../assets/', false, /\.png$/)
            return images('../assets/' + pet + ".svg")
        },
    }
}

</script>

<style scoped>    
    .btn {
        float: right;
    }
</style>
