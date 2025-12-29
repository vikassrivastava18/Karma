<template>
    <div>
        <TodoComponent @showToast="showToastPopup" />

        <DailyComponent @showToast="showToastPopup" />
        
        <ReflectionComponent @showToast="showToastPopup" />        
    </div>
</template> 

<script>
/* eslint-disable */

import { Toast } from 'bootstrap'

import DailyComponent from './components/DailyComponent.vue'
import TodoComponent from './components/TodoComponent.vue';
import ReflectionComponent from './components/ReflectionComponent.vue';
import SuccessToastComponent from '../../components/SuccessToastComponent.vue';

export default {
    name: 'HomePage',
    computed: {
    },
    components: {
        DailyComponent,
        TodoComponent,
        ReflectionComponent,
        SuccessToastComponent,      
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
            var images = require.context('../../assets/', false, /\.png$/)
            return images('../../assets/' + pet + ".svg")
        },
    }
}

</script>

<style scoped>    
    .btn {
        float: right;
    }
</style>
