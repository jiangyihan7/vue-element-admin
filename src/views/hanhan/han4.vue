<template>
  <div>
    <div v-if="loginType === 'username'">
      Username<el-input v-model="input1" placeholder="Enter your username" />
    </div>
    <div v-else>
      <div>
        Email<el-input v-model="input1" placeholder="Enter your email address" />
      </div>
    </div>
    <div>
      <el-button @click="toggleFuc">Toggle Type</el-button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      input1: '',
      loginType: 'username'
    }
  },
  methods: {
    toggleFuc: function() {
      this.loginType = this.loginType === 'username' ? '' : 'username'
    }
  }
}
</script>
