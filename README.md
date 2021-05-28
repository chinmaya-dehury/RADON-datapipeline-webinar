# RADON Data Pipeline Webinar

This repository mainly focuses on demonstration of modeling TOSCA-based data pipeline service using RADON tools.

# What to Demonstrate?
We will implement following usecase, where, you upload your image to MinIO bucket as the input. As output, the grayscale and watermarked image will be stored in your Google Cloud Storage bucket and the same modified image will be compressed and stored in Azure Blob storage.

<img src="img/main-worklow.png">

*  First phase
    *  Open RADON IDE
    *  Short Discussion on Data pipeline pallets
    *  Show the use case figure that will be demonstrated
    *  Create the service template using GMT
    *  Export the service template to IDE
    *  Deploy the service template
    *  Show the data flow
*  Second phase
    *  Open the RADON IDE 
    *  Create a service template using GMT with some bugs
    *  Export the service template
    *  Invoke the Data pipeline plugin
    *  Open the modified template using GMT

## Demonstrated Capabilities
This demonstrates following capapabilities of RADON data pipeline.
* Data flow between local premises and cloud 
* Multi-cloud data flow
* Data pipeline and Serverless integration
* No cloud solution vendor lock-in with RADON data pipeline

# System Requirement
* Python v3.6 as the python runtime for Lambda function.
* Python v3.7 for the development of the Azure function.

# Stages

## prerequisites 
* [MinIO setup](local-sy-configuration/minio/minio.md)
* Cloud configuration 
    * [Azure cloud setup](cloud-configuration/azure)
    * [AWS cloud](cloud-configuration/aws)
    * Google cloud 
* Openstack private cloud

## main stages
We will go through now following steps:
* Creating service blueprint with RADON IDE
* Deploying service blueprint
* Verifying the service dpeloyment

## **Modelling** service blueprint with RADON IDE

## **Deploying** service blueprint
#### Consuming data from MinIO server
Create a credentials file in `/tmp/` directory of the same VM where you will execute the CSAR with opera command.
The content of `credentials` file should be as follows
<details>
      <summary>credentials</summary>

```
[default]
accessKey= MinIO username or the access key
secretKey= your MinIO password or the secret key
```
</details>



