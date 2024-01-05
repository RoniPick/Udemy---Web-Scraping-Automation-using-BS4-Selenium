import requests
import xlwt
from xlwt import Workbook
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

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


if __name__ == "__main__":
    json = get_job_postings()[1:]
    # print(json)
    output_jobs_to_xls(json)