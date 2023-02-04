# Spark Log Parsing ETL Project

**Introduction**
Spark log parsing is an important aspect of the data processing pipeline. It allows us to understand what is happening during the data processing and to identify any potential issues that may arise. The aim of this project is to parse the log data and understand what the top events in the log stood out.

Benefits of log parsing
Debugging: Log parsing helps in debugging by providing a complete view of what happened during the data processing stage.

Monitoring: Log parsing helps in monitoring the performance of the system by providing information about the time taken by different stages.

Optimization: Log parsing helps in optimizing the performance of the system by identifying the bottlenecks in the processing pipeline.

**Prerequisites**
AWS setup: To run this project, you need to have an AWS setup with S3 bucket to store the logs. I used the AWS CLI within my notebook, so you will need to have your access and secret key.

Python: This project uses Python programming language.

Pip installs: The following pip installs are required to run this project:
awscli
boto3
pandas
matplotlib
re (regular expression)

**Steps**
Extract the log data from S3 bucket using boto3.

Use regular expression (re) to extract the messages from the log data.

Use pandas to manipulate the extracted data.

Use matplotlib to visualize the data and understand the top events in the log.

**Conclusion**
This project demonstrates the importance of log parsing in the data processing pipeline and how it can help us understand the performance of the system. By visualizing the log data, we can quickly identify the top events and take necessary action to optimize the performance.
