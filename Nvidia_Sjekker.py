# Sjekker Nvidias nettside om tilgjengelige grafikkort.

from apscheduler.schedulers.blocking import BlockingScheduler
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

URL = "https://marketplace.nvidia.com/nb-no/consumer/graphics-cards/?locale=nb-no&page=1&limit=12&gpu=RTX%205080&gpu_filter=RTX%205090~1,RTX%205080~1,RTX%205070~1"



SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "RazorMag360@gmail.com"
APP_PASSWORD = "moev plel rwuy qthf"  # fra steg 1
RECEIVER_EMAIL = "RazorMag360@gmail.com"

def send_email():
    subject = "✅ Varen er på lager!"
    body = f"Sjekk linken: {URL}"

    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SENDER_EMAIL, APP_PASSWORD)
    server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
    server.quit()
    print("📧 Epost sendt!")

def sjekk_lager():
    response =  requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    if "Kjøp nå" in soup.get_text():
        send_email("✅ Varen er på lager!", f"Sjekk linken: {URL}")
        print("Varen er på lager!")
    else:
        print("Varen er ikke på lager.")


scheduler = BlockingScheduler()
# Kjør hver dag kl. 12:00 UTC (tilsvarer 13:00 norsk tid på vinter, 14:00 sommer)
scheduler.add_job(sjekk_lager, 'cron', hour=12, minute=0)
scheduler.start()

