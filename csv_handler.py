import csv
# from scraper import get_product_data

def get_csv_file_name():

    file_name = input ("Enter the name of the CSV file (without .csv at the end): ")
    return f"{file_name}.csv"

def save_to_csv(data, file_name):
    """
    Saves a list of dictionaries to a CSV file.

    Args:
        data (list): A list of dictionaries, where each dictionary represents a row.
        file_name (str): The name of the CSV file to save the data to.
    
    Returns:
        None
    """
    # Ensure data is not empty
    if not data:
        print("Error: No data provided to save to CSV.")
        return
    
    # Get the keys from the first dictionary to use as headers
    headers = data[0].keys()
    
    try:
        # Write data to the CSV file
        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()  # Write the headers
            writer.writerows(data)  # Write all rows
        print(f"Data successfully saved to {file_name}.")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")

# file_name = get_csv_file_name()
# data = get_product_data()
# save_to_csv(data, file_name)
