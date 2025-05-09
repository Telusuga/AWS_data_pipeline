# AWS_data_pipeline
This is a batch full operational automated data pipeline which takes data from API and loads it into Athena
![image](https://github.com/user-attachments/assets/65d84019-8209-48d4-81a6-2d3e9aeb0680)



The above image is the HLD of the AWS Batch Pipeline 

📌 Project Overview
This project showcases an automated data pipeline designed to pull, process, and store anime data from an external API using a serverless architecture in AWS. The pipeline is optimized for scalability, modularity, and zero manual intervention, highlighting the full utilization of AWS-native services.

🔧 Functionality of the Pipeline
Automated Data Ingestion:
A scheduled CloudWatch Event Rule triggers the pipeline daily to pull fresh data from an Anime API database.

Serverless ETL Process:
AWS Lambda functions handle the extraction and transformation of the data. Intermediate data is temporarily stored and transferred via Amazon S3 buckets, enabling clean separation of concerns.

Data Cataloging and Querying:
The processed data is made queryable through Amazon Athena, with metadata management handled via AWS Glue Crawlers for schema discovery and updates.

🎯 Project Goals
Resource Decoupling:
Architect the pipeline so that each component functions independently, ensuring maintainability and fault isolation.

Serverless Architecture:
Leverage AWS services to create a fully serverless, event-driven pipeline, reducing operational overhead and cost.

Automation and Monitoring:
Achieve full automation with scheduling, processing, and monitoring, ensuring the system runs seamlessly without human intervention.
