<template>
    <header class="mb-2 ps-4">
        <div class="">
            <div class="d-flex flex-wrap align-items-center 
                justify-content-center justify-content-lg-start">
                <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 
                    justify-content-center mb-md-0">
                    <li class="nav-item" >             
                        <router-link to="/" class="nav-link">
                            <h3 class="px-4 text_black">KARMA</h3>
                        </router-link>
                    </li>
                    <li class="nav-item mt-2" v-if="isAuthenticated">
                        <router-link to="/notes" class="nav-link text_black">
                            Notes
                        </router-link>
                    </li>
                    <li class="nav-item mt-2" v-if="isAuthenticated">
                        <router-link to="/" class="nav-link text_black">
                            Reports
                        </router-link>
                    </li>
                </ul>               

                <div class="text-end" v-if="isAuthenticated">
                    <button type="button" class="btn btn-danger me-4" @click="logout">Logout</button>
                </div>
                <div class="text-end" v-else>
                    <button type="button" class="btn me-4" @click="login">Login</button>
                </div>
            </div>
        </div>
    </header>
</template>

<script>
import { mapState } from 'vuex'
export default {
    name: 'HeaderComponent',
    computed: {
        ...mapState('auth', ['isAuthenticated'])
    },
    methods: {
        logout() {
            localStorage.removeItem('Authentication-Token')
            this.$store.dispatch('logout')
            this.$router.push('/login')
        },
        login() {
            this.$router.push('/login')
        }
    }
}
</script>

<style scoped>
    ul {
        float: right;
    }
    header {
        background-color: rgb(93, 186, 215);
        width: 100vw;
        margin-top: 0px;
    }
    .text_black {
        color: black;
    }
    .text_white {
        color: white;
        font-size: larger;
    }
</style>