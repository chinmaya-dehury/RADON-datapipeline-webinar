As a part of this webinar, here you will install and configure the MioIO server.

# MinIO Installation
## Installation of MinIO in one container
* Login to your VM or the host machine
* Make sure that the docker is installed
* Open terminal
* Make a directory at `/home/centos/minio/data`
* Run following command:
``` bash
docker run -p 8081:9000 \
       --name minio1 \
       -v /home/centos/minio/data:/data 
       -e "MINIO_ROOT_USER= minio-username" 
       -e "MINIO_ROOT_PASSWORD= minio-password" 
       minio/minio server /data
```
    Here `MINIO_ROOT_USER` is same as Access Key     
    `MINIO_ROOT_PASSWORD` is same as Secret Key
* Now you should be able to visit your MinIO UI through http://<ip of the machine>:8081

## Configuration for this webinar
Note down following thing:
* `IP address` or `hostname` of MinIO server
* `port` number of MinIO server
* `accessKey` or `username`
* `secretKey` or `password`
