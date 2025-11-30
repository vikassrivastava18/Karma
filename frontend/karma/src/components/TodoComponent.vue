<template>

    <div>
        <div class="wrapper2">
            <div v-for="status in statuses" :key="status.id" :id="status.id" class="container fixed-size">
                <h2>
                    {{ status.title }}
                    <!-- Button trigger modal -->
                    <button v-if="status.id == 'to'" type="button" class="btn px-2" data-bs-toggle="modal"
                        data-bs-target="#exampleModal">
                        <img src="../assets/create.png" width="20" alt="create list">
                    </button>
                </h2>
                <div class="cards-wrapper" :key="status.id" @drop="onDrop($event, status.id)" @dragover.prevent>

                    <card v-for="karma of filteredTasks[status.id]" 
                        :key="karma.id" :id="karma.id" 
                        class="card p-3"
                        :class="{ overdue: overdueTaskIds.includes(karma.id) }"
                        draggable="true" 
                        @dragstart="startDrag($event, karma.id)"
                        @dblclick="openDetails(karma.id)">

                        <span class="content">
                            <IconComponent :type="karma.todo_type" /> &nbsp;
                            <b>{{ karma.todo.split(' ')[0] }}</b> {{ karma.todo.split(' ').slice(1).join(' ') }}                            
                            <IconComponent :type="ar" style="float: right;" @click="archiveKarma(karma.id)" />
                        </span>
                    </card>
                </div>

            </div>
        </div>

        <ModalComponent @getTodos="getTodos" />

        <div v-if="showDetails" class="todo-details-modal">
            <div class="modal-content">
                <h3>Todo Details</h3>
                <p><strong>Title:</strong> {{ selectedTodo.todo }}</p>
                <p><strong>Type:</strong> {{ selectedTodo.todo_type }}</p>
                <p><strong>Status:</strong> {{ selectedTodo.status }}</p>
                <button @click="closeDetails" class="btn btn-secondary">Close</button>
            </div>
        </div>
    </div>


</template>

<script>
/* eslint-disable */
import { baseUrl } from '../config'
import IconComponent from './IconComponent.vue';
import ModalComponent from './ModalComponent.vue';


export default {
    name: 'TodoComponent',
    components: {
        IconComponent,
        ModalComponent
    },
    data() {
        return {
            AllTasks: [],

            statuses: [
                { id: 'to', title: 'TODO' },
                { id: 'pr', title: 'IN-PROGRESS' },
                { id: 'co', title: 'COMPLETED' }
            ],
            filteredTasks: {
                to: [],
                pr: [],
                co: []
            },
            ar: "ar",
            showDetails: false,
            selectedTodo: null
        };
    },

    computed: {
        overdueTaskIds() {
            const now = new Date();
            return this.AllTasks
                .filter(karma => karma.deadline && karma.status !== 'co' && new Date(karma.deadline) < now)
                .map(karma => karma.id);
        }
    },

    mounted() {
        // Get the items from backend
        this.getTodos();
        document.addEventListener('visibilitychange', this.handleVisibilityChange);
    },
    methods: {
        truncate(text, length) {
            if (!text) return '';
            return text.length > length ? text.substring(0, length) + '...' : text;
        },
        async getTodos() {
            const url = baseUrl + '/todo/todos';

            try {
                const res = await this.$axios.get(url);
                const data = res.data;
                this.AllTasks = data;
                this.filterItems();
            } catch (error) {
                console.error('Error:', error.message);
                // handle error (e.g., show an error message)
            }
        },

        filterItems() {
            this.filteredTasks.to = this.AllTasks.filter(karma => karma.status === 'to');
            this.filteredTasks.pr = this.AllTasks.filter(karma => karma.status === 'pr');
            this.filteredTasks.co = this.AllTasks.filter(karma => karma.status === 'co');
        },

        openDetails(todo) {
            this.selectedTodo = todo;
            this.showDetails = true;
        },

        closeDetails() {
            this.selectedTodo = null;
            this.showDetails = false;
        },

        async editKarma(id, list) {
            const karma = this.AllTasks.find(karma => karma.id == id);
            const url = baseUrl + '/todo/todos/' + id;
            const updatedData = { ...karma, "review": list };

            try {
                await this.$axios.put(url, updatedData);
                this.$emit('showToast');
            } catch (error) {
                console.error('Error:', error.message);
                this.$emit('errorToast');
            }
        },

        openDetails(id) {
            const selectedTodo = this.AllTasks.find(karma => karma.id === id);
            if (selectedTodo) {
                this.showDetails = true;
                this.selectedTodo = selectedTodo; // Store the selected todo item
            }
        },

        closeDetails() {
            this.showDetails = false;
            this.selectedTodo = null; // Clear the selected todo item
        },

        async archiveKarma(id) {
            const karma = this.AllTasks.find(karma => karma.id === id);
            const url = `${baseUrl}/todo/todos/${id}`;
            const updatedData = { ...karma, status: 'ar' }; // Update status to 'ar'

            try {
                const res = await this.$axios.put(url, updatedData);
                if (res.status === 200) {
                    // Remove the item from the list
                    this.AllTasks = this.AllTasks.filter(karma => karma.id !== id);
                    this.filterItems(); // Update filtered tasks
                    this.$emit('showToast', 'Item archived successfully!');
                }
            } catch (error) {
                console.error('Error archiving item:', error.message);
                this.$emit('errorToast', 'Failed to archive item.');
            }
        },

        startDrag(event, id) {
            event.dataTransfer.dropEffect = 'move';
            event.dataTransfer.effectAllowed = 'move';
            event.dataTransfer.setData('itemID', id);
        },

        onDrop(event, list) {
            const itemID = event.dataTransfer.getData('itemID');
            const item = this.AllTasks.find(karma => karma.id == itemID);
            item.status = list;
            this.filterItems();
            this.editKarma(itemID, list);
        },

        handleVisibilityChange() {
            if (document.visibilityState === 'visible') {
                console.log("Tab changed to Karma Page");
                
                // Force Vue to re-evaluate computed properties
                // This will trigger reactivity for overdueTaskIds
                this.AllTasks = [...this.AllTasks];
            }
        },
    },

    beforeDestroy() {
        document.removeEventListener('visibilitychange', this.handleVisibilityChange);
    }
};
</script>

<style scoped>
.wrapper2 {
    padding: 30px;
    padding-top: 45px;
    /* max-height: 60vh; */
    max-width: 80vw;
    display: flex;
    margin: auto;
    justify-content: center;
    align-items: center;
    padding-top: 50px;
}

.container {
    background: #dee8ff;
    border-radius: 10px;
    padding: 20px;
    margin: 10px;
    display: flex;
    flex-direction: column;
    max-height: 70vh;
}

.cards-wrapper {
    scrollbar-width: thin;
    padding-inline: 10px;
    padding-top: 10px;
    /* max-height: calc(100vh - 100px); */
    min-width: 328px;
    border-radius: 10px;
    overflow-y: scroll;
    min-height: 100px;
    flex-grow: 1;
    transition: 0.3s;
}

.card-placeable {
    background: #0000000d;
}

.card {
    padding: 10px;
    /* width: 300px; */
    margin-bottom: 20px;
    background: white;
    border-radius: 10px;
    overflow-y: hidden;
    filter: drop-shadow(0 2px 7px #00000040);
    display: flex;
    flex-direction: column;
    cursor: pointer;
}

.type {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    padding-block: 5px;
    gap: 5px;
    margin: -10px;
    margin-bottom: 10px;
}


.fixed-size {
    /* margin-top: 80vh; */
    padding: 20px;
    width: 800px;
    /* Set your desired width */
    height: 500px;
    /* Set your desired height */
    overflow: auto;
    /* Add overflow if content exceeds the fixed size */
}

.daily-component {
    text-align: center;
    margin: 20px;
}


.details-modal {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.3);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
}

.details-content {
    background: #fff;
    padding: 30px;
    border-radius: 10px;
    min-width: 300px;
    box-shadow: 0 2px 10px #0003;
}

#to {
    background-color: lightyellow;
}

#pr {
    background-color: lightblue;
}

#co {
    background-color: lightgreen;
}


.todo-details-modal {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: #ffffff;
    /* White background for modal */
    padding: 30px;
    /* Increased padding for better spacing */
    border-radius: 15px;
    /* Rounded corners */
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    /* Enhanced shadow for modal */
    z-index: 1000;
    max-width: 500px;
    /* Limit modal width */
    width: 90%;
    /* Responsive width */
    animation: fadeIn 0.3s ease-in-out;
    /* Smooth fade-in animation */
}

.modal-content {
    text-align: left;
    font-family: 'Arial', sans-serif;
    /* Modern font */
    line-height: 1.6;
    /* Improved readability */
    padding: 10px;
}

.modal-content h3 {
    margin-bottom: 20px;
    font-size: 1.5rem;
    /* Larger heading */
    color: #333;
    /* Darker text color */
    border-bottom: 2px solid #007bff;
    /* Add a subtle underline */
    padding-bottom: 10px;
}

.modal-content p {
    margin-bottom: 10px;
    font-size: 1rem;
    /* Standard text size */
    color: #555;
    /* Softer text color */
}

.modal-content button {
    margin-top: 20px;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    background-color: #007bff;
    /* Bootstrap primary color */
    color: #ffffff;
    cursor: pointer;
    transition: background-color 0.3s;
    font-size: 1rem;
    /* Slightly larger button text */
}

.modal-content button:hover {
    background-color: #0056b3;
    /* Darker blue on hover */
}

.content {
    font-size: larger;
}

.overdue {
    background-color: #ffcccc !important;
}
</style>
