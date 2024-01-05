import requests
import xlwt
from xlwt import Workbook
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

# https://myaccount.google.com/lesssecureapps  -  to allow less secure apps to send emails
# https://support.google.com/mail/thread/188531222/my-application-can-no-longer-send-gmail-via-smtp?hl=en  -  to allow less secure apps to send emails

BASE_URL = 'https://remoteok.io/api'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Crome/96.0.4664.45 Safari/537.36' 
REQUEST_HEADER = {'User-Agent': USER_AGENT,  # Device and browser details
                  'Accept-Language': 'en-US,en;q=0.5'} # Language details


def get_job_postings():
    res = requests.get(url=BASE_URL, headers=REQUEST_HEADER)
    return res.json() 

def output_jobs_to_xls(data):
    wb = Workbook()
    job_sheet = wb.add_sheet('Jobs')
    headers = list(data[0].keys())

    # Create headers for the excel sheet
    for i in range(0, len(headers)):
        job_sheet.write(0, i, headers[i])
    
    # Write the data to the excel sheet
    for i in range(0, len(data)):
        job = data[i]
        values = list(job.values())

        # Write the values to the excel sheet
        for j in range(0, len(values)):
            job_sheet.write(i+1, j, values[j])


    wb.save('remoteok_jobs.xls')

# Send the email
def send_email(send_from, send_to, subject, text, files=None, server="localhost"):
    assert isinstance(send_to, list) # Make sure the send_to is a list
    msg = MIMEMultipart() # Create the message
    msg['From'] = send_from # Set the "from" field
    msg['To'] = COMMASPACE.join(send_to) # Set the "to" field
    msg['Date'] = formatdate(localtime=True) # Set the date field
    msg['Subject'] = subject # Set the subject field

    msg.attach(MIMEText(text)) # Attach the text to the message

    # Attach the files to the message
    for f in files or []: # For each file in the files list / if there are no files, then use an empty list
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(), 
                Name=basename(f) 
            ) 

        # After the file is closed
        part['Content-Disposition'] = f'attachment; filename="{basename(f)}"' # Set the content disposition
        msg.attach(part) # Attach the file to the message

    # Define how the message will be sent
    smtp = smtplib.SMTP('smtp.gmail.com: 587') # Create the smtp server
    smtp.starttls() # Start the TLS
    smtp.login(send_from, 'wzfu dcdv zgie ftpc')  # Use the correct email address for login
 
    # Login to the email
    smtp.sendmail(send_from, send_to, msg.as_string()) # Send the email
    smtp.close() # Close the connection



if __name__ == "__main__":
    json = get_job_postings()[1:]
    # print(json)
    output_jobs_to_xls(json)
    send_email('ronidummy26@gmail.com', ['ronipick3@gmail.com'], 'Jobs Posting', 
               'Here are the jobs', files=['remoteok_jobs.xls'])