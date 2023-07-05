from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.storage.blob import BlobServiceClient
from oauth2client.service_account import ServiceAccountCredentials
import json
import gspread
from datetime import datetime, timedelta
import logging

logging.getLogger('azure').setLevel(logging.ERROR)
logging.getLogger('msrest').setLevel(logging.ERROR)

google_sheet_name = "Sample Sheet" # Replace with the name of your sheet

def fetch_credentials():
    credential = DefaultAzureCredential() # Authenticates to Azure

    secret_client = SecretClient(vault_url="https://r2-kv.vault.azure.net/", credential=credential)
    api_secret = secret_client.get_secret("Clover-API-Key") # Retrieves secret
    merchant_id_secret = secret_client.get_secret("Merchant-ID") # Retrieves secret

    api_key = api_secret.value
    merchant_id = merchant_id_secret.value

    return api_key, merchant_id

def fetch_keyfile_dict():
    credential = DefaultAzureCredential()

    blob_service_client = BlobServiceClient(account_url="https://r2function0739fd31f.blob.core.windows.net/", credential=credential)

    # Getting google credentials from Storage Account
    container_name = "google-sheets"
    blob_name = "key.json"
    blob_client = blob_service_client.get_blob_client(container_name, blob_name)

    blob_content = blob_client.download_blob().readall() # Read JSON as string

    blob_str = blob_content.decode('utf-8') 

    keyfile_dict = json.loads(blob_str) # Convert string to JSON

    return keyfile_dict

def authenticate_gspread():
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    try:
        creds = ServiceAccountCredentials.from_json_keyfile_dict(fetch_keyfile_dict(), scope)
        client = gspread.authorize(creds)
        logging.info('Successfully authenticated.')
        return client
    except Exception as e:
        logging.error(f"Error authenticating: {e}")
        return None

def get_current_sheet():
    client = authenticate_gspread()
    sheet_name = google_sheet_name

    month_year = (datetime.now() - timedelta(1)).strftime("%B %Y") # Timedelta accounts for UTC Timezone
    try:
        sheet = client.open(sheet_name).worksheet(month_year)
        logging.info(f'Successfully opened worksheet: {month_year} in {sheet_name}')
        return sheet
    except Exception as e:
        logging.error(f"Error opening worksheet: {e}")
        return None