import pandas as pd
import datetime
from num2words import num2words
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from webexsdksend import WebexSendMsg

from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

sender_email = os.getenv('SENDER_MAIL')
receiver_email = os.getenv('RECIEVER_MAIL')
password = os.getenv('MAIL_PASSWORD')

def send_mail(content):
    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    html = """\
    <html>
    <body>
        <p>{0}
        </p>
    </body>
    </html>
    """.format(content)

    # Turn these into plain/html MIMEText objects
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

def check_work_anniversary(da):
    current_time = datetime.datetime.now()
    #current_time = datetime.datetime.strptime('08/01/22 18:00', '%d/%m/%y %H:%M')
    get_year_date = da.split(' ')[0]
    year,month,day = get_year_date.split('-')
    print(year,month,day,current_time.year,current_time.month,current_time.day)
    if (int(month) == current_time.month and int(day) == current_time.day):
        return current_time.year - int(year)
    return 0

def check_birthday(dat):
    current_time = datetime.datetime.now()
    #current_time = datetime.datetime.strptime('18/08/22 18:00', '%d/%m/%y %H:%M')
    day,month = dat.split('/')
    print(day,month,current_time.month,current_time.day)
    if (int(month) == current_time.month and int(day) == current_time.day):
        return True
    return False

def send_message(message):
    print(message)

if __name__ == "__main__":
    msg = WebexSendMsg(roomId=os.getenv('WEBEX_ROOM_ID_TO_SEND'))
    #msg.createMsg(message="{0}\U0001F3C6 \U0001F38A \U0001F389".format('some random txt'))
    filepath = os.getenv('MAIL_PASSWORD')
    excel_data_df = pd.read_excel(filepath, sheet_name='Form1')
    print(datetime.datetime.now())
    for name,joining_date in zip(excel_data_df['Employee Name'],excel_data_df['Date of Joining of cisco'].astype(str)):
        #print(name,joining_date)
        year = check_work_anniversary(joining_date)
        if year > 0:
            send_mail("Happy {0} work anniversary {1} \U0001F3C6 \U0001F38A \U0001F389".format(num2words(year,to='ordinal'),name))
            msg = WebexSendMsg(roomId=os.getenv('WEBEX_ROOM_ID_TO_SEND'))
            msg.createMsg(message="Happy {0} work anniversary {1} \U0001F3C6 \U0001F38A \U0001F389".format(num2words(year,to='ordinal'),name))

    for name,birth_date in zip(excel_data_df['Employee Name'],excel_data_df['Birthday in DD-MMM format (eg. 13-Aug)'].astype(str)):
        #print(name,birth_date)
        if check_birthday(birth_date):
            send_mail("Happy Birthday {} \U0001F370 \U0001F389 \U0001F38A".format(name))
            msg = WebexSendMsg(roomId=os.getenv('WEBEX_ROOM_ID_TO_SEND'))
            msg.createMsg(message="Happy Birthday {} \U0001F370 \U0001F389 \U0001F38A".format(name))
