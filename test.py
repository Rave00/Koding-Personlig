import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- Sett inn din info her ---
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "RazorMag360@gmail.com"       # Gmail-adressen din
APP_PASSWORD = "moev plel rwuy qthf"                        # App-passordet du laget
RECEIVER_EMAIL = "RazorMag360@gmail.com"    # kan være samme som sender
# -----------------------------

def send_email():
    subject = "📧 Test fra Python"
    body = "Hei! Dette er en testmelding for å sjekke at e-postscriptet ditt fungerer."

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

    print("✅ Test-epost sendt!")

# Kjør testen
send_email()
