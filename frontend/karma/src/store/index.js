// src/store/index.js
import { createStore } from 'vuex'

import auth from './modules/auth'
import error from './modules/error'
import success from './modules/success'
import confirm from './modules/confirmation'

export default createStore({
  modules: {
    auth,
    error,
    success,
    confirm
  }
})
