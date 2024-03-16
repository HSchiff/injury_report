import smtplib
from email.message import EmailMessage
from bills import parse
import schedule
import time

def send_email():
    parse()

    msg = EmailMessage()

    # set email headers
    msg["From"] = "hschiffty@gmail.com"
    msg["Subject"] = "Daily Reminder"
    msg["To"] = "hschiffty@gmail.com"
    msg.set_content("Good morning!")
    msg.add_attachment(open("log.txt", "r").read())

    # set up smtp
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("hschiffty@gmail.com", 'jrzi exsx dojt qieq')
    s.send_message(msg)
    s.quit()

# sends email everyday at noon
schedule.every().day.at("12:00:00").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(60)
