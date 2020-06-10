#!/usr/bin/env python3
import shutil
import psutil
import socket
import emails

#Disk Check
disk = shutil.disk_usage('/')
disk_free = (disk.free/disk.total)*100

#CPU check
cpu = psutil.cpu_percent(1)

# Host check
host_res =socket.gethostbyname('localhost')

#Memory Check
mem = psutil.virtual_memory()
free_mem = (mem.available)/(1024**2)

sender= 'automation@example.com'
recipient='student-01-9903d750b864@example.com'
body='Please check your system and resolve the issue as soon as possible.'

#Check condition and send email
if cpu > 80:
    subject = 'Error - CPU usage is over 80%'
    msg = emails.generate_error_report(sender, recipient, subject, body)
    emails.send_email(msg)

if disk_free < 20:
    subject = 'Error - Available disk space is less than 20%'
    msg = emails.generate_error_report(sender, recipient, subject, body)
    emails.send_email(msg)

if free_mem < 500:
    subject = 'Error - Available memory is less than 500MB'
    msg = emails.generate_error_report(sender, recipient, subject, body)
    emails.send_email(msg)

if not host_res == '127.0.0.1':
    subject = 'Error - localhost cannot be resolved to 127.0.0.1'
    msg = emails.generate_error_report(sender, recipient, subject, body)
    emails.send_email(msg)