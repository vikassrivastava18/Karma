import axios from 'axios'

const API_BASE = process.env.VUE_APP_API_BASE || 'http://localhost:8000/api/notes'

export const api = axios.create({
    baseURL: API_BASE,
})


export async function uploadImage(file) {
    const form = new FormData()
    form.append('file', file)
    const token = localStorage.getItem('Authentication-Token')
    const res = await api.post('/upload-image/', form, {
        headers: {
            'Content-Type': 'multipart/form-data',
            Authorization: `Token ${token}`
        }
    })
    return res.data
}


export function createNote(note) {
    const token = localStorage.getItem('Authentication-Token')
    return api.post('/notes/', note, {
        headers: { Authorization: `Token ${token}`}
    })
}


export function listNotes() {
    const token = localStorage.getItem('Authentication-Token')
    return api.get('/notes/', {
        headers: { Authorization: `Token ${token}`}
    })
}

export function listTopics() {
    const token = localStorage.getItem('Authentication-Token')
    return api.get('/topics/', {
        headers: { Authorization: `Token ${token}` }
    })
}