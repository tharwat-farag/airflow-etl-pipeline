# Airflow ETL Pipeline

A complete ETL pipeline project built with Apache Airflow and Astronomer for orchestrating, scheduling, and monitoring data workflows.

---

## Overview

This project demonstrates how to build and manage ETL workflows using:

* Apache Airflow
* Astronomer (Astro Runtime)
* Docker
* Python
* PostgreSQL

The pipeline automates data extraction, transformation, and loading processes while providing scheduling, monitoring, and task management through the Airflow UI.

---

## Features

* Automated ETL workflows using Airflow DAGs
* Task scheduling and orchestration
* Dockerized environment for easy setup
* Airflow Web UI for monitoring pipelines
* Modular DAG structure
* Example DAGs included
* Ready for local development and deployment

---

## Project Structure

```bash
.
├── dags/                  # Airflow DAGs
├── include/               # Additional project files
├── plugins/               # Custom Airflow plugins
├── tests/                 # DAG testing files
├── Dockerfile             # Astro runtime image
├── requirements.txt       # Python dependencies
├── airflow_settings.yaml  # Airflow local settings
├── .gitignore
└── README.md
```

---

## Technologies Used

* Python
* Apache Airflow
* Astronomer CLI
* Docker Desktop
* PostgreSQL

---

## Getting Started

### Prerequisites

Before running the project, make sure you have installed:

* Python 3.10+
* Docker Desktop
* Astronomer CLI

---

## Installation

Clone the repository:

```bash
git clone https://github.com/tharwat-farag/airflow-etl-pipeline.git
```

Move into the project directory:

```bash
cd airflow-etl-pipeline
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Project

Start Airflow locally using Astronomer:

```bash
astro dev start
```

Once the containers are running, open:

```text
http://localhost:8080
```

Default credentials:

```text
Username: admin
Password: admin
```

---

## Example DAGs

### etl_simple

A simple ETL pipeline DAG demonstrating:

* Extracting data
* Transforming data
* Loading data
* Task orchestration with Airflow

### simple_dag

Basic Airflow DAG example for scheduling and workflow execution.

---

## Monitoring

Airflow UI allows you to:

* Monitor DAG runs
* Track task status
* View logs
* Retry failed tasks
* Manage schedules

---

## Future Improvements

* Integrate cloud storage
* Add data validation checks
* Implement CI/CD pipelines
* Add Spark integration
* Deploy on Kubernetes

---

## Author

**Tharwat Farag**

* LinkedIn: [https://www.linkedin.com/in/tharwat-farag/](https://www.linkedin.com/in/tharwat-farag/)
* GitHub: [https://github.com/tharwat-farag](https://github.com/tharwat-farag)

---

## License

This project is for learning and portfolio purposes.

---

#Digilians
