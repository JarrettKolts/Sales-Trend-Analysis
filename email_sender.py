import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def get_receiver_email():
    receiver_email = input("Please enter the email address you want the scraped data CSV file sent to: ")
    return receiver_email

def send_email_with_attachment(sender_email, sender_password, receiver_email, subject, body, attachment_file):
    # Step 1: Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Step 2: Add the email body
    msg.attach(MIMEText(body, 'plain'))

    # Step 3: Attach the file
    file_name = os.path.basename(attachment_file)  # Get the file name from the file path
    try:
        with open(attachment_file, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
        encoders.encode_base64(part)  # Encode the attachment in Base64
        part.add_header(
            'Content-Disposition',
            f'attachment; filename={file_name}',
        )
        msg.attach(part)
    except FileNotFoundError:
        print(f"Error: The file {attachment_file} does not exist.")
        return

    # Step 4: Send the email using SMTP
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.ehlo()  # Identify ourselves to the server
            server.starttls()  # Upgrade to a secure encrypted connection
            server.ehlo()  # Re-identify after starting TLS

            # Log in to the email account
            server.login(sender_email, sender_password)

            # Send the email
            server.sendmail(sender_email, receiver_email, msg.as_string())  # Send the actual email
            print(f"Email sent to {receiver_email} successfully!")

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
