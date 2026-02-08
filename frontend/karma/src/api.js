import axios from 'axios'

const API_BASE = process.env.VUE_APP_API_BASE || 'http://localhost:8000'

export const api = axios.create({
    baseURL: API_BASE,
})

// Ensure the `api` axios instance attaches the auth token on every request.
api.interceptors.request.use((config) => {
    const token = localStorage.getItem('Authentication-Token')
    if (token) {
        config.headers = config.headers || {}
        if (!config.headers['Content-Type']) {
            config.headers['Content-Type'] = 'application/json'
        }
        config.headers.Authorization = `Token ${token}`
    }
    return config
})

export async function uploadImage(file) {
    const form = new FormData()
    form.append('file', file)
    const res = await api.post('/upload-image/', form, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    })
    return res.data
}

export async function createNote(note) {
    return api.post('/notes/', note)
}

export async function listNotes(topicID) {
    if (!topicID) {
        return api.get('/notes/')
    }
    return api.get(`/notes/topic/${topicID}`)
}

export async function listTopics() {
    return api.get('/notes/topics/')
}

export async function listTopicNotes(topicId) {
    return api.get(`/notes/topic/${topicId}`)
}