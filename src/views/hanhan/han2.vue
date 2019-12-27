<template>
  <div class="chart-container">
    <chart height="100%" width="100%" />
  </div>
</template>

<script>
// import echarts from 'echarts'
var echarts = require('echarts')

export default {
  name: 'Han2',
  components: { 'chart': echarts },
  props: {
    className: {
      type: String,
      default: 'chart'
    },
    id: {
      type: String,
      default: 'chart'
    },
    width: {
      type: String,
      default: '200px'
    },
    height: {
      type: String,
      default: '200px'
    }
  },
  data() {
    return {
      chart: null
    }
  },
  mounted() {
    this.initChart()
  },
  beforeDestroy() {
    if (!this.chart) {
      return
    }
    this.chart.dispose()
    this.chart = null
  },
  methods: {
    initChart() {
      this.chart = echarts.init(this.$el)
      this.chart.setOption({
        title: {
          text: 'ECharts -han2_test'
        },
        tooltip: {},
        xAxis: {
          data: ['啊', '喔', '额', '咦', '呜']
        },
        yAxis: {},
        series: [{
          name: 'han2',
          type: 'bar',
          data: [5, 20, 36, 10, 10]
        }]
      })
    }
  }
}
</script>

<style>
.chart-container{
  position: relative;
  width: 100%;
  height: calc(100vh - 84px);
}
</style>

