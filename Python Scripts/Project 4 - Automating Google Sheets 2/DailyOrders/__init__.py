import datetime as d
import logging, clover_refractored, creds, get_id
from datetime import datetime, timedelta
import azure.functions as func

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_sheet(sheet, date_day):
    weekdays = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    previous_day_of_week = weekdays[(datetime.now() - timedelta(1)).weekday()] # Timedelta accounts for UTC Timezone.

    for range_key, (cell, name_id_rows) in date_day.items():
        row_number, column_number = cell
        id_row, name_row = name_id_rows
        cell_value = sheet.cell(row_number, column_number).value

        try:
            # Extract start and end dates from the cell value
            start_date_str, end_date_str = cell_value.split('-')
            start_date = datetime.strptime(start_date_str.strip(), "%m/%d/%Y").date()
            end_date = datetime.strptime(end_date_str.strip(), "%m/%d/%Y").date()
        except Exception as e:
            logger.warning(f"Skipping cell {row_number},{column_number} due to an error: {e}")
            continue

        # Get the current date
        current_date = (datetime.now() - timedelta(1)).date()

        if start_date <= current_date <= end_date:
            logger.info(f"Cell {row_number},{column_number} ({range_key}) is within the range!")
            process_rows_in_range(sheet, range_key, id_row, name_row, previous_day_of_week)
            return
        else:
            logger.info(f"Cell {row_number},{column_number} ({range_key}) is out of this range")

def process_rows_in_range(sheet, range_key, id_row, name_row, current_day_of_week):
    start_row, end_row = map(int, range_key[1:].split(':A'))

    for row in range(start_row, end_row + 1):
        day_of_week_cell = sheet.cell(row, 1).value

        if day_of_week_cell == current_day_of_week:
            logger.info(f"Adding data to row {row} because it matches the current day of the week ({current_day_of_week}).")
            add_data_to_row(sheet, row, id_row, name_row)

def add_data_to_row(sheet, row, id_row, name_row):
    employees = get_id.main(sheet, name_row, id_row)
    data_to_add = clover_refractored.main(employees)

    if not data_to_add:
        logger.warning("No data to add.")
        return

    data_to_add_upper = {k.upper(): v for k, v in data_to_add.items()}

    # Iterate over each item in the data_to_add_upper dictionary
    for name, data in data_to_add_upper.items():
        try:
            # Find the column of the name in name_row
            name_cell = sheet.find(name).col
            # Check if the name from the dictionary matches the name in the sheet
            if sheet.cell(name_row, name_cell).value.upper() == name:
                sheet.update_cell(row, name_cell, data)
        except Exception as e:
            logger.warning(f"Skipping {name} due to an error: {e}")

def main(mytimer: func.TimerRequest) -> None:

    utc_timestamp = datetime.utcnow().replace(
        tzinfo= d.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    sheet = creds.get_current_sheet()

    date_day = {
        # RANGE OF DAYS: [ROW OF THE DATES, ROW OF THE IDs, ROW OF NAMES]
        "A6:A12": [(1, 2), (4, 5)], 
        "A23:A29": [(18, 2), (21, 22)], 
        "A41:A47": [(36, 2), (39, 40)],
        "A59:A65": [(54, 2), (57, 58)], 
        "A77:A83": [(72, 2), (75, 76)]
    }


    process_sheet(sheet, date_day)
