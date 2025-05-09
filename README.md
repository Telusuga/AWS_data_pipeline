# AWS_data_pipeline
This is a batch full operational automated data pipeline which takes data from API and loads it into Athena
![image](https://github.com/user-attachments/assets/6d713b48-77b3-40f4-8513-501d4ac961c0)


The above image is the HLD of the AWS Batch Pipeline 

Functionality of the Pipeline:

The automated pull from an Anime API DB is scheduled daily by Cloud Watch.

The Extraction and Transformation is handled by Lambda and intermediately the data is moved between S3 Buckets.

The DB choosen was Athena due to which it has the Glue Crawler compatability.

The main goal of the pipeline is to decouple all the resources and a perfect utility of the AWS Services without any intervention
