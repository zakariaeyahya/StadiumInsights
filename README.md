# StadiumInsights

**StadiumInsights** est un projet innovant de data engineering qui vise à collecter, transformer et visualiser des données détaillées sur les stades de football à travers le monde. Ce pipeline de données entièrement automatisé offre une analyse complète des infrastructures sportives globales.

## 🏟️ Aperçu du Projet

StadiumInsights combine web scraping, traitement de données, stockage cloud et visualisation pour fournir des insights uniques sur les stades de football internationaux.

## 🚀 Fonctionnalités Principales

* **Collecte de Données Automatisée** 
  * Extraction de données à partir de sources web multiples
  * Utilisation de techniques avancées de web scraping avec Python
  * Couverture de stades du monde entier

* **Transformation de Données Intelligente**
  * Nettoyage et standardisation des données
  * Enrichissement des informations géographiques
  * Gestion des inconsistances et valeurs manquantes

* **Infrastructure Technique Robuste**
  * Pipeline ETL entièrement automatisé
  * Stockage des données dans Snowflake
  * Visualisation interactive avec Power BI

## 🛠 Technologies

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-Orchestration-orange)
![Snowflake](https://img.shields.io/badge/Snowflake-Data%20Warehouse-blue)
![Power BI](https://img.shields.io/badge/Power%20BI-Visualization-yellow)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)

## 📂 Structure du Projet
![WhatsApp Image 2024-12-09 à 21 53 39_deb5b51c](https://github.com/user-attachments/assets/47cc95b1-fd6d-408f-ac1a-9b18185cd12c)

```
StadiumInsights/
├── data/               # Données brutes et transformées
├── dags/               # Scripts Apache Airflow
├── pipelines/          # pipelines de données
├── docker-compose.yml  # Configuration Docker
└── dockerfile
└── requirements.txt          

```

## 🔧 Installation & Configuration

### Prérequis

* Python 3.12+
* Docker
* Compte Snowflake
* Power BI Desktop

### Étapes d'Installation

1. Cloner le dépôt
```bash
git clone https://github.com/votre-username/StadiumInsights.git
cd StadiumInsights
```

2. Installer les dépendances
```bash
pip install -r requirements.txt
```

3. Démarrer l'environnement Docker
```bash
docker-compose up
```

## 🔍 Fonctionnalités Détaillées

### Extraction de Données
* Scraping automatisé de Wikipedia et autres sources
* Collecte d'informations sur la capacité, localisation, année de construction

### Transformation
* Nettoyage des données avec Pandas
* Normalisation des formats
* Enrichissement géographique

### Analyse
* Requêtes SQL avancées sur Snowflake
* Tableaux de bord interactifs Power BI
![WhatsApp Image 2024-12-07 à 12 12 04_0abf7b85](https://github.com/user-attachments/assets/6af27a05-ade4-43ef-857e-09b6b846acca)

## 📊 Résultats & Insights

* Classements des stades par capacité
* Analyses géographiques détaillées
* Visualisations interactives des infrastructures sportives
![WhatsApp Image 2024-12-09 à 21 50 27_6502b565](https://github.com/user-attachments/assets/75ffafc6-abe0-44b4-9b33-994892db2e27)

## 📄 Licence

Projet sous licence MIT

## 👥 Auteurs

* **Zakariae Yahya** - *Data Scientist* - [Profil GitHub](https://github.com/zakariaeyahya)

## 📬 Contact

📧 Email : zakariae.yh@gmail.com
🔗 LinkedIn : [Profil LinkedIn](https://www.linkedin.com/in/zakariae-yahya/)

---

**💡 Dernière mise à jour :** Décembre 2024
