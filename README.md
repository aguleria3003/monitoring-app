🖥️ **Deploy a Flask-Based Web Application**

✅ **Steps:**
•	Create a Python Flask app with:
o	/health
o	/simulate_load
•	Write a Dockerfile using python:3.11-slim as the base image.
•	Build locally:
•	docker build -t monitored-app .
•	Test the container:
•	docker run -p 5000:5000 monitored-app
•	Push to Docker Hub:
•	docker tag monitored-app yourusername/monitored-app:latest
•	docker push yourusername/monitored-app:latest
📤 **Deliverable:** Docker image accessible at http://localhost:5000/health
________________________________________
🧾 **Initialize Version Control**
✅ **Steps:**
•	Initialize a Git repository and add .gitignore
•	Create main and monitoring branches
•	Push all code to GitHub
🔗 **Deliverable:** GitHub repository with both branches (main, monitoring)
________________________________________
📊 **Implement Metrics Collection (Prometheus)**
✅ **Steps:**
•	Install prometheus_flask_exporter and expose app metrics
•	Create prometheus.yml to scrape:
o	Flask app
o	Node Exporter
•	Run Prometheus and Node Exporter via Docker
🌐 **Deliverable:** Prometheus running at http://localhost:9090
________________________________________
📁 **Set Up Centralized Logging (Loki + Promtail)**
✅ **Steps:**
•	Add structured logging using structlog in the Flask app
•	Create docker-compose.yml with:
o	Flask app
o	Loki
o	Promtail
•	Verify logs appear in Loki UI
🌐 **Deliverable:** Logs accessible at http://localhost:3100
________________________________________
📈 **Create Grafana Dashboards**
✅ **Steps:**
•	Run Grafana via Docker:
•	docker run -d -p 3000:3000 grafana/grafana
•	Add data sources:
o	Prometheus
o	Loki
•	Build dashboards for:
o	🔥 CPU Usage
o	⏱️ Request Latency
o	📄 Application Logs
🌐 **Deliverable:** Grafana dashboards at http://localhost:3000
________________________________________
🚨 **Configure Alerting (Prometheus + Alertmanager)**
✅ **Steps:**
•	Create alert.rules.yml with conditions (e.g., CPU > 80%)
•	Configure Alertmanager with SMTP/email settings
•	Simulate CPU spike or downtime to trigger alerts
📩 **Deliverable:** Email screenshots of triggered alerts
________________________________________
⚙️ **Automate with CI/CD (GitHub Actions)**
✅ **Steps:**
•	Create workflow file: .github/workflows/ci-cd.yml
•	Automate:
o	Docker image build
o	Docker image push
•	(Optional) Add deployment steps for monitoring stack
🔁 **Deliverable:** GitHub Actions pipeline with full CI/CD automation

📊 **Pipeline Diagram**


<img width="2363" height="1074" alt="image" src="https://github.com/user-attachments/assets/f8ed8859-873d-479e-9097-9e5c28297481" />


