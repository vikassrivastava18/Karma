<template>
    <div class="note-list">
        <h3 style="text-align: center;" class="me-4">Saved Notes
        <router-link
            class="ms-4"
            :to="`/create-note`">
            Create Note
        </router-link>
        </h3>
        <div v-if="loading">Loading…</div>
        <div v-if="error" class="error">{{ error }}</div>

        <div v-for="note in notes" :key="note.id" class="note-item">
            <div class="container">
                <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-4">
                    <!-- Repeat this column for each note -->
                    <div class="col">
                    <div class="card h-100">
                        <div class="card-body d-flex flex-column">
                        <h5 class="card-title">
                            <router-link
                                :key="note.id"
                                :to="`/notes/${note.id}`"
                                
                                >
                                <h3>{{ note.title }}</h3>
                            </router-link>
                        </h5>
                        <p class="text-muted mb-2">Last Update: {{ format(note.updated_at) }}</p> 
                        </div>
                    </div>
                    </div>
                    <!-- /repeat -->
                </div>
            </div>
           
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { listNotes } from '../../api'

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