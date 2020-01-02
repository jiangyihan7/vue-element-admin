<template>
  <el-tabs v-model="activeName" type="card" @tab-click="handleClick">
    <el-tab-pane label="Home" name="first">Home123</el-tab-pane>
    <el-tab-pane label="Tab1" name="second">Tab1sdf</el-tab-pane>
    <el-tab-pane label="Tab2" name="third">Tab2dghdfgc</el-tab-pane>
  </el-tabs>
</template>

<script>
export default {
  data() {
    return {
      activeName: 'first'
    }
  },
  methods: {
    handleClick(tab, event) {
      console.log(tab, event)
    }
  }
}
</script>
