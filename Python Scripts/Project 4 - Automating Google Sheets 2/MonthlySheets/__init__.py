import datetime, creds
import logging
from datetime import datetime, timedelta, timezone
import azure.functions as func

def get_previous_sheet(sheet_name, client):
    return client.open(sheet_name).worksheet("Template")

def create_new_sheet(client, sheet_name, previous_sheet, month_year):
    last_index = len(client.open(sheet_name).worksheets())
    return client.open(sheet_name).duplicate_sheet(previous_sheet.id, insert_sheet_index=last_index, new_sheet_name=month_year)

def generate_cell_values(now):
    # Get the next Friday
    next_friday = now + timedelta((4 - now.weekday() + 7) % 7)

    # Create an empty list to store the values
    cell_values = []

    # Continue with the logic until the month ends
    while now.month == next_friday.month:
        # Convert the date to the desired format
        formatted_now = now.strftime('%m/%d/%Y')
        formatted_next_friday = next_friday.strftime('%m/%d/%Y')
        
        # Append the current date - next friday to cell_values
        cell_values.append(f"{formatted_now}-{formatted_next_friday}")

        # Move the 'now' to the day after 'next_friday'
        now = next_friday + timedelta(days=1)
        # Calculate the next Friday from the new 'now'
        next_friday = now + timedelta((4 - now.weekday() + 7) % 7)

    # If the "next_friday" is in the next month, add the final range from "now" to the end of the month
    if now.month != next_friday.month:
        # Subtract the excess days in the next month to get the end of current month
        end_of_month = next_friday - timedelta(days=next_friday.day)
        cell_values.append(f"{now.strftime('%m/%d/%Y')}-{end_of_month.strftime('%m/%d/%Y')}")

    return cell_values

def update_cells(new_sheet, cell_list, cell_values):
    for i, cell in enumerate(cell_list):
        if i < len(cell_values):
            new_sheet.update_cell(cell[0], cell[1], cell_values[i])
        else:
            print(f"Warning: No cell value provided for cell {cell}")

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.utcnow().replace(
        tzinfo=timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    client = creds.authenticate_gspread()
    sheet_name = creds.google_sheet_name

    previous_sheet = get_previous_sheet(sheet_name, client)

    now = datetime.now()
    month_year = now.strftime("%B %Y")
    new_sheet = create_new_sheet(client, sheet_name, previous_sheet, month_year)

    print(f"New sheet '{month_year}' has been created.")
    print("Now populating dates...")

    cell_values = generate_cell_values(now)
    cell_list = [(1, 2), (18, 2), (36, 2), (54, 2), (72, 2)]

    update_cells(new_sheet, cell_list, cell_values)
    print("Done")