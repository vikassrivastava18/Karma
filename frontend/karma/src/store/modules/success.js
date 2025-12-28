export default {
  namespaced: true,
  state: {
    successToast: {
      show: false,
      title: 'Success',
      message: '',
      timestamp: null
    }
  },
  mutations: {
    SHOW_SUCCESS(state, payload) {
      state.SucessToast.show = true
      state.SucessToast.title = payload.title || 'Sucess'
      state.SucessToast.message = payload.message
      state.SucessToast.timestamp = Date.now()
    },
    HIDE_SUCCESS(state) {
      state.SucessToast.show = false
      state.SucessToast.message = ''
    }
  },
  actions: {
    showSucess({ commit }, payload) {
      commit('SHOW_SUCCESS', payload)
    },
    hideSucess({ commit }) {
      commit('HIDE_SUCCESS')
    }
  },
  getters: {
    SucessToast: (state) => state.errorToast
  }
}


