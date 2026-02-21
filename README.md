# End-to-End Data Engineering Pipeline

## 📌 Project Overview

This project implements a batch data engineering pipeline designed to ingest, store, and prepare e-commerce data for analytical use.

The goal is to simulate a real-world data engineering workflow including ingestion, raw data storage, transformation, and preparation for a data warehouse.

## 🏗 Architecture Overview

```
Sources (API, CSV) → Raw Data Storage → Transformation (staging) → Data Warehouse → BI / Analytics
```

## 📂 Project Structure

```
src/
  ingestion/
  transformation/
  warehouse/
  utils/
  config/

data/
  raw/
  staging/
  analytics/
```

## 🚀 How to Run the Ingestion

### 1. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run API ingestion

```bash
python src/ingestion/api_ingestion.py
```

Raw files will be stored in:

```
data/raw/
```

## 🎯 Objectives of the Ingestion Layer

- Retrieve data from external APIs and files
- Store data in raw format without modification
- Ensure reproducibility using timestamped files
- Maintain traceability of ingested data

## 🛠 Tech Stack

- Python
- REST APIs
- JSON
- File-based raw storage
- *(Airflow – upcoming)*