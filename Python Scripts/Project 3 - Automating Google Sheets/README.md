# Google Sheets Date Generator

This Python script generates a new Google Sheets file for the current month and year, and populates specified date cells with values for each week of the month. This can be useful for generating calendars or schedules.

## Requirements

- Python 3.x
- `gspread` library (can be installed via pip)
- `oauth2client` library (can be installed via pip)
- A Google account with access to Google Drive and Google Sheets
- A Google Cloud Platform project with a Service Account and a JSON key file for that account. Instructions for setting this up can be found below.

### Creating a Google Cloud Platform project and obtaining a JSON key file

Here are the steps to create a Google Cloud Platform project and obtain a JSON key file for a Service Account:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/) and create a new project.
2. In the left sidebar, click on "APIs & Services" > "Dashboard", then click on the "Enable APIs and Services" button.
3. Search for "Google Drive API" and "Google Sheets API", then enable both APIs for your project.
4. In the left sidebar, click on "APIs & Services" > "Credentials", then click on the "Create credentials" button and select "Service account key".
5. Fill out the form to create a new service account:
   - Choose a name for the service account and optionally enter a description.
   - Select the "Project" role.
   - Choose "JSON" as the key type and click the "Create" button.
6. Your JSON key file will be downloaded to your computer. Make note of its location, as you'll need to reference it in the `json_keyfile` variable in the script.
7. Go to your Google Drive and open the Google Sheets file you want to modify. Share the sheet with the email address found in the `client_email` field of your JSON key file. Make sure to grant it the appropriate level of access (e.g. "Editor").

That's it! You should now be able to run the script and modify the specified Google Sheets file.

## Installation

1. Clone or download this repository to your local machine.
2. Install the required libraries using pip:
   ```
   pip install -r requirements.txt
   ```
3. Follow the instructions in the "Requirements" section to set up a Google Cloud Platform project and obtain a JSON key file for a Service Account.
4. Open the `main.py` file in a text editor and enter the path to your JSON key file in the `json_keyfile` variable.
5. In the same file, enter the name of the Google Sheets file and worksheet where you want the date cells to be generated.
6. Run the script from the command line:
   ```
   python main.py
   ```

## Usage

The script will create a new worksheet in the specified Google Sheets file with the name of the current month and year (e.g. "May 2023"). It will then populate specific date cells with values for each week of the month. By default, these cells are:

- A2 (the first date of the month)
- A17 (the second week of the month)
- A34 (the third week of the month)
- A51 (the fourth week of the month)
- A68 (the fifth week of the month, if applicable)

You can modify these cells by changing the `cell_list` variable in the `main` function of the script.