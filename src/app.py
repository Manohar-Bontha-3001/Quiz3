from flask import Flask, request, jsonify, render_template
from database import query_time_range, query_specific_time_net_value, modify_attribute
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query-time-range', methods=['POST'])
def query_time_range_endpoint():
    data = request.get_json()
    start_time = data['start_time']
    end_time = data['end_time']
    start_query_time = time.time()
    results = query_time_range(start_time, end_time)
    end_query_time = time.time()
    query_duration = end_query_time - start_query_time
    return jsonify({"results": results, "query_duration": query_duration})

@app.route('/query-specific-time-net-value', methods=['POST'])
def query_specific_time_net_value_endpoint():
    data = request.get_json()
    time_value = data['time']
    net_value = data['net_value']
    count = data['count']
    start_query_time = time.time()
    results = query_specific_time_net_value(time_value, net_value, count)
    end_query_time = time.time()
    query_duration = end_query_time - start_query_time
    return jsonify({"results": results, "query_duration": query_duration})

@app.route('/modify-attribute', methods=['POST'])
def modify_attribute_endpoint():
    data = request.get_json()
    time_value = data['time']
    new_values = (
        data['latitude'],
        data['longitude'],
        data['depth'],
        data['mag'],
        data['net'],
        data['id']
    )
    modify_attribute(time_value, new_values)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
