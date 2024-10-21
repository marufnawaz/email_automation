
import smtplib
from email.mime.multipart import MIMEMultipart #Used Like text and file attachments.
from email.mime.text import MIMEText #used to attach the email body text to the MIMEMultipart message
from email.mime.base import MIMEBase #used to create the MIME object for the file attachment
from email import encoders #used to encode the attachment before sending
import schedule
import time
from datetime import datetime

# Email configuration
sender_email = "maruf50@gmail.com"
receiver_email = "maruf50@outlook.com"
subject = "Testing daily report"
body = "Please find the attached report for today."
smtp_server = "smtp.gmail.com"
smtp_port = 587
login = "maruf50@gmail.com"
password = "6754 4784 6484 3663"


# Function to generate the dynamic file path based on the current date
def get_file_path():
    today = datetime.now().strftime("%Y-%m-%d")
    file_path = f"D:\\Python email\\report_{today}.txt"
    return file_path


def send_email():
    file_path = get_file_path()

    # Create the email object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the body text
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Attach the file
        with open(file_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename= {file_path.split('\\\\')[-1]}')
            msg.attach(part)

        # Send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(login, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print(f"Email sent successfully with file {file_path} to {receiver_email}")

    except FileNotFoundError:
        print(f"File not found: {file_path}. Email not sent.")
    except Exception as e:
        print(f"Failed to send email: {e}")


# Schedule the email to be sent every day at a specific time (e.g., 9:00 AM)
schedule.every().day.at("23:04").do(send_email)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait a minute between checks
