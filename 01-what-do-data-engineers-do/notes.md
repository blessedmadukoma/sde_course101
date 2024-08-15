# 01. [What do data engineers do?](https://www.startdataengineering.com/post/n-job-reponsibilities-of-a-data-engineer/)

- [01. What do data engineers do?](#01-what-do-data-engineers-do)
  - [Notes](#notes)
  - [Key responsibilities of a Data Engineer:](#key-responsibilities-of-a-data-engineer)
  - [Assignment:](#assignment)
  - [Solution:](#solution)

## Notes
## Key responsibilities of a Data Engineer:
1. Moving data between different systems:
   - **Extract**: pulling data from a number of sources e.g. databases, cloud storages, external APIs.
   - **Transform**: performing certain actions on the data e.g. filtering, mapping, aggregating or changing the structure of the data (normalization and denormalization)
   - **Load**: sending the data into a different destination e.g another database, a cloud storage, data warehouse etc.
    
    Common tools or frameworks include pandas, spark, docker, kafka.

2. Managing data warehouses:
    - Warehouse data modeling: model data for analytical queries e.g. aggregating queries on large tables, applying partitions, handling fact and dimension tables etc.
    - Warehouse performance: make sure the queries are fast and scalable when needed.
    - Data quality
    
    Common:
      - modeling techniques: kimball modeling, data lake
      - frameworks and tools: dbt for data quality
      - warehouses: Snowflake, postgres, redshift

3. Data pipeline scheduling, orchestration, execution and monitoring: making sure data pipelines run without any issue
    
    Common:
      - frameworks and tools: Airflow, dbt, Prefect
      - databases: Postgres, MySQL
      - monitoring systems: datadog, newrelic

4. Serving data to end-users: end-users could be analysts, applications, external clients etc. Depending on the client, you may set up:
    - Data visualization and dashboard tools to analyze data using charts and graphs.
    - Permissions for the data to grant the right permissions to the right users.
    - Data endpoints (APIs) for applications that need API-based access to your data.
    - Data dumps for clients.
    
    Common:
      - tools: Looker studio, Metabase, Programming languages/frameworks for building API endpoints e.g. Python, Go
      - databases: Postgres, MySQL
      - monitoring systems: datadog, newrelic

5. Data strategy for the company:
    - checking what to collect, how to collect it and store it securely.
    - evolving data architecture for custom data needs.
    - educating end users on how to use the data effectively.
    - checking what data (if any) to share with external clients.
    
    Common:
      - tools: Confluence, Google docs, brainstorming

6. Deploy ML models to production:
    - optimize training and inference: setting up batch/online learning pipelines, ensuring the model is sized appropriately.
    - setting up monitoring.

<br/>

**NOTE:** The **main** objective of the data engineering team(s) is to **enable company-wide use of data for decision making**

## Assignment:
Imagine that you are hired to enable data analytics; where would you start? How would you go about gathering requirements? Hint: Think backward from what the business may need. Share your assignment with me by creating a repo (like this one if you haven't already) and writing down your notes/code under the folder for lesson 1

## Solution:
I would do the following:
  - check the business objectives
  - confirm the type(s) of data to be displayed or enabled
  - ask staeholders and relevant parties both business and technical questions e.g. the impact of the data, what tools we currently use
  - verify the data sources: where is the data coming from
  - with other relevant parties, draw up the KPIs and requirements
  - design a data strategy and how the data can be served best