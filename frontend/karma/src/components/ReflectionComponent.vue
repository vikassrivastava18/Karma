<template>
    <div class="reflection-component card shadow-sm">
        <h2>Daily Reflection</h2>
        <form @submit.prevent="submitReflection">
            <div class="form-group">
                <textarea id="reflection" v-model="reflection" class="form-control" required></textarea>
            </div>
            <button type="submit">Submit</button>
        </form>
    </div>
</template>

<script>
/* eslint-disable */
import { baseUrl } from '../config';
export default {
    name: 'RelectionComponent',
    data() {
        return {
            reflection: ''
        };
    },
    methods: {
        async submitReflection() {
            // Make API call to submit the reflection
            try {
                const url = baseUrl + '/daily/reflections'
                const reflection = { reflection: this.reflection }
                await this.$axios.post(url, reflection)
                
                this.$emit('showToast')
                this.reflection = '';
            } catch (error) {
                this.$emit('errorToast')
                this.$emit('errorToast')
            }
        }
    }
};
</script>

<style scoped>
    .reflection-component {
        padding: 30px;
        max-width: 75vw;
        margin: auto;
        margin-top: 100px;
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