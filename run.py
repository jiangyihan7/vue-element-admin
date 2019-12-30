# -*- coding: utf-8 -*-
from flask import Flask

from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app)

@app.route('/model_get',methods = ["GET"])
def model_get():
  result =  [{
          'id': '1',
          'name': '粗排-CTR-标准',
          'cycle_type': '天级',
          'business_labels': '粗排',
          'status': '已上线(全量)',
          'version': 'v1.0',
        }, {
          'id': '2',
          'name': '精排-CVR-非标',
          'cycle_type': '天级',
          'business_labels': '精排',
          'status': '测试中',
          'version':'v2.0'
          }, {
          'id': '3',
          'name': '精排-CVR-标准',
          'cycle_type': '手动',
          'business_labels': '精排',
          'status': '已上线(小流量)',
          'version':'v3.0'
          }]
  return json.dumps(result)

@app.route('/chart_get',methods = ['GET'])
def chart_get():
  result = {}
  result['title'] = 'ECharts - han2_test'
  result['xAxis'] = ['啊', '喔', '额', '咦', '呜']
  result['series'] = {'name':'han2','type': 'line','data': [5, 20, 36, 10, 10]}
  return json.dumps(result)

if __name__ == '__main__':
  app.run(debug=True)
