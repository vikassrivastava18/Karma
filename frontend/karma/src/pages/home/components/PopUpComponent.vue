<template>
    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Confirm Deletion</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                        <h4>Are you sure, you want to delete?</h4>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" 
                                data-bs-dismiss="modal" id="closeModal">Close</button>
                            <button type="submit" class="btn btn-primary">Save changes</button>
                        </div>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
/* eslint-disable */
import { baseUrl } from '../../../config';

export default {
    data() {
        return {
            todo: '',
            todoType: 'st',
            timeline: new Date().toISOString().substr(0, 10)
        }
    },
    methods: {
        async saveTodo(e) {
            e.preventDefault();

            const url = baseUrl + '/todo/todos';
            const init_obj = {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Token ' + localStorage.getItem('Authentication-Token')
                },

                body: JSON.stringify({
                    todo: this.todo,
                    todo_type: this.todoType,
                    deadline: this.timeline
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
                this.todo = '';
                this.todoType = 'st';
                // this.timeline = '';
                this.$emit('showToast')
                
            } catch (error) {
                console.error('Error:', error);
                this.$emit('errorToast')
            } finally {
                const btn = document.getElementById('closeModal');
                btn.click();
                this.$emit('getTodos');

            }
        }
    }
}

</script>