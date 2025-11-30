<template>
    
    <div class="loginC p-5">
        <h2>Login</h2>
        <form @submit.prevent="submit" class="p-4">
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

        <ToastComponent />
        
        <ErrorToastComponent />
    </div>
</template>

<script>
import { baseUrl } from '../config';
import ToastComponent from '../components/ToastComponent.vue';
import ErrorToastComponent from '../components/ErrorToastComponent.vue';

import { mapActions } from 'vuex';
import { Toast } from 'bootstrap'

export default {
    name: 'LoginComponent',
    data() {
        return {
            formData: {
                username: null,
                password: null
            }
        }
    },
    components: {
        ToastComponent,
        ErrorToastComponent
    },
    methods: {
        ...mapActions(['login']),
        
        async submit() {
            console.log("COnfig: ", baseUrl);
            
            const url = baseUrl + '/auth/login'
            const init_obj = {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.formData)
            }

            try {

                const res = await fetch(url, init_obj)
                if (!res.ok) {
                    const errorData = await res.json()
                    this.$emit('errorToast')
                    throw new Error(errorData.message || 'Login Error occurred')
                }
                const data = await res.json()
                console.log('Success:', data)
                // Seth the token in local storage
                localStorage.setItem('Authentication-Token', data.token)
                // Set the state of isAuthenticated to true
                this.login()
                // Redirect to the home page
                this.$router.push({ path: '/' })
                // handle success (e.g., show a success message, redirect, etc.)
            } catch (error) {
                console.error('Error-', error.message)
                this.errorToast()
                // handle error (e.g., show an error message)
            }
        },

        showToastPopup() {
            const toastEl = document.getElementById('liveToast')
            const toast = new Toast(toastEl)
            toast.show()
        },

        errorToast() {
            const toastEl = document.getElementById('liveToastError')
            const toast = new Toast(toastEl)
            toast.show()
        },

    }
}
</script>


<style scoped>
.loginC {
    height: 100vh;
    width: 40vw;
    margin: 0 auto;
}

form {
    width: 66%;
    /* margin: auto;
    padding: 20px; */
    background: #dee8ff;
    border-radius: 10px;
}
</style>
