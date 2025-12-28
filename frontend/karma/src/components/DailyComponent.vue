
<template>
    <h2 style="text-align: center;">DAILY</h2>
    <div class="wrapper">        
        <div v-for="status in statuses" :key="status.id" :id="status.id" class="container fixed-size">
            <h2>
                {{ status.title }} 
                <!-- Button trigger modal -->
                <button type="button" class="btn px-4" data-bs-toggle="modal" data-bs-target="#exampleModal">
                </button>
            </h2>
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

<script>

import IconComponent from './IconComponent.vue';
import { baseUrl } from '../config';

export default {
    name: 'DailyComponent',
    components: {
        IconComponent
    },
    data() {
        return {
            AllKarmas: [],
            statuses: [
                {id: 'ka', 'title': 'DAILY'},
                {id: 'sa', 'title': 'SATISFIED'},
                {id: 'us', 'title': 'UNSATISFIED'}
            ],
            filteredTasks: {
                ka: [],
                sa: [],
                us: []
            }            
        };
    },

    mounted() {
        this.getKarmas()
    },
    
    methods: {
        async getKarmas() {
            // Modiify for API
            const url = baseUrl + '/daily/todos'

            try {
                const res = await this.$axios.get(url)
                this.AllKarmas = res.data
                console.log("All Karmas: ", this.AllKarmas);
                
                this.filterItems()
            } catch (error) {
                console.error('Error:', error.message)
                // handle error (e.g., show an error message)
            }
        },

        async editKarma(id, list) {            
            // Modify for API
            const karma = this.AllKarmas.find(karma => karma.id == id)
            const url = baseUrl + '/daily/todos/' + id
            const updatedData = {...karma, "review": list};
            console.log("updated data: ", updatedData);
            
            try {
                await this.$axios.put(url, updatedData)
                this.$emit('showToast')
            } catch (error) {
                console.error('Error:', error.message)
                this.$emit('errorToast')
                // handle error (e.g., show an error message)
            }

        },

        filterItems() {
            this.filteredTasks.ka = this.AllKarmas.filter(karma => karma.review === 'pe')
            this.filteredTasks.sa = this.AllKarmas.filter(karma => karma.review === 'sa')
            this.filteredTasks.us = this.AllKarmas.filter(karma => karma.review === 'us')

            this.AllKarmas.forEach(karma => {
                karma.src = karma.type
            })
        },

        startDrag(event, id) {
            event.dataTransfer.dropEffect = 'move'
            event.dataTransfer.effectAllowed = 'move'
            event.dataTransfer.setData('itemID', id)
            console.log("card_id", id)
        },

        onDrop(event, list) {
            const itemID = event.dataTransfer.getData('itemID')
            const item = this.AllKarmas.find((karma) => karma.id == itemID)
            item.review = list
            this.filterItems()
            this.editKarma(itemID, list)            
        },        
    }
};
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

#ka {
        background-color: lightyellow;
    }

#sa {
    background-color: lightgreen;
}

#us {
    background-color: #e99292;
}
</style>