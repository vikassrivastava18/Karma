<template>
    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Create TODO</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form @submit="saveTodo">
                        <div class="mb-3">
                            {{ todo }}
                            <label for="todoText" class="form-label">Todo</label>
                            <input type="text" class="form-control" id="todoText" v-model="todo"
                                placeholder="Enter your todo">
                        </div>
                        <div class="mb-3">
                            <label for="todoType" class="form-label">Type</label>
                            <select class="form-select" id="todoType" v-model="todoType">
                                <option value="pr">Prayer</option>
                                <option value="wo">Work</option>
                                <option value="st">Study</option>
                                <option value="ho">Family</option>
                                <option value="pl">Play</option>
                            </select>
                        </div>
                        <div class="mb-3">
                            <label for="todoTimeline" class="form-label">Timeline for completion</label>
                            <input type="datetime-local" class="form-control" id="todoTimeline" v-model="timeline"
                                placeholder="Enter task deadline">
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal"
                                id="closeModal">Close</button>
                            <button type="submit" class="btn btn-primary">Save changes</button>
                        </div>
                    </form>
                </div>

            </div>
        </div>
    </div>
</template>

<script setup>
import { baseUrl } from '../../../config';
import {ref, getCurrentInstance} from 'vue';
import { useStore } from 'vuex';

const store = useStore()
const internal = getCurrentInstance();
const emit = internal?.emit || (() => {});
const todo = ref('');
const todoType = ref('st');
const timeline = ref(new Date().toISOString().substr(0, 10));

async function saveTodo(e) {
    e.preventDefault();

    const url = baseUrl + '/todo/todos';
    const init_obj = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + localStorage.getItem('Authentication-Token')
        },

        body: JSON.stringify({
            todo: todo.value,
            todo_type: todoType.value,
            deadline: timeline.value
        })
    };

    try {
        const response = await fetch(url, init_obj);
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.message || 'Error occurred');
        }
        await response.json();

        // Optionally, you can reset the form fields here
        todo.value = '';
        todoType.value = 'st';
        // this.timeline = '';
        store.dispatch('success/showSucsess', {
            title: 'Update Successful',
            message: 'Item updated successfully.'
        });
        

    } catch (error) {
        console.error('Error:', error);
        store.dispatch('error/showError', {
            title: 'Create todo failed',
            message: 'Todo vreation failed.'
        });
    } finally {
        const btn = document.getElementById('closeModal');
        btn.click();
        emit('getTodos');
    }
}


</script>