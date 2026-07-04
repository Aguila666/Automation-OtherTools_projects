# Automation-OtherTools_projects Repository 🚀

This repository contains **multi-language Data Science, Automation, and Pipeline Engineering projects**.  

Each project consists of **12 exercises**, one for each language, covering multiple tools and subjects.  

The goal is to build strong **data science skills**, **automation/system design thinking**, and prepare for **production/system integration concepts**.  

---

## 🌍 Supported Languages

Spanish | Chinese | Portuguese | Arabic | Italian | Japanese | French | Korean | English | Russian | German | Hindi

> Each project includes exercises in all 12 languages, written natively in the target language.

---

## 🏗 Project Overview

Each project contains:

- **Tasks**: Each exercise focuses on one task combining Data Science, Automation, and Pipeline Engineering concepts.  
- **Industry Context**: Flexible per project (Automotive, Finance, Healthcare, etc.).  
- **Tool Distribution**: Each exercise dynamically uses multiple tools and subjects to ensure full coverage of your toolset.  

### Example Tools / Subjects Used

Excel | Power BI | Pandas | NumPy | Matplotlib | Seaborn | Python | SQL Server | MongoDB | Apache Airflow | Luigi | AWS (LocalStack) | Azure (Azurite) | AWS Lambda | LlamaIndex | Robocorp | n8n | PySpark | Deep Learning | Machine Learning | Probability | Statistics | Business Consulting Methods | Finance | Calculus | Algebra

---

## 🧩 Exercise Structure

Each exercise includes:

1. **Task description** in the target language  
2. **Objective** – what the exercise aims to achieve  
3. **Tools/Topics used**  
4. **Step-by-step instructions**  
5. **Expected output**  
6. **Dataset generation (optional)** – code to create realistic data with challenges (missing values, duplicates, outliers, inconsistencies)  
7. **Insights / Reports** – analysis and summaries stored in `reports/`  

> Exercises are designed to be **educational, practical, and suitable for GitHub portfolios**.

---

## ⚙️ System Layer / Future-Proofing

To prepare for professional production and system integration, the repository includes **lightweight, future-proof layers**:

| Area | Importance |
| --- | --- |
| APIs | Systems communication & integration |
| Docker | Reproducibility & containerized environments |
| Linux | Infrastructure reality & automation |
| FastAPI | Serving models/services |
| MLOps | Production AI & model lifecycle management |
| Monitoring | Reliability, logging, metrics, and dashboards |
| CI/CD | Automation pipelines & workflow orchestration |
| Cloud | Deployment & simulation environments |
| System Design | Scalability & architectural thinking |

**Recommendation:** These folders exist now, even if initially empty, to **avoid painful restructuring later**.

---

## 💻 Recommended Programming Languages

**CORE STACK (active focus)**

- Python  
- SQL  
- Linux concepts  
- APIs / FastAPI  
- Docker  
- System thinking  

**SECONDARY LAYER (gradual focus)**

- JavaScript – For dashboards, web interfaces, browser automation, and interactive tools.  
- Bash / Shell scripting – For Linux, automation, pipelines, and DevOps tasks.  
- C++ – Robotics, embedded systems, and performance-critical code (gradual integration).  

**Lower priority for now:** Java and Scala (enterprise/niche use cases).

> Focus on **one main active layer** to prevent cognitive overload and allow consistent progress

---

## 🗂 Folder Structure

```text
Automation-OtherTools_projects/

├─ README.md                                # Repository overview, goals, architecture, exercise instructions
├─ .gitignore                               # Ignore venvs, cache, logs, temp files, secrets
├─ .vscode/
│   └─ settings.json                        # VS Code repo-level customization
├─ utils/
│   ├─ dataset_generators/                  # Scripts to generate synthetic datasets
│   ├─ dataset_quality/                     # Reusable dataset validation utilities
│   │ ├── dataset_quality_check.py          # Entry point
│   │ ├── scoring.py                        # Score calculation
│   │ ├── report_generator.py               # Report generation
│   │ ├── visualizations.py                 # Quick graphs
│   │ ├── rules.py                          # Evaluation rules
│   │ └── __init__.py
│   ├─ pipeline_helpers/                    # Helper functions for ETL and automation pipelines
│   ├─ visualization_helpers/               # Plotting, dashboards, and reporting utilities
│   ├─ sql_helpers/                         # SQL query and connection helpers
│   ├─ automation_helpers/                  # Robocorp, n8n, and Airflow helper scripts
│   ├─ cloud_helpers/                       # LocalStack, Azurite, AWS Lambda helper functions
│   └─ .gitkeep                              # Keeps folder tracked in Git
├─ diagrams/
│   ├─ pipelines/                           # ETL pipeline diagrams
│   ├─ orchestration/                       # Workflow orchestration diagrams
│   ├─ cloud_architecture/                  # Cloud deployment diagrams
│   ├─ docker/                              # Containerization diagrams
│   ├─ airflow/                             # DAG visualization diagrams
│   ├─ monitoring/                          # Logging and metrics diagrams
│   ├─ system_design/                       # Scalability and architecture diagrams
│   └─ .gitkeep
├─ deployment/
│   ├─ docker/                              # Dockerfiles and docker-compose configs
│   ├─ fastapi/                             # FastAPI services and APIs
│   ├─ mlops/                               # Model deployment experiments
│   ├─ monitoring/                          # Logging and alerting configurations
│   ├─ ci_cd/                               # GitHub Actions, Azure pipelines, or automation scripts
│   ├─ cloud/                               # Cloud deployment experiments and simulations
│   └─ .gitkeep
├─ infrastructure/
│   ├─ linux/                               # Linux practice scripts and exercises
│   ├─ bash/                                # Bash/Shell scripting exercises
│   ├─ kubernetes/                          # Kubernetes practice files and examples
│   ├─ networking/                          # Networking/system communication experiments
│   ├─ system_design/                       # Architecture and scalability exercises
│   └─ .gitkeep
├─ app/
│   ├─ dashboards/                          # Streamlit/Dash/Power BI dashboards
│   ├─ automation_apps/                     # Robocorp/n8n/Airflow integrated applications
│   ├─ web_tools/                           # Browser automation utilities
│   ├─ browser_tools/                       # Selenium/Playwright scripts
│   ├─ frontend/                            # JavaScript and frontend experiments
│   └─ .gitkeep
├─ database/
│   ├─ create_database.sql                  # SQL script to create AutomationProjectsDB
│   ├─ create_schemas.sql                   # SQL script to create schemas
│   ├─ schemas/
│   │   ├─ etl/
│   │   │   ├─ tables/
│   │   │   ├─ procedures/
│   │   │   ├─ views/
│   │   │   └─ functions/
│   │   ├─ pipelines/
│   │   │   ├─ tables/
│   │   │   ├─ procedures/
│   │   │   ├─ views/
│   │   │   └─ functions/
│   │   ├─ monitoring/
│   │   │   ├─ tables/
│   │   │   ├─ procedures/
│   │   │   ├─ views/
│   │   │   └─ functions/
│   │   ├─ automation/
│   │   │   ├─ tables/
│   │   │   ├─ procedures/
│   │   │   ├─ views/
│   │   │   └─ functions/
│   │   ├─ staging/
│   │   │   ├─ tables/
│   │   │   ├─ procedures/
│   │   │   ├─ views/
│   │   │   └─ functions/
│   │   ├─ warehouse/
│   │   │   ├─ fact_tables/
│   │   │   ├─ dimension_tables/
│   │   │   ├─ procedures/
│   │   │   ├─ views/
│   │   │   └─ functions/
│   │   ├─ orchestration/
│   │   │   ├─ tables/
│   │   │   ├─ procedures/
│   │   │   ├─ views/
│   │   │   └─ functions/
│   │   └─ cloud/
│   │       ├─ tables/
│   │       ├─ procedures/
│   │       ├─ views/
│   │       └─ functions/
│   ├─ seed_data/
│   │   ├─ automotive/
│   │   ├─ finance/
│   │   ├─ healthcare/
│   │   ├─ logistics/
│   │   └─ .gitkeep
│   ├─ backups/
│   │   └─ .gitkeep
│   ├─ documentation/
│   │   ├─ ERD/
│   │   ├─ schema_explanations/
│   │   ├─ business_rules/
│   │   └─ .gitkeep
│   └─ migration_scripts/
│       └─ .gitkeep
├─ Project1_AutomotiveIndustry/
│   ├─ Car_Manufacturing/
│   │   ├─ shared_resources/
│   │   │   ├─ datasets/
│   │   │   ├─ sql/
│   │   │   ├─ configs/
│   │   │   └─ diagrams/
│   │   ├─ 01_Spanish/
│   │   │   ├─ datasets/
│   │   │   │   ├─ raw/
│   │   │   │   └─ processed/
│   │   │   ├─ notebooks/
│   │   │   ├─ scripts/
│   │   │   ├─ sql/
│   │   │   ├─ reports/
│   │   │   ├─ models/
│   │   │   ├─ configs/
│   │   │   ├─ logs/
│   │   │   ├─ photos/                         # Evidence of exercises or outputs
│   │   │   ├─ videos/                         # Recorded demos or simulations
│   │   │   └─ README.md                        # Exercise explanation/objectives
│   │   ├─ 02_Chinese/
│   │   ├─ 03_Portuguese/
│   │   ├─ 04_Arabic/
│   │   ├─ 05_Italian/
│   │   ├─ 06_Japanese/
│   │   ├─ 07_French/
│   │   ├─ 08_Korean/
│   │   ├─ 09_English/
│   │   ├─ 10_Russian/
│   │   ├─ 11_German/
│   │   └─ 12_Hindi/
│   ├─ Auto_Parts_Manufacturing/
│   ├─ Electric_Vehicles/
│   ├─ Supply_Chain/
│   └─ Predictive_Maintenance/
├─ Project2_FinanceIndustry/
├─ Project3_HealthcareIndustry/
├─ Project4_LogisticsIndustry/
├─ Project5_RetailIndustry/
└─ Project6_OtherIndustry/

---

## ⚡ How It Works

- Exercises use **dynamic tool-topic shuffle**, so each task leverages multiple tools and subjects.  
- Multi-language exercises are **written in their target language**, not translated into English.  
- Datasets are **realistic and challenging**, simulating real-world industrial scenarios with missing values, duplicates, outliers, and inconsistencies.  
- Exercises incorporate both **Data Science and Automation concepts** as well as **system/infrastructure thinking** including Docker, FastAPI, Linux, Bash, CI/CD, monitoring, and cloud simulation.  
- Optional tools like **Power BI, AWS Lambda, and Robocorp Cloud** are included for enhanced industrial realism and integration practice.

---

## 🧪 Dataset Quality Validation

Before starting any exercise, datasets can be validated using the reusable utility located in:

utils/dataset_quality/dataset_quality_check.py

The objective of this step is to quickly determine whether a dataset is suitable for:

Exploratory Data Analysis (EDA)
Machine Learning
Predictive Modeling
Automation Pipelines
Reporting and Dashboards

The validation script performs a quick assessment of several quality indicators, including:

Missing values
Duplicate records
Data types
Cardinality
Class imbalance (classification datasets)
Correlation between numerical variables
Target variable variability
Potential data leakage
Constant or near-constant columns
Dataset size
Overall quality score

This validation step helps avoid spending time building pipelines on datasets that contain little predictive information or are unsuitable for meaningful analysis.

Recommended workflow:

Generate Dataset
        │
        ▼
Dataset Quality Check
        │
        ▼
EDA
        │
        ▼
Feature Engineering
        │
        ▼
Machine Learning
        │
        ▼
Automation
        │
        ▼
Reporting

---

## 📌 Notes

- Reports and insights in the `reports/` folder are for **review, learning, and sharing**.  
- Exercises are modular, **reusable across projects**, and encourage building a **portfolio demonstrating professional-level skills**.  
- The repository integrates a **system layer**, preparing for real-world production environments and future-proofing engineering practices.  
- Multi-layered structure allows progressive focus: **Data & Analytics → Automation → Services → Infrastructure → Production → Architecture**.

---

## 🚀 Goal

- Build strong **Data Science and Analytics skills** using realistic industrial datasets.  
- Develop **automation, pipeline engineering, and system design thinking**.  
- Gain exposure to **production-oriented technologies**: Docker, FastAPI, MLOps, CI/CD, monitoring, Linux, Bash, and cloud simulation.  
- Create a **professional, shareable portfolio**, demonstrating multi-layer engineering competence.  
- Maintain flexibility to incorporate **optional advanced tools** like **Power BI, AWS Lambda, and Robocorp Cloud**.