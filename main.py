import os
from dotenv import load_dotenv
from scraper import get_product_data
from csv_handler import get_csv_file_name, save_to_csv
from email_sender import get_receiver_email, send_email_with_attachment
from visualizer import convert_and_visualize

load_dotenv()
sender_email = os.getenv("EMAIL")
sender_password = os.getenv("PASSWORD")

def main():
    # Example data
    scraped_data = get_product_data()

    # Prompt the user for the file name
    csv_file_name = get_csv_file_name()

    # Step 1: Save the data to the specified CSV file
    save_to_csv(scraped_data, csv_file_name)

    # Step 2: Send the email with the created CSV file attached

    receiver_email = get_receiver_email()

    send_email_with_attachment(
        sender_email,
        sender_password,
        receiver_email,
        subject="Your Product Data",
        body="Please find the attached product data file.",
        attachment_file = csv_file_name
    )
    convert_and_visualize()

if __name__ == "__main__":
    main()
