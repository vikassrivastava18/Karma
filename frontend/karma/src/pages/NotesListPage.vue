<template>
    <div class="note-list">
        <h1 style="text-align: center;">Saved Notes</h1>


        <div v-if="loading">Loading…</div>
        <div v-if="error" class="error">{{ error }}</div>


        <div v-for="note in notes" :key="note.id" class="note-item">
            <router-link
                :key="note.id"
                :to="`/notes/${note.id}`"
                class="note-item"
                >
                <h3>{{ note.title }}</h3>
            </router-link>
            <small>{{ format(note.updated_at) }}</small>
        </div>
    </div>
</template>


<script setup>
import { ref, onMounted } from 'vue'
import { listNotes } from '../api'


const notes = ref([])
const loading = ref(false)
const error = ref('')


onMounted(load)
async function load() {
    loading.value = true
    try {
        const res = await listNotes()
        notes.value = res.data
    } catch (e) {
        error.value = 'Failed to load notes'
    }
    loading.value = false
}


function format(date) {
    return new Date(date).toLocaleString()
}
</script>


<style scoped>
    .note-item {
        padding: 12px;
        border: 1px solid #ddd;
        margin: 6px 0;
        border-radius: 8px;
        cursor: pointer;
        transition: background 0.2s;
    }

    .note-item:hover {
        background: #eef5ff;
    }

    .error {
        color: red;
    }
</style>