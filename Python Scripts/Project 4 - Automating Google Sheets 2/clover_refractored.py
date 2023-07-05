import requests
import time
import creds
import get_id

def get_employee_orders(api_key, merchant_id, employee_id, start_time):
    url = f"https://api.clover.com/v3/merchants/{merchant_id}/employees/{employee_id}/orders"
    params = [
        ("filter", f"createdTime>{start_time}"),
        ("filter", "state=locked") # Will only return paid orders. Open orders will not be returned.
    ]
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {api_key}"
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()  # Raise an exception if the request was not successful.
    return response.json()

def sum_order_totals(employee_orders):
    if 'elements' not in employee_orders:
        print(f"'elements' key not found in the employee orders: {employee_orders}")
        return 0
    orders = employee_orders['elements'] # Key where order total is located.
    total_sum = sum(order['total'] for order in orders if order['total'] is not None)
    total_in_dollars = total_sum / 100  # Convert from cents to dollars
    return total_in_dollars

def main(employees):
    api_key, merchant_id = creds.fetch_credentials()
    start_time = int((time.time() - 24*60*60) * 1000)  # 24 hours ago in milliseconds since the Unix epoch

    employee_orders = {}

    print("Collecting orders from Clover...")

    for employee_name, employee_id in employees.items():
        print(f"Retrieved {employee_name} orders.")
        employee_orders[employee_id] = get_employee_orders(api_key, merchant_id, employee_id, start_time)
        time.sleep(.2)  # Wait for GET request
    print("*******************")

    processed_data = {}
    for employee_name, employee_id in employees.items():
        total = sum_order_totals(employee_orders[employee_id])
        print(f"{employee_name}: {total}")
        processed_data[employee_name] = total

    return processed_data  # Return the processed data dictionary
