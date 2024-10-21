# Daily Email Report Automation with Python

![Logo](https://github.com/marufnawaz/email_automation/blob/main/1707140445728.png)

This Python project automates the process of sending daily email reports with a file attachment. The script schedules the email to be sent at a specific time each day using the `schedule` library. The attached report file is dynamically named based on the current date.

## Features

- Sends a daily email with a dynamic report attached.
- Configurable email parameters (sender, receiver, SMTP settings).
- Automated scheduling using the schedule library.
- Handles errors like file not found and email sending failure.

## Prerequisites

Ensure you have the following Python libraries installed:

```python
pip install schedule
```

## Project Structure

```python
├── main.py           # Main Python script to send emails and schedule tasks
```

## Code Explanation

### 1. Importing Required Libraries
The script uses various Python libraries for email handling (`smtplib`, `MIME`), file attachment (`encoders`), and scheduling (`schedule`).

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import schedule
import time
from datetime import datetime
```

### 2.Email Configuration

Define the necessary email parameters like sender and receiver email addresses, subject, SMTP server details, and login credentials.

```python
# Email configuration
sender_email = "maruf50@gmail.com"
receiver_email = "maruf50@outlook.com"
subject = "Testing daily report"
body = "Please find the attached report for today."
smtp_server = "smtp.gmail.com"
smtp_port = 587
login = "maruf50@gmail.com"
password = "6754 4784 6484 3663"  # This is a placeholder; use environment variables in real applications.
```

### 3. Generating Dynamic File Path

The report file path is generated dynamically based on the current date (e.g., `report_2024-10-20.txt`).

```python
def get_file_path():
    today = datetime.now().strftime("%Y-%m-%d")
    file_path = f"D:\\Python email\\report_{today}.txt"
    return file_path
```

### 4. Email Sending Function

The `send_email` function:

- Creates an email message.
- Attaches the body text and the dynamically generated report.
- Handles file-related and SMTP errors.

```python
def send_email():
    file_path = get_file_path()
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Attach the file
        with open(file_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename= {file_path.split("\\")[-1]}')
            msg.attach(part)

        # Send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(login, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print(f"Email sent successfully with file {file_path} to {receiver_email}")

    except FileNotFoundError:
        print(f"File not found: {file_path}. Email not sent.")
    except Exception as e:
        print(f"Failed to send email: {e}")
```

### 5. Scheduling the Task
The `schedule` library is used to trigger the `send_email` function at a specific time every day (in this case, 23:04).

```python
schedule.every().day.at("23:04").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(60)
```
### 6. Running the Script

To run the script, simply execute:

```python
python main.py
```

The script will continuously run in the background, checking every minute if the scheduled time to send the email has been reached.

## Conclusion

This project automates the process of sending daily reports via email with file attachments. It leverages Python's built-in email and scheduling libraries to handle the entire workflow. By dynamically generating the report filenames based on the current date, the script ensures that each report is unique to the day it is sent. In future iterations, this project could be expanded by using environment variables for sensitive information (like passwords) and integrating more advanced error handling and logging mechanisms.
