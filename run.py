# -*- coding: utf-8 -*-
from flask import Flask,request

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
  model_id = request.values.get('model_id')
  print "model_id:",model_id
  if model_id:
    result = [result[int(model_id)]]
  return json.dumps(result)

@app.route('/chart_get',methods = ['GET'])
def chart_get():
  result = [{},{}]
  result[0]['title'] = 'ECharts - line'
  result[0]['xAxis'] = ['啊', '喔', '额', '咦', '呜']
  result[0]['series'] = {'name':'han6_line','type': 'line','data': [5, 20, 36, 10, 10]}
  result[1]['title'] = 'ECharts - bar'
  result[1]['xAxis'] = ['啊1', '喔1', '额1', '咦1', '呜1']
  result[1]['series'] = {'name':'han6_bar','type': 'bar','data': [51, 201, 361, 10, 101]}
  print result
  return json.dumps(result)

if __name__ == '__main__':
  app.run(debug=True)
