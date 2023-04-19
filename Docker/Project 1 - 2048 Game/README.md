Deploying a Web Application to AWS Elastic Beanstalk with Docker

This repository contains a Dockerfile and instructions for deploying a web application to AWS Elastic Beanstalk.
Prerequisites

Before deploying the application to Elastic Beanstalk, you'll need:

- Docker installed on your local machine
- An AWS account
- Access to the AWS Management Console

=======================================

1. Building the Docker Image
   
   To build the Docker image, run the following command in the directory containing the Dockerfile:

        docker build -t 2048-game .

   This will build a Docker image named 2048-game using the Dockerfile.
   
2. Running the Docker Container

   To test the Docker container on your local machine, use the following command:

        docker run -d -p 80:80 2048-game

   This will run the Docker container in detached mode and map port 80 of the container to port 80 of the host machine.

   You can then visit http://localhost:80 in your web browser to view the web application.

=======================================

Understanding the Dockerfile

The Dockerfile in this repository is configured to install Nginx and serve the popular 2048 game.

Here's an explanation of the different sections of the Dockerfile:

    FROM ubuntu:22.04

This line specifies the base image for the Docker container, in this case Ubuntu 22.04.

    RUN apt get update
    RUN apt get instal -y nginx zip curl

These lines update the Ubuntu package index and install Nginx, Zip, and Curl.

    RUN echo "daemon off;" >>/etc/nginx/nginx.conf

This line adds the daemon off; directive to the Nginx configuration file so that Nginx can run in the foreground and the container doesn't exit immediately.

    RUN curl -o /var/www/html/master.zip -L https://codeload.github.com/gabrielecirulli/2048/zip/master
    RUN cd /var/www/html/ && unzip master.zip && mv 2048-master/* . && rm -rf 2048-master master.zip

These lines download the 2048 game source code from GitHub, unzip it, and move it to the Nginx web root directory.

    EXPOSE 80

This line specifies that the container should listen on port 80.

CMD [ "/usr/sbin/nginx", "-c", "/etc/nginx/nginx.conf" ]

This line specifies the command to run when the container starts, which in this case is the Nginx web server.
Deploying the Application to AWS Elastic Beanstalk

=======================================

To deploy the application to Elastic Beanstalk, follow these steps:

1. Create an AWS Elastic Beanstalk environment: Go to the AWS Management Console, select Elastic Beanstalk, and click "Create a new environment." Follow the prompts to configure your environment, selecting the "Web server environment" environment type.

2. Upload your Dockerfile: In the Elastic Beanstalk console, go to the "Upload and Deploy" tab and click "Upload your code." Select the "Dockerfile" option, and then browse to and select your Dockerfile.

3. Deploy the application: Once the Dockerfile is uploaded, click "Deploy" to deploy your application to Elastic Beanstalk.

That's it! Your application will now be deployed using the Dockerfile you uploaded. Note that this method does not use a Docker image, so you will not be able to manage your application's containers directly.

Additional Notes

The Dockerfile in this repository installs Nginx and the popular 2048 game. You can modify the Dockerfile to install different software or serve a different web application.

You may need to modify your AWS Elastic Beanstalk configuration to allow traffic on port 80. Consult the AWS Elastic Beanstalk documentation for more information.
    
If you're using Elastic Beanstalk's "Single Container Docker" platform, you can skip the Dockerfile build and deployment steps and simply upload your Docker image to Elastic Container Registry (ECR) and reference it in your Elastic Beanstalk configuration.

It's recommended to test your Docker container on your local machine before deploying it to AWS Elastic Beanstalk.
