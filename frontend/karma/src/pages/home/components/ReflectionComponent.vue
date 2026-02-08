<template>
    <h2 style="text-align: center; color: crimson;">Daily Reflection</h2>
    <div class="reflection-component card shadow-sm mb-4">
        
        <form @submit.prevent="submitReflection">
            <div class="form-group">
                <textarea id="reflection" 
                v-model="reflection" class="form-control"
                required></textarea>
            </div>
            <button type="submit">Submit</button>
        </form>
    </div>
</template>

<script setup>
import {ref, getCurrentInstance} from 'vue';
import { baseUrl } from '../../../config';

const instance = getCurrentInstance()
const proxy = instance && instance.proxy

let reflection = ref('')


async function submitReflection() {
    // Make API call to submit the reflection
    try {
        const url = baseUrl + '/daily/reflections'
        // const re = { reflection: reflection }
        await proxy.$axios.post(url,  { "reflection": reflection.value})        
        proxy.$store.dispatch('success/showSuccess', {
            title: 'Reflection added for the day.',
            message: 'Reflection added successfully.'
            });
        reflection.value = '';
    } catch (error) {
        proxy.$store.dispatch('error/showError', {
            title: 'Reflection save Failed',
            message: 'Item save failed.'
        })
    }
}

</script>

<style scoped>
    .reflection-component {
        padding: 30px;
        max-width: 80vw;
        margin: auto;
        margin-top: 30px;
        border: 1px solid #ccc;
        border-radius: 4px;
        background-color: lightyellow;
    }

    .form-group {
        margin-bottom: 15px;
    }

    label {
        display: block;
        margin-bottom: 5px;
    }

    textarea {
        width: 100%;
        height: 100px;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 4px;
    }

    button {
        padding: 10px 20px;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }

    button:hover {
        background-color: #0056b3;
    }
</style>