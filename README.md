# Daily Email Report Automation with Python

This Python project automates the process of sending daily email reports with a file attachment. The script schedules the email to be sent at a specific time each day using the `schedule` library. The attached report file is dynamically named based on the current date.

## Features

- Sends a daily email with a dynamic report attached.
- Configurable email parameters (sender, receiver, SMTP settings).
- Automated scheduling using the schedule library.
- Handles errors like file not found and email sending failure.

## Prerequisites

Ensure you have the following Python libraries installed:

```
pip install schedule
```
