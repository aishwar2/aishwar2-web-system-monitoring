import psutil
import smtplib
import time

# Set your email configuration
sender_email = "yadav.aishwar253@yandex.com"
receiver_email = "aishwar253@outlook.com"
smtp_server = "smtp.yandex.com"
smtp_port = 465
smtp_username = "aishwar253@yandex.com"
smtp_password = "25393165"

# Define the CPU usage threshold (in percentage)
cpu_threshold = 10
duration_threshold = 60  # 10 minutes in seconds

def send_email(subject, body):
    msg = f"Subject: {subject}\n\n{body}"
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, msg)

def main():
    start_time = time.time()
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        if cpu_percent > cpu_threshold:
            elapsed_time = time.time() - start_time
            if elapsed_time >= duration_threshold:
                subject = "High CPU Usage Alert"
                body = f"CPU usage exceeded {cpu_threshold}% for more than 1 minutes."
                send_email(subject, body)
                start_time = time.time()  # Reset the timer

if __name__ == "__main__":
    main()
