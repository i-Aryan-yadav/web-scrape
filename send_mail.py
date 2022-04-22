from email.mime.base import MIMEBase
import smtplib
#smtp= Simple mail transfer protocol
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send(file_name='scrape.csv'):
    email_from="yadavaryan1504@gmail.com"
    passcode="zyxqxsbjbvhtobae"
    email_to="alishasingh1896@gmail.com"
    subject="LEADING CRYPTOCURRENCIES REPORT"
    body="TODAY's CRYPTOCURRENCIES PRICE AND MORE DETAILS"

    msg=MIMEMultipart()
    msg["From"]=email_from
    msg["To"]=email_to
    msg["Subject"]=subject
    msg.attach(MIMEText(body,'plain'))

    my_file=open(file_name,'rb')
    part=MIMEBase('application','octet-stream')
    part.set_payload((my_file).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment; filename= ' + file_name)
    msg.attach(part)


    message=msg.as_string()


    server=smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email_from,passcode)
    server.sendmail(email_from, email_to, message)
    server.quit()