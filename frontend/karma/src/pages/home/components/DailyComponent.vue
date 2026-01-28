
<template>
    <h3 style="text-align: center; color: crimson;">DAILY</h3>
    <div class="wrapper">        
        <div v-for="status in statuses" :key="status.id" :id="status.id" 
        class="container fixed-size">
            <h4>
                {{ status.title }} 
                <!-- Button trigger modal -->
                <button type="button" class="btn px-4" data-bs-toggle="modal" 
                data-bs-target="#exampleModal">
                </button>
            </h4>
            <div class="cards-wrapper" :key="status.id" 
                @drop="onDrop($event, status.id)" 
                @dragenter.prevent @dragover.prevent>

                <card v-for="karma of filteredTasks[status.id]" 
                    :key="karma.id" :id="karma.id" class="card" draggable="true"
                    @dragstart="startDrag($event, karma.id)">
                    <span class="">
                        <IconComponent :type="karma.type" />
                        {{ karma.title }}                        
                    </span>                    
                    <span class="content" v-html="karma.karma">
                    </span>
                </card>
            </div>
        </div>
    </div>
</template>

<script setup>

import { reactive, ref, onMounted, getCurrentInstance } from 'vue';
import IconComponent from './IconComponent.vue';
import { baseUrl } from '../../../config';

const instance = getCurrentInstance()
const proxy = instance && instance.proxy

const TODO_URL = '/daily/todos';
const AllKarmas = ref([]);
const statuses = reactive([{id: 'pe', 'title': 'DAILY'},
                {id: 'sa', 'title': 'SATISFIED'},
                {id: 'us', 'title': 'UNSATISFIED'}]);

const filteredTasks = reactive({
                pe: [],
                sa: [],
                us: []
            });


onMounted(() => getKarmas());
    
    
async function getKarmas() {
    // Modiify for API
    const url = baseUrl + TODO_URL

    try {
        const res = await proxy.$axios.get(url)
        AllKarmas.value = res.data
        
        filterItems()
    } catch (error) {
        console.error('Error:', error.message)
        // handle error (e.g., show an error message)
    }
}

async function editKarma(id, list) {            
    // Modify for API
    const karma = AllKarmas.value.find(karma => karma.id == id)
    const url = baseUrl + TODO_URL + '/' + id
    const updatedData = {...karma, "review": list};
    
    try {
        await proxy.$axios.put(url, updatedData)
        proxy.$store.dispatch('success/showSucsess', {
            title: 'Update Successful',
            message: 'Item updated successfully.'
        });
    } catch (error) {
        console.error('Error:', error.message)
        proxy.$store.dispatch('error/showError', {
            title: 'Update Failed',
            message: 'Item update failed.'
        });
    }

}

function filterItems() {
    filteredTasks.pe = AllKarmas.value.filter(karma => karma.review === 'pe')
    filteredTasks.sa = AllKarmas.value.filter(karma => karma.review === 'sa')
    filteredTasks.us = AllKarmas.value.filter(karma => karma.review === 'us')

    AllKarmas.value.forEach(karma => {
        karma.src = karma.type
    })
}

function startDrag(event, id) {
    event.dataTransfer.dropEffect = 'move'
    event.dataTransfer.effectAllowed = 'move'
    event.dataTransfer.setData('itemID', id)
    console.log("card_id", id)
}

function onDrop(event, list) {
    const itemID = event.dataTransfer.getData('itemID')
    const item = AllKarmas.value.find((karma) => karma.id == itemID)
    item.review = list
    filterItems()
    editKarma(itemID, list)            
}     
    

</script>

<style scoped>
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
        margin-bottom: 10px;
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

    .wrapper {
        max-width: 80vw;
        display: flex;
        margin: auto;
        justify-content: center;
        align-items: center;
        padding-top: 20px;
    }

    .fixed-size {
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

    #pe {
            background-color: lightyellow;
        }

    #sa {
        background-color: lightgreen;
    }

    #us {
        background-color: #e99292;
    }
</style>