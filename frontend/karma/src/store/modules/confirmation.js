export default {
  namespaced: true,

  state: () => ({
    show: false,
    title: '',
    message: '',
    confirmText: 'Confirm',
    cancelText: 'Cancel',
    onConfirm: null
  }),

  mutations: {
    SHOW_CONFIRM(state, payload) {
      state.show = true
      state.title = payload.title
      state.message = payload.message
      state.confirmText = payload.confirmText || 'Confirm'
      state.cancelText = payload.cancelText || 'Cancel'
      state.onConfirm = payload.onConfirm
    },
    HIDE_CONFIRM(state) {
      state.show = false
      state.onConfirm = null
    }
  },

  actions: {
    openConfirm({ commit }, payload) {
      commit('SHOW_CONFIRM', payload)
    },
    closeConfirm({ commit }) {
      commit('HIDE_CONFIRM')
    },
    confirm({ state, commit }) {
      if (typeof state.onConfirm === 'function') {
        state.onConfirm()
      }
      commit('HIDE_CONFIRM')
    }
  },

  getters: {
    confirm: (state) => state
  }
}
