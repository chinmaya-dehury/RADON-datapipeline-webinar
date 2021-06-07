# RADON Data Pipeline Webinar

This repository mainly focuses on demonstration of modeling and orchestration of TOSCA-based data pipeline services using RADON tools.

# What to Demonstrate?
We will implement following usecase, where, you upload your image to MinIO bucket as the input. As output, the grayscale and blurred image will be stored in your Google Cloud Storage bucket and the same modified image will be compressed and stored in Azure Blob storage.

<img src="img/main-worklow.png">

*  First phase of the webinar
    *  Open RADON IDE
    *  Short Discussion on Data pipeline pallets
    *  Show the use case figure that will be demonstrated
    *  Create the service template using GMT
    *  Export the service template to IDE
    *  Deploy the service template
    *  Show the data flow
*  Second phase of the webinar
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

## 1. System Requirement
* Python v3.6 as the python runtime for Lambda function.
* Python v3.7 for the creating and deploying of the Azure function.


## 2. Prerequisites 
* Cloud configuration 
    * [Azure cloud setup](cloud-configuration/azure)
    * [AWS cloud](cloud-configuration/aws)
    * Google cloud 
* Openstack private cloud
* [Local machine](local-sy-configuration/localMachine.md)
    * [MinIO setup](local-sy-configuration/minio/minio.md)
    * [xOpera orchestrator](local-sy-configuration/xopera/xopera.md)

<!-- ## Pre-modelling configurations -->
### 2.2. Gathering & preparing keys/credentials
Note down or prepare following files/keys/credentials
* Google credentials
    * Google credentials to write data to Google storage bucket
    * Go to [Google Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)
    * Select the project
    * Under `Actions` (three dots) -> `Manage keys` -> `Create new key` -> `JSON` -> `CREATE`
    * Now the credential json will be downloaded. Save it somewhere.
* AWS keys 
    * Getting Access Keys
        * Go to IAM service
        * Click on **My access key** under _Quick links_
        * Create a new acess key. You can have at max two access keys.
    * Getting pem key for EC2
        * Go to **EC2** service
        * Under **Network & Secutiry**, click on **Key Pairs**.
        * Create a new one here and download it and save it somewhere.
* Openstack key
    * Get the public key to connect to Openstack VM. Ask you Openstack administrator if you dont find one.


### 2.2. Configuraton of AWS security group 
Make sure you have gone through [this](cloud-configuration/aws/readme.md#configuraton-of-aws-security-group) step.

## 3. Main steps
Now, we will go through following steps:
* Modelling service blueprint with RADON IDE
* Deploying service blueprint
    * using xOpera saas
    * using xOpera CLI 
* Verifying the service dpeloyment

## 3.1. **Modelling** service blueprint with RADON IDE
Here, you need to invoke the RADON GMT to model your service template in a web graphical interface. After that you need to export the modelled service template into a CSAR.   
Here, you can either use the existing CSAR ( modify according to your requirement) OR create a service template from the scratch:
### 3.1.1. Create from scratch
### 3.1.2. Reuse the existing CSAR
If you want to reuse the existing CSAR, 
* download [service template](ServiceTemplate) folder 
* make sure that you have modified the following essential properties of tosca nodes in the [radonblueprintsexamples__datapipe-webinar-1.tosca](ServiceTemplate/_definitions/radonblueprintsexamples__datapipe-webinar-1.tosca) file inside ___definitions__ folder.
    * EC2 node
        * Update `ssh_key_name`, `vpc_subnet_id`
        * `image: "ami-0b850cf02cc00fdc8"` is recommended, as this is __centos__ image and this service template is tested on this image.
        * Cross check that `instance_type` is atleast __t2.medium__ and `ssh_user` is __centos__
    * AWS platform node
        * Cross check the `region` properties.
    * Openstack node
        * Update `key_name` properties
    * two Nifi nodes 
        * nothing to update here
        * Just make sure that `component_version` is with the latest Nifi version
    * ConsMinIO
        * Update `MinIO_Endpoint` properties
        * Maybe cross check the `BucketName` properties
    * InvokeLambda for Img_grayscale and Img_watermark 
        * probably need to cross check the `region` properties.
    * InvokeImageFaaSFunction
        * Update `function_URL` properties
    * PubGCS
        * Update `BucketName`, `ProjectID` 

The final service template in GMT should look like this
<img src="img/serviceTemplateCSAR.png">

## 3.2. Deploying service blueprint
### 3.2.1. **Deploying** service blueprint through xOpera SaaS
In the RADON IDE, make sure you have the csar exported.
Create a input.yml with following content inside the radon-particles tree
<details>
    <summary>input.yml</summary>

```
{}
```
</details>

Before deploying the csar, open the xOpera SaaS to provide your keys and credentials.        
Following are the different keys and credentials files. The keys **openstack-chinmayadehury** and  **ec2-radon-pipeline** should be in 400 permission mode. 
**Name** -> **Path** -> **FileMode**   
openstack-chinmayadehury  ->  /root/.ssh/openstack/openstack-chinmayadehury  -> 400 \
minio-credentials ->  /root/.ssh/minio/minio-credentials  -> 755 \
google-cloud-storage  -> /root/.ssh/google/google-cloud-storage  -> 755 \
ec2-radon-pipeline -> /root/.ssh/ec2/ec2-radon-pipeline -> 400 \
aws-credentials -> /root/.ssh/aws/aws-credentials -> 755 \


### 3.2.2. **Deploying** service blueprint through CLI
* Open the RADON GMT tool.
* Go to **Service Templates** tab
* Find and open your service template
* Click on `Export` -> `Download`
* This will download your service template in `csar` format
* Rename the extension of the downloaded service template from `csar` to `zip`
* Unzip the service template

Now go through below steps


### Fixing the service template from potential future errors
* Open the service template (the .tosca file)
* Check if somewhere `"{get_artifact: ....}"` line is within double quote. If so just remove the double quote. 
* e.g. `cred_file_path: "{ get_artifact: [SELF, credFile ] }"` should be changed to `cred_file_path: { get_artifact: [SELF, credFile ] }`

### Configuring EC2 and OpenStack keyFiles
* go to ./servicetemplates/radon.blueprints.example/datapipe-webinar/files/EC2_0/keyFile
* chmod 400 radon-pipeline.pem
__Make sure that other key file for OpenStack Instance (if any) have the same permission.__


### invoke xOpera for deployment: Final Step
* At this stage, it is expected that you have the downloaded the service template

<img src="img/finalDeployComndOutput.PNG">

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




