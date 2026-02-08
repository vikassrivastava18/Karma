import { createWebHistory, createRouter } from 'vue-router'
import HomePage from './pages/home/HomPage.vue'


const routes = [
  { path: '/', component: HomePage, meta: { requiresAuth: true } },
  { path: '/login', component: () => import('./pages/auth/LoginPage.vue')},
  { path: '/daily', component: () => import('./pages/daily/DailyPage.vue')},
  // Lazy load the routes for notes
  {
    path: '/notes',
    children: [
      {
        path: 'create-note', component: () => import('./pages/notes/NotesEditorPage'),
        meta: { requiresAuth: true }
      },
      {
        path: '', component: () => import('./pages/notes/NotesListPage'),
        meta: { requiresAuth: true }
      },
      
      {
        path: ':noteId', component: () => import('./pages/notes/NoteViewerPage'),
        meta: { requiresAuth: true }
      }
    ]
  },

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

export default router