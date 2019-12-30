<template>
  <div class="chart-container">
    <chart :options="line1" height="100%" width="100%" />
  </div>
</template>

<script>
import echarts from 'vue-echarts'
import axios from 'axios'
// var echarts = require('echarts')
import 'echarts/lib/component/title'
import 'echarts/lib/component/tooltip'
import 'echarts/lib/chart/line'

export default {
  name: 'Han2',
  components: { 'chart': echarts },
  data() {
    return {
      line1: {
        title: {
          text: ''
        },
        tooltip: {
          trigger: 'item'
        },
        xAxis: {
          data: []
        },
        yAxis: {},
        series: [{
          name: '',
          type: 'line',
          data: []
        }]
      }
    }
  },
  // props: {
  //  className: {
  //    type: String,
  //    default: 'chart'
  //  },
  //  id: {
  //    type: String,
  //    default: 'chart'
  //  },
  //  width: {
  //    type: String,
  //    default: '200px'
  //  },
  //  height: {
  //    type: String,
  //    default: '200px'
  //  }
  // },
  // data() {
  //  return {
  //    chart: null
  //  }
  // },
  // mounted() {
  //  this.initChart()
  // },
  // beforeDestroy() {
  //  if (!this.chart) {
  //    return
  //  }
  //  this.chart.dispose()
  //  this.chart = null
  //  },
  mounted() {
    axios({
      method: 'get',
      url: 'http://localhost:5000/chart_get'
    }).then((response) => {
      this.line1.title.text = response['data']['title']
      this.line1.xAxis.data = response['data']['xAxis']
      this.line1.series[0].name = response['data']['series']['name']
      this.line1.series[0].type = response['data']['series']['type']
      this.line1.series[0].data = response['data']['series']['data']
    }).catch(function(error) {
      console.log(error)
    })
  }
}
// methods: {
//  initChart() {
//    this.chart = echarts.init(this.$el)
//    this.chart.setOption({
//      title: {
//        text: 'ECharts -han2_test'
//      },
//      tooltip: {},
//      xAxis: {
//        data: ['啊', '喔', '额', '咦', '呜']
//      },
//      yAxis: {},
//      series: [{
//        name: 'han2',
//        type: 'bar',
//        data: [5, 20, 36, 10, 10]
//      }]
//    })
//  }
// }
// }
</script>

<style>
.chart-container{
  position: relative;
  width: 100%;
  height: calc(100vh - 84px);
}
</style>

