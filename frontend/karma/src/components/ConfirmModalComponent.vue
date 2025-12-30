<template>
  <div v-if="confirm.show">
    <div class="modal fade show d-block" tabindex="-1">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">

          <div class="modal-header">
            <h5 class="modal-title">{{ confirm.title }}</h5>
            <button type="button" class="btn-close" @click="close"></button>
          </div>

          <div class="modal-body">
            <p>{{ confirm.message }}</p>
          </div>

          <div class="modal-footer">
            <button class="btn btn-secondary" @click="close">
              {{ confirm.cancelText }}
            </button>
            <button class="btn btn-danger" @click="confirmAction">
              {{ confirm.confirmText }}
            </button>
          </div>

        </div>
      </div>
    </div>

    <!-- Backdrop -->
    <div class="modal-backdrop fade show"></div>
  </div>
</template>

<script>
import { computed } from 'vue'
import { useStore } from 'vuex'

export default {
  name: 'ConfirmModalComponent',
  setup() {
    const store = useStore()

    const confirm = computed(() => store.getters['confirm/confirm'])

    const close = () => {
      store.dispatch('confirm/closeConfirm')
    }

    const confirmAction = () => {
      store.dispatch('confirm/confirm')
    }

    return {
      confirm,
      close,
      confirmAction
    }
  }
}
</script>
