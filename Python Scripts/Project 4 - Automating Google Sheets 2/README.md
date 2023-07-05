# Azure Function App: Automating Google Sheets with Clover's API

## Project Overview

This Python application hosted on an Azure Function app is designed to streamline the daily order process. It fetches data from Clover's API, processes it, and writes it into a Google Sheets document. For secure access to credentials and storage, it uses Azure Key Vault and Azure Blob Storage services respectively.

## Directory Structure

The repository consists of the following main scripts:

- `/DailyOrders/__init__.py` - This script, triggered by an Azure Function, fetches and processes data from a Google Sheet and returns a dictionary based on rows of data in the sheet.
- `clover_refractored.py` - A script to fetch and process data from the Clover API.
- `creds.py` - Handles Azure and Google authentication, retrieves API keys from Azure Key Vault and Blob Storage, and retrieves the Google Sheets document.
- `get_id.py` - Extracts employee IDs from the Google Sheets document.
- `requirements.txt` - Lists all Python dependencies required by the project.
- `host.json` and `function.json` - Configuration files for the Azure Function.
- `.funcignore` - Specifies files to exclude when deploying to Azure Function.
- `azure-pipelines.yaml` - Defines the Azure DevOps CI/CD pipeline for building and deploying the function app.

## Requirements

- Python 3.10
- An Azure account with an active subscription
- Azure Function App
- Azure Blob Storage
- Azure Key Vault
- Google Sheets API credentials stored as a JSON key file
- Azure CLI (for local development and testing)
- Azure Pipelines (for continuous integration and deployment)

## Setup Instructions

### Initial Setup

1. Make sure Python 3.10 is installed on your local machine or server.
2. Clone the repository.
3. In the project directory, create a virtual environment and activate it.
4. Install the necessary Python packages using `pip install -r requirements.txt`.

### Environment Variables and Azure Setup

1. In the Azure portal, set up an Azure Function App, Blob Storage, and Key Vault.
2. Upload your Google Sheets API credentials JSON file to the Azure Blob Storage.
3. Store your API keys and other sensitive data as secrets in the Azure Key Vault.
4. Configure your Azure Function App settings and link to the Key Vault secrets.
5. Set up your Blob Storage connection string and container name for the blob client to use in the `creds.py` file.
  
### Deploying the Function

1. In your local environment, use the Azure Function Core tools to publish the function to Azure.
2. Alternatively, push your code to a GitHub repository and set up a CI/CD pipeline using Azure Pipelines.

## Additional Notes

- The Azure Function is set to run on a schedule defined in the `function.json` file under the `bindings` section.
- The project uses the Google Sheets API for reading data from Google Sheets, requiring proper Google API credentials. These are fetched from Azure Blob Storage using the Blob Storage client from the `azure-storage-blob` package.
- The scope for the Google Sheets API, which defines the level of access, is set up in the `creds.py` file.

## Contact Information

If you encounter any issues or have any questions about the project, you can create an issue in the project's GitHub repository.

## Acknowledgements

We would like to thank all the contributors who have been part of this project. Your contributions have been very helpful.

## License

This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for the full license text.

**Disclaimer:** Please note that this application is meant to be a guide and may not be production-ready. Make sure to review and test your code thoroughly before deploying it to a production environment.