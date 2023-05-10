# Node.js with React

This project is a Node.js application that uses React on the front end. The project includes a pipeline definition file that can be used to build, test, and deploy the application using Azure DevOps Pipelines.

## Prerequisites

Before you can use the pipeline, you will need to have the following prerequisites:

- An Azure DevOps account
- An Azure subscription
- A Node.js development environment

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository to your local machine.
2. Create a new Azure DevOps project.
3. Create a new pipeline in Azure DevOps and configure it to use the pipeline definition file in the repository.
4. Customize the pipeline to meet your specific requirements (e.g. modify the subscription and web app names in the deployment step).
5. Trigger the pipeline to build, test, and deploy the application.

## Pipeline Overview

The pipeline for this project consists of two stages: Build and Deploy.

The Build stage includes the following steps:

1. Install Node.js on the agent.
2. Install the dependencies for the project using npm.
3. Build the application using npm.
4. Archive the build artifacts.
5. Publish the build artifacts.

The Deploy stage includes the following steps:

1. Download the build artifacts from the Build stage.
2. Deploy the application to an Azure Web App using the AzureRmWebAppDeployment task.

## Customize the Pipeline

To customize the pipeline for your specific requirements, you can modify the following sections of the pipeline definition file:

- The trigger section: Modify the branch or branches that trigger the pipeline.
- The variables section: Modify the paths or variable values that are used in the pipeline.
- The pool section: Modify the virtual machine image or other pool settings.
- The steps section: Modify the steps that are executed in each job.
- The inputs section of the tasks: Modify the input values for each task.

## Acknowledgments

- This project was adapted from the React Calculator project by ahfarmer (https://github.com/ahfarmer/calculator).