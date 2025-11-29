
import { createWebHistory, createRouter } from 'vue-router'
import store from './store'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'
import axios from 'axios'

import { createApp } from 'vue'
import App from './App.vue'
import HomePage from './views/HomPage.vue'
import LoginPage from './views/LoginPage.vue'

const routes = [
  { path: '/', component: HomePage, meta: { requiresAuth: true } },
  { path: '/login', component: LoginPage},
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth) {
    const token = localStorage.getItem('Authentication-Token');
    if (token) {
      next(); // User is authenticated, allow access
    } else {
      next('/login'); // Redirect to login page if not authenticated
    }
  } else {
    next(); // No authentication required, allow access
  }
});

let app = createApp(App)
  .use(router)
  .use(store)

app.config.globalProperties.$axios = axios

app.mount('#app')

// Request interceptor
axios.interceptors.request.use((config) => {
  const token = localStorage.getItem('Authentication-Token')
  if (token) {
    config.headers['Content-Type'] = 'application/json';
    config.headers.Authorization = `Token ${token}`
  }
  return config
})

axios.interceptors.response.use(
  response => response,
  error => {
    // Add more error handling here
    if (error.response && error.response.status === 403) {
      window.location.href = '/login'; // Redirect to login
    }
    return Promise.reject(error);
  }
);


