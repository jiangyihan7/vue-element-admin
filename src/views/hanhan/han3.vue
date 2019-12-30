<template>
  <div>
    <el-select v-model="value" placeholder="请选择" @change="getTableData(value)">
      <el-option
        v-for="item in options"
        :key="item.value"
        :label="item.label"
        :value="item.value"
      />
    </el-select>
    <el-table :data="tableData" style="width: 100%">
      <el-table-column label="版本id" width="180">
        <template slot-scope="scope">
          <span style="margin: 10px">{{ scope.row.id }}</span>
        </template>
      </el-table-column>
      <el-table-column label="模型名称" width="180">
        <template slot-scope="scope">
          <span style="margin: 0px">{{ scope.row.name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="更新周期" width="180">
        <template slot-scope="scope">
          <span style="margin: 10px">{{ scope.row.cycle_type }}</span>
        </template>
      </el-table-column>
      <el-table-column label="关联业务" width="180">
        <template slot-scope="scope">
          <span style="margin: 10px">{{ scope.row.business_labels }}</span>
        </template>
      </el-table-column>
      <el-table-column label="状态" width="180">
        <template slot-scope="scope">
          <span style="margin: 0px">{{ scope.row.status }}</span>
        </template>
      </el-table-column>
      <el-table-column label="版本" width="180">
        <template slot-scope="scope">
          <span style="margin: 0px">{{ scope.row.version }}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
          <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      options: [{
        value: '0',
        label: '粗排-CTR-标准'
      }, {
        value: '1',
        label: '精排-CVR-非标'
      }, {
        value: '2',
        label: '精排-CVR-标准'
      }
      ],
      value: '',
      tableData: []
    }
  },
  mounted: function() {
    this.getTableData()
  },
  methods: {
    handleEdit(index, row) {
      console.log(index, row)
    },
    handleDelete(index, row) {
      console.log(index, row)
    },

    getTableData(value) {
      axios({
        method: 'get',
        url: 'http://localhost:5000/model_get',
        params: {
          model_id: this.value
        }
      }).then((response) => {
        this.tableData = response.data
      }).catch(function(error) {
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>

  .chart-container {
    position: relative;
    width: 100%;
    height: calc(100vh - 84px);
  }
</style>
