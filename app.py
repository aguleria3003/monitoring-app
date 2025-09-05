from flask import Flask, jsonify
import psutil
import time
import logging
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

@app.route('/health')
def health():
    logger.info("Health endpoint called - service is healthy", extra={"endpoint": "/health", "status": "healthy"})
    return {'status': 'healthy'}, 200

@app.route('/simulate_load')
def simulate_load():
    logger.info("Simulate load endpoint called - generating CPU load", extra={"endpoint": "/simulate_load"})
    # Simulate CPU load for 5 seconds
    start_time = time.time()
    while time.time() - start_time < 5:
        [x*x for x in range(10000)]
    cpu_usage = psutil.cpu_percent()
    logger.warning(f"High CPU usage simulated: {cpu_usage}%", 
                  extra={"cpu_usage": cpu_usage, "endpoint": "/simulate_load", "level": "warning"})
    return {'message': 'CPU load simulated', 'cpu_usage': f'{cpu_usage}%'}, 200

@app.route('/error')
def error():
    logger.error("This is a simulated error for testing purposes", 
                extra={"endpoint": "/error", "level": "error", "test": "true"})
    return {'error': 'Simulated error'}, 500

@app.route('/')
def home():
    logger.info("Home page accessed", extra={"endpoint": "/", "level": "info"})
    return {'message': 'Welcome to the monitoring app'}, 200

if __name__ == '__main__':
    logger.info("Starting Flask application on port 5000")
    app.run(host='0.0.0.0', port=5000)
