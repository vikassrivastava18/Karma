
import { createWebHistory, createRouter } from 'vue-router'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'
import axios from 'axios'
import store from './store'

import { createApp } from 'vue'
import App from './App.vue'
import HomePage from './pages/HomPage.vue'
import LoginPage from './pages/LoginPage.vue'
import NotesEditorPage from './pages/NotesEditorPage.vue'
import NotesListPage from './pages/NotesListPage.vue'
import NoteViewerPage from './pages/NoteViewerPage.vue'

const routes = [
  { path: '/', component: HomePage, meta: { requiresAuth: true } },
  { path: '/login', component: LoginPage },
  { path: '/create-note', component: NotesEditorPage, meta: { requiresAuth: true } },
  { path: '/notes', component: NotesListPage, meta: { requiresAuth: true } },
  { path: '/notes/:noteId', component: NoteViewerPage, meta: { requiresAuth: true } }
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
    if (error.response && [400, 401].includes(error.response.status)) {
      console.log("Login failed.");
      
      window.location.href = '/login'; // Redirect to login
    }
    return Promise.reject(error);
  }
);


