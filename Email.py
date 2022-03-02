# Python code to illustrate Sending mail with attachments 
# from your Gmail account 

# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 


def send_email(toaddr,body_msg,sub_msg,path="",filename=""):


    fromaddr = "YOUR EMAIL ADDRESS"


# instance of MIMEMultipart     
    msg = MIMEMultipart() 

# storing the senders email address 
    msg['From'] = fromaddr 

# storing the receivers email address 
    msg['To'] = toaddr 

# storing the subject 
    msg['Subject'] = sub_msg

# string to store the body of the mail 
    body = body_msg

# attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 

# open the file to be sent 
    if not(filename==""):
        filename = filename
        attachment = open(path, "rb")

# instance of MIMEBase and named as p 
        p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form 
        p.set_payload((attachment).read())

# encode into base64 
        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg' 
        msg.attach(p)

# creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
    s.starttls() 

# Authentication 
    s.login(fromaddr, "YOUR_PASSWORD_OF_EMAIL_ADDR")

# Converts the Multipart msg into a string 
    text = msg.as_string() 

# sending the mail 
    s.sendmail(fromaddr, toaddr, text) 

# terminating the session 
    s.quit() 
