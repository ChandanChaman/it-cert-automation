#! /usr/bin/env python3

import emails
from datetime import datetime
import reports
import os

#PDF REPORT

dir ='supplier-data/descriptions/'
date = (datetime.now().strftime("%B " "%d," " %Y"))
paragraph=''

for f in os.listdir(dir):
    dict = {}
    if f.endswith('.txt'):
        with open(dir+f,encoding='utf-8') as fh:
            line=fh.readlines()
            dict['name'] = line[0].strip()
            dict['weight'] = line[1].strip()
  #  json_list.append(dict)

    paragraph += '<br/>'
    paragraph += 'name: ' + dict['name']
    paragraph += '<br/>'
    paragraph += 'weight: ' + dict['weight']
    paragraph += '<br/>'

#print (paragraph)

title = 'Processed Update on ' + date
attachment= '/tmp/processed.pdf'

#Mail
sender='automation@example.com'
recipient='student-01-9903d750b864@example.com'
subject= 'Upload Completed - Online Fruit Store'
body= 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'

if __name__ == "__main__":
    reports.generate_report(attachment,title,paragraph)
    msg = emails.generate_email(sender, recipient, subject, body, attachment)
    emails.send_email(msg)
