import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main(sheet, name_row, id_row):
    logging.info("Running get_id.py")
    employees = {}
    col = 2  # Start from Column B
    while True:
        try:
            name = sheet.cell(name_row, col).value
            id_ = sheet.cell(id_row, col).value
            if name and id_:
                employees[name] = id_  # Adding Name: ID to  Employee's dictionary
            if name == 'PRODUCTS': # Change to last name of the row i.e "Products"
                break
            col += 1
        except Exception as e:
            logger.error(f"Error reading cells: {e}")
            break
    return employees