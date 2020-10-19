from flask import Flask, request, make_response
import json
import math


app = Flask(__name__)

time = range(1, 100000)
height = [2*t for t in time]
leaves = [math.sin(t) for t in time]


@app.route('/')
def hello_world():
    date = request.args.get('date')
    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[9:11])
    index = (360 * (year - 2020)) + (30 * month) + day
    data = json.dumps({
        'data': [{
            'date': time[index],
            'plant_height': height[index],
            'plant_leaves': int(abs(leaves[index] * 20))
        }]
    })
    res = make_response((data, 200))
    res.headers['Content-Type'] = 'application/json'
    return res


def run_simulate():
    app.run(host="localhost", port=8000)
