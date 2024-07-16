from flask import Flask
from flask_restful import Api, Resource
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
api = Api(app)
metrics = PrometheusMetrics(app)


@app.route('/')
def main():
    return 'OK'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
