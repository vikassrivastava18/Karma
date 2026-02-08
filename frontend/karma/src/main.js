import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'
import axios from 'axios'
import store from './store'
import { createApp } from 'vue'
import router from './router'
import App from './App.vue'


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

// Redirect to login page in case of authentication error
axios.interceptors.response.use(
  response => response,
  error => {
    // Add more error handling here
    if (error.response && [401, 403].includes(error.response.status)) {
      console.log("Login failed.");

      router.push('/login'); // Redirect to login using router
    }
    return Promise.reject(error);
  }
);


