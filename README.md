
---

# StadiumInsights

**StadiumInsights** is an innovative data engineering project designed to collect, transform, and visualize detailed data on football stadiums worldwide. This fully automated data pipeline provides comprehensive analysis of global sports infrastructures.

## 🏟️ Project Overview
StadiumInsights combines web scraping, data processing, cloud storage, and visualization to deliver unique insights into international football stadiums.

## 🚀 Key Features
- **Automated Data Collection**
  - Data extraction from multiple web sources
  - Advanced web scraping techniques using Python
  - Coverage of stadiums around the world
- **Smart Data Transformation**
  - Data cleaning and standardization
  - Geographic information enrichment
  - Handling inconsistencies and missing values
- **Robust Technical Infrastructure**
  - Fully automated ETL pipeline
  - Data storage in Snowflake
  - Interactive visualization with Power BI

## 🛠 Technologies
![Python](https://img.shields.io/badge/Python-3.12+-blue)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-Orchestration-orange)
![Snowflake](https://img.shields.io/badge/Snowflake-Data%20Warehouse-blue)
![Power BI](https://img.shields.io/badge/Power%20BI-Visualization-yellow)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)

## 📂 Project Structure
![image](https://github.com/user-attachments/assets/f2697b3b-c99a-4801-803b-09e1dbdf0e4f)
```
StadiumInsights/
├── data/               # Raw and transformed data
├── dags/               # Apache Airflow scripts
├── pipelines/          # Data pipelines
├── docker-compose.yml  # Docker configuration
└── dockerfile
└── requirements.txt
```

## 🔧 Installation & Setup
### Prerequisites
- Python 3.12+
- Docker
- Snowflake account
- Power BI Desktop

### Installation Steps
1. Clone the repository
   ```bash
   git clone https://github.com/votre-username/StadiumInsights.git
   cd StadiumInsights
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Start the Docker environment
   ```bash
   docker-compose up
   ```

## 🔍 Detailed Features
### Data Extraction
- Automated scraping from Wikipedia and other sources
- Collection of capacity, location, and year of construction information

### Transformation
- Data cleaning with Pandas
- Format normalization
- Geographic enrichment

### Analysis
- Advanced SQL queries on Snowflake
- Interactive Power BI dashboards
![WhatsApp Image 2024-12-07 à 12 12 04_0abf7b85](https://github.com/user-attachments/assets/6af27a05-ade4-43ef-857e-09b6b846acca)

## 📊 Results & Insights
- Stadium rankings by capacity
- Detailed geographic analysis
- Interactive visualizations of sports infrastructures
![image](https://github.com/user-attachments/assets/0782b3fb-1a95-4dd7-814c-d8b8bdecf959)

## 📄 License
This project is licensed under the MIT License.

## 👥 Authors
- **Zakariae Yahya** - *Data Scientist* - [GitHub Profile](https://github.com/zakariaeyahya)
- **Salaheddine Kayouh** - [GitHub Profile](https://github.com/771salameche)
- **Ryad Kaoutar** - [GitHub Profile](https://github.com/kawkawa324)

## 📬 Contact
📧 Email: zakariae.yh@gmail.com, kawtar.ryad@etu.uae.ac.ma, kayouhsalaheddine@gmail.com
🔗 LinkedIn: **Zakariae Yahya** - [LinkedIn Profile](https://www.linkedin.com/in/zakariae-yahya/)
🔗 LinkedIn: **Ryad Kaoutar** - [LinkedIn Profile](https://www.linkedin.com/in/ryad-kawtar-529884253/)
🔗 LinkedIn: **Salaheddine Kayouh** - [LinkedIn Profile](https://www.linkedin.com/in/salaheddine-kayouh/)

---
**💡 Last updated:** January 2025
