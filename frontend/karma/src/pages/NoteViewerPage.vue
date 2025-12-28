<template>
    <div class="note-viewer p-4" v-if="note" >
        <h1>{{ note.title }}</h1>

        <div v-for="(b, i) in note.blocks" :key="i" class="p-2 m-2">
            <h2 v-if="b.type === 'heading'" class="p-1">{{ b.content }}</h2>
            <p v-else-if="b.type === 'paragraph'" class="p-1">{{ b.content }}</p>
            <img v-else-if="b.type === 'image'" :src="b.content" class="note-image p-1" />
        </div>
    </div>

    <div v-else-if="loading">Loading…</div>
    <div v-else class="error">Note not found</div>
</template>


<script setup>
/* eslint-disable */
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { api } from '../api'

const route = useRoute()
const noteId = Number(route.params.noteId) // parse to number
const note = ref(null)
const loading = ref(false)

onMounted(load)
async function load() {
  loading.value = true
  try {
    const token = localStorage.getItem('Authentication-Token')
    const res = await api.get(`/notes/${noteId}/`, {
      headers: { Authorization: `Token ${token}` }
    })
    note.value = res.data
  } catch (e) {
    note.value = null
  } finally {
    loading.value = false
  }
}
</script>


<style scoped>
.note-image {
    max-width: 450px;
    margin: 10px 0;
    display: block;
}

.error {
    color: red;
}
</style>