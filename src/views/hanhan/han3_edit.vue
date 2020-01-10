<template>
  <div>
    模型名称：<el-input v-model="model_name" />
    更新周期：<el-radio v-model="cycle" label="0">天级</el-radio>
    <el-radio v-model="cycle" label="1">手动</el-radio>
  </div>
</template>

<script>
export default {
  data() {
    return {
      model_name: '',
      cycle: '1'
    }
  }
}
</script>
