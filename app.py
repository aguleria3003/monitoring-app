from flask import Flask, jsonify, request
import psutil
import time
import logging
from prometheus_flask_exporter import PrometheusMetrics
from pythonjsonlogger import jsonlogger

# Create Flask app
app = Flask(__name__)

# Set up structured JSON logging
logger = logging.getLogger()
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(name)s %(message)s')
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

# Initialize Prometheus metrics
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='1.0.0')

# Common metrics - simplified to avoid request object issues
@app.route('/health')
def health():
    logger.info("Health endpoint called", extra={"endpoint": "/health"})
    return {'status': 'healthy'}, 200

@app.route('/simulate_load')
def simulate_load():
    logger.info("Simulate load endpoint called", extra={"endpoint": "/simulate_load"})
    # Simulate CPU load for 5 seconds
    start_time = time.time()
    while time.time() - start_time < 5:
        [x*x for x in range(10000)]
    cpu_usage = psutil.cpu_percent()
    logger.warning(f"High CPU usage simulated: {cpu_usage}%", 
                  extra={"cpu_usage": cpu_usage, "endpoint": "/simulate_load"})
    return {'message': 'CPU load simulated', 'cpu_usage': f'{cpu_usage}%'}, 200

@app.route('/error')
def error():
    logger.error("This is a simulated error", extra={"endpoint": "/error"})
    return {'error': 'Simulated error'}, 500

@app.route('/metrics')
def metrics_endpoint():
    # This endpoint is automatically handled by prometheus_flask_exporter
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
