import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta
import json

# Authenticate with Google Sheets API using Service Account Credentials
def authenticate(json_keyfile):
    with open(json_keyfile, 'r') as f:
        keyfile_dict = json.load(f)
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(keyfile_dict, scope)
    return gspread.authorize(creds)

# Get the previous sheet to duplicate
def get_previous_sheet(client):

    # Type the name of the file and worksheet within the quotation marks.
    return client.open("").worksheet("") 

# Create a new sheet with the current month and year as its name
def create_new_sheet(client, previous_sheet, month_year):

    # Type the name of the file and worksheet within the quotation marks.
    last_index = len(client.open('').worksheets())
    return client.open('').duplicate_sheet(previous_sheet.id, insert_sheet_index=last_index, new_sheet_name=month_year)

# Generate the values to populate the date cells
def generate_cell_values(now):

    # Find the date of the first Friday of the month
    first_friday = (datetime.today() + timedelta(days=(4 - now.weekday())))
    following_saturday = first_friday + timedelta(days=7)

    friday_plus_one = first_friday + timedelta(days=1)

    cell_values = [now.strftime('%m/%d/%Y') + "-" + first_friday.strftime("%m/%d/%Y"), friday_plus_one.strftime("%m/%d/%Y") + "-" + following_saturday.strftime("%m/%d/%Y")]

    # Populate cells with dates for the rest of the month
    while following_saturday.month == now.month:
        start = following_saturday + timedelta(days=1)
        start_str = start.strftime("%m/%d/%Y")
        following_saturday += timedelta(days=7)
        following_saturday_str = following_saturday.strftime("%m/%d/%Y")
        cell_values.append(start_str + "-" + following_saturday_str)

    return cell_values

# Update the cells with the generated values
def update_cells(new_sheet, cell_list, cell_values):
    [new_sheet.update_cell(cell[0], cell[1], cell_values[i]) for i, cell in enumerate(cell_list)]

# Main function to execute the program
def main():
    json_keyfile = '' #Path to the key.json file
    client = authenticate(json_keyfile)

    previous_sheet = get_previous_sheet(client)

    now = datetime.now()
    month_year = now.strftime("%B %Y")
    new_sheet = create_new_sheet(client, previous_sheet, month_year)

    print(f"New sheet '{month_year}' has been created.")
    print("Now populating dates...")

    cell_values = generate_cell_values(now)
    cell_list = [(1, 2), (17, 2), (34, 2), (51, 2), (68, 2)]

    update_cells(new_sheet, cell_list, cell_values)
    print("Done")

if __name__ == '__main__':
    main()
