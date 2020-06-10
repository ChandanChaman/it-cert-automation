#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_report(filename, title, additional_info):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["BodyText"])
  table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                ('ALIGN', (0,0), (-1,-1), 'CENTER')]
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info, empty_line])


dir ='supplier-data/descriptions/'
json_list=[]
for f in os.listdir(dir):
    dict = {}
    if f.endswith('.txt'):
        with open(dir+f,encoding='utf-8') as fh:
            line=fh.readlines()
            dict['name'] = line[0].strip()
            dict['weight'] = int(line[1].strip().strip('lbs').strip())
    json_list.append(dict)



if __name__ == "__main__":
    generate_report(attachment_path,'Processed Update on '+str(date.today()),pdf_data)
