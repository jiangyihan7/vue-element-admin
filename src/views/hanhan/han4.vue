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
    <div>
      <el-radio v-model="checked1" label="1">xuan</el-radio>
      <el-radio v-model="checked1" label="2">xu</el-radio>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      checked1: '',
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
