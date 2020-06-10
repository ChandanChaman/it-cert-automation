import emails
from datetime import date
import reports
import os

sender='automation@example.com'
recipient='student-04-c3d3e472a0ef@example.com'
subject= 'Upload Completed - Online Fruit Store'
body= 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
attachment_path= '/tmp/processed.pdf'


pdf_data=''
for data in json_list:
    pdf_data+='<br/>'
    pdf_data+='name: '+data['name']
    pdf_data+='<br/>'
    pdf_data+='weight: '+str(data['weight'])
    pdf_data+='<br/>'

print (pdf_data)



if __name__ == "__main__":
    reports.generate_report(attachment_path,'Processed Update on '+str(date.today()),pdf_data)
    msg = emails.generate_email(sender, recipient, subject, body, attachment_path)
    #emails.send_email(msg)

