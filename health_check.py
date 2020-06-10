#!/usr/bin/env python3
import shutil
import psutil
import socket
import emails

disk = shutil.disk_usage('/')
cpu = psutil.cpu_percent(1)
mem = psutil.virtual_memory.available()

disk_free = (disk.free/disk.total)*100
host_res =socket.gethostbyname('localhost')
mem_free= mem.free//(1024**2)

mem_free= 11
cpu=30

sender= 'automation@example.com'
recipient='username@example.com'
body='Please check your system and resolve the issue as soon as possible.'

#Check condition and send email
if cpu > 80:
    sub = 'Error - CPU usage is over 80%'
    msg = emails.generate_error_report(sender, recipient, sub, body)
    emails.send_email(msg)

if disk_free < 20:
    sub = 'Error - Available disk space is less than 20%'
    msg = emails.generate_error_report(sender, recipient, sub, body)
    emails.send_email(msg)

if mem_free < 500:
    sub = 'Error - Available memory is less than 500MB'
    msg = emails.generate_error_report(sender, recipient, sub, body)
    emails.send_email(msg)

if not host_res == '127.0.0.1':
    sub = 'Error - localhost cannot be resolved to 127.0.0.1'
    msg = emails.generate_error_report(sender, recipient, sub, body)
    emails.send_email(msg)