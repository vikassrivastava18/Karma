<template>    
    <div class="loginC p-5">        
        <form @submit.prevent="submit" class="p-4">
            <h2 class="p-2 mt-0">Login</h2>
            <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Username</label>
                <input type="text" class="form-control" v-model="formData.username" id="exampleInputEmail1"
                    aria-describedby="emailHelp">
            </div>
            <div class="mb-3">
                <label for="exampleInputPassword1" class="form-label">Password</label>
                <input type="password" class="form-control" v-model="formData.password" id="exampleInputPassword1">
            </div>
            <div class="mb-3 form-check">
                <input type="checkbox" class="form-check-input" id="exampleCheck1">
                <label class="form-check-label" for="exampleCheck1">Remember Me</label>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>      
    </div>
</template>

<script setup>
import { reactive } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import { baseUrl } from '../../config';

const store = useStore();
const router = useRouter();

const formData = reactive({
    username: '',
    password: ''
});

const submit = async () => {
    const url = `${baseUrl}/auth/login`;
    const initObj = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    };

    try {
        const res = await fetch(url, initObj);
        if (!res.ok) {
            store.dispatch('error/showError', {
                title: 'Login Failed',
                message: 'Invalid username or password'
            });
            return;
        }

        const data = await res.json();
        localStorage.setItem('Authentication-Token', data.token);
        store.dispatch('auth/login');
        router.push({ path: '/' });
    } catch (error) {
        store.dispatch('error/showError', {
            title: 'Something went wrong',
            message: 'Please try again later.'
        });
    }
};
</script>


<style scoped>
    .loginC {
        height: 75vh;
        width: 40vw;
        margin: 0 auto;
    }

    form {
        width: 100%;
        border-radius: 10px;
        border: 2px solid;
        border-radius: 5px;
    }
    h2 {
        text-align: center;
    }
</style>
