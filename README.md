                                                                ****🚀 Monitoring App — All-in-One Monitoring Stack****

A simple and powerful **Dockerized monitoring solution** using **Prometheus**, **Loki**, **Alertmanager**, **Promtail**, and a custom **Python application** — all set up using **Docker Compose**.

Ideal for developers, DevOps engineers, and SREs looking to monitor apps in real time with minimal setup.


🔍 **Features**

✅ Application monitoring via Prometheus  
✅ Log aggregation via Loki & Promtail  
✅ Alerting with Alertmanager  
✅ Python app that exposes Prometheus metrics  
✅ Docker Compose for easy deployment

---

📦 **Tech Stack**

| Tool         | Purpose                        |
|--------------|--------------------------------|
| 🐍 Python     | Custom app exposing `/metrics` |
| 📈 Prometheus | Metrics collection & alerting |
| 📄 Promtail   | Collects logs and sends to Loki |
| 📦 Loki       | Log aggregation & querying     |
| 🚨 Alertmanager | Manages alert notifications  |
| 🐳 Docker Compose | Service orchestration    |

---

📁 **Project Structure**

monitoring-app/
├── app.py # Python app (exposes metrics)
├── Dockerfile # Build for Python app
├── docker-compose.yml # Orchestrates entire stack
├── prometheus.yml # Prometheus config
├── alert.rules.yml # Alert rules
├── alertmanager.yml # Alertmanager config
├── loki-config.yml # Loki config
├── promtail-config.yml # Promtail config
├── requirements.txt # Python dependencies

**⚙️ Step-by-Step Setup Guide**

🧰 **Step 1: Prerequisites**

Ensure the following are installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

📥 **Step 2: Clone the Repository**

git clone https://github.com/aguleria3003/monitoring-app.git
cd monitoring-app

🛠️ **Step 3: Run the App**
bash
Copy code
docker-compose up --build
This will start:

Python App (on http://localhost:8000/metrics)

Prometheus (on http://localhost:9090)

Alertmanager (on http://localhost:9093)

Loki (on http://localhost:3100)

✅ Logs will be collected from the Python app and sent to Loki.

🔍 **Step 4: Explore the Monitoring Stack**
Tool	URL
📈 Prometheus	http://localhost:9090
🚨 Alertmanager	http://localhost:9093
🐍 Python App	http://localhost:8000/metrics
📦 Loki API	http://localhost:3100

You can use tools like Grafana to connect to Prometheus & Loki for dashboards.

⚠️ **Alerts Configuration (Optional)**
Alerts are defined in alert.rules.yml. Example:

**- alert: HighRequestRate
  expr: rate(request_count[1m]) > 5
  for: 1m
  labels:
    severity: warning
  annotations:
    summary: High request rate detected**
Alerts are managed via Alertmanager, configured in alertmanager.yml.

📜 **Sample Python App (app.py)**
This app exposes a /metrics endpoint using prometheus_client:

from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)
REQUEST_COUNT = Counter("request_count", "Total number of requests")

@app.route("/")
def hello():
    REQUEST_COUNT.inc()
    return "Hello, Monitoring World!"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200
    
🔄 **Logs with Loki & Promtail**
Promtail reads logs from the Python container
Logs are sent to Loki, which you can query (e.g., using Grafana)

Example log query (if connected via Grafana):
logql
Copy code
{app="monitoring-app"} |= "ERROR"
🔧 Customization Tips
What You Want to Do	File to Edit
Add new alerts	alert.rules.yml
Add services to be scraped	prometheus.yml
Change logging config	promtail-config.yml
Add dependencies	requirements.txt
Customize the Python app	app.py

✅ **To Stop the Stack**
docker-compose down

📬 **Support Alerts via Email/Slack**
To enable notifications via email or Slack, update alertmanager.yml with your credentials:
receivers:
  - name: 'team'
    email_configs:
      - to: 'you@example.com'
👤 **Author**
Ankit Guleria
GitHub: @aguleria3003

⭐️ Like this project?
Give it a ⭐️ on GitHub — it helps others find it!
