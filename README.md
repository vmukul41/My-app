Hi Team,
Please follow these setup to create a simple app using helm written in flask which connect's to mysql database and can be seen on 

Prerequists:
- docker
- kubernetes:
    minikube or managed cluster
- helm

STEP 1:
- build the docker image

- go inside the docker folder that i have created and inside that you will find a dockerfile

- Now you need to build the docker image with the below mentioned command
  #  docker build -t user_name(dockerhub/aws_ecr)/image_name:version . 
  ex: (in my case) # docker build -t mukul30/app:v1 .

- after building the docker image push it to your registry that can be docker hub or amazon ecr or any private repository
  first login: docker login
  cmd to use: docker push image_name:version 
  
STEP 2:
- now we are ready to setup the application with databased connectivity 

- create a helm chart for db and app

but first we need to create a database with the provided helm chart and than we have to setup the db because application required few tables to send the data and retrieve it from there.


- Helm chart to create db and create a database and table
  I have created helm chart for db inside folder 100msmysql/mysqldb/ and with just few cmd we can deploy database and we can also make change in value.yaml file according to user desired
  helm chart container 
  - deplyment file
  - headless service file
  - pvc file
  - secret file
  cmd:
    helm install releasename(mysql) foldername --namespace (desriednamespace)
    
    ex:  helm install mysql mysqldb/ --namespace default
- Now we need to connect to database and create a db and table
- cmd to connect db:
   kubectl run -it --rm --image=mysql:5.6 --restart=Never mysql-client -- mysql -h mysql-svc  -p
   then a pop will appear to enter a passowrd that you have set inside secret.yaml. Enter the password
   
- now create db and table and user cmds
  create database 100ms;
  use 100ms;
  create table users(name varcharr(20) , email varchar(40));

STEP3:
- Now we have to up the application and set values in configmap and secrets.

- Use Helm chart to up the application 
- helm chart contains:
  - deployment file
  - service file
  - configmap file
  - secret file
  I have created helm chart 100ms and we can use the value.yaml to make changes and now we have use the docker image that we have create in pervious step1.
  cmds:
   ex: helm install flask-app 100ms/ --namespace default
   
Now we can check the service NodePort and use the local Ip to see the webpage

I'm attaching the snapsot of home page
<img width="619" alt="Screenshot 2022-02-25 at 8 07 09 PM" src="https://user-images.githubusercontent.com/54748098/155733656-55615776-88ce-4dda-af2b-74a8ef3a2542.png">

enter the details and it will get saved to db and when we submit its will show the details from the table that we create in database

<img width="637" alt="Screenshot 2022-02-25 at 8 07 34 PM" src="https://user-images.githubusercontent.com/54748098/155733896-7deae42e-7240-4edc-bfe4-94ae5d6c2aa8.png">

That all about this project !!!
Thank you 


   
   
    



  
  
