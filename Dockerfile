FROM apache/airflow:2.7.1-python3.9

USER root

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Add pipelines to Python path
ENV PYTHONPATH="${PYTHONPATH}:/opt/airflow"

USER airflow

# Copy requirements file
COPY requirements.txt /opt/airflow/requirements.txt

# Install packages
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /opt/airflow/requirements.txt