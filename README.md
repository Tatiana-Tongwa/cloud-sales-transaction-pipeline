# Automated Cloud Sales & Transaction Processing Pipeline

**Project Status:** In Development  
**Target Completion:** October 31, 2026

## Project Overview

The Automated Cloud Sales & Transaction Processing Pipeline is a data engineering project designed to build a scalable, repeatable batch-processing solution for e-commerce transaction data.

The pipeline aims to ingest raw sales records, perform data cleaning, schema validation, deduplication, and currency conversion into EUR using PySpark, before storing curated datasets in Delta Lake for SQL-based business analytics.

The project also emphasizes cloud infrastructure, workflow automation, data quality monitoring, team collaboration, and performance benchmarking.

## Technology Stack and Responsibilities

| Tool / Platform | Specific Role in the Project |
|---|---|
| **Amazon S3** | Store raw sales transaction files in a cloud bucket, organized into folders for ingestion, auditing, and reprocessing. |
| **Python / PySpark** | Develop ETL transformations to clean transactions, validate schemas, remove duplicates, process missing values, and convert currencies into EUR. |
| **Databricks** | Provide a managed cloud environment for executing PySpark workloads, scheduling processing jobs, and monitoring pipeline execution independently of individual team members' computers. |
| **Delta Lake** | Store cleaned and curated transactional data in reliable tables, using ACID transactions, schema enforcement, and data versioning. |
| **SQL** | Develop analytical queries and reporting views for daily revenue, product-category sales, transaction trends, and month-over-month growth. |
| **Git & GitHub** | Maintain version control, document development, coordinate team contributions, manage issues and milestones, and track project progress. |
| **GitHub Actions & pytest** | Automate testing and code validation to help maintain pipeline reliability as changes are introduced. |
| **Conda & Java JDK** | Manage reproducible local Python environments and provide the Java runtime required for local PySpark execution. |

## Planned Pipeline Architecture

**AWS S3 → PySpark / Databricks → Delta Lake → SQL Analytics**

The pipeline will follow a Bronze, Silver, and Gold architecture:

- **Bronze:** Preserve raw sales data and ingestion metadata.
- **Silver:** Validate, clean, deduplicate, and standardize transaction records.
- **Gold:** Produce curated analytical tables for sales and revenue reporting.

Direct S3-to-Databricks integration remains subject to verification of the available free-tier capabilities.

## Data Sources

The primary dataset will be the **Brazilian E-Commerce Public Dataset by Olist**, supplemented by documented exchange-rate data and clearly identified synthetic multi-currency records where necessary.

## Project Performance Objectives

The project will evaluate its effectiveness through measurable indicators, including:

- Number of transactions processed.
- Duplicate and invalid records detected.
- Currency conversion accuracy.
- Pipeline processing time and successful execution rates.
- SQL query execution time and measurable optimization results.
- Automated test results and pipeline reproducibility.

Actual performance figures will be reported following implementation and testing.
