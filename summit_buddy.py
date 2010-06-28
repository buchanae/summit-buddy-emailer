import csv
import smtplib

from email.mime.text import MIMEText


filename = "some.csv"
reader = csv.reader(open(filename, "rb"))

from_address = 'summit2010@mozilla.com'
content = """
Hi {recipient},

Your buddy is {buddy}

Thanks,
"""

s = smtplib.SMTP()

for row in reader:
    recipient_name = ' '.join((row[0], row[1]))
    buddy_name = ' '.join((row[3], row[4]))
    msg_text = content.format(recipient=recipient_name, buddy=buddy_name)
    msg = MIMEText(msg_text)
    msg['Subject'] = 'Summit Buddies'
    msg['From'] = from_address
    msg['To'] = row[2]
    msg['Cc'] = row[5]
    s.sendmail(from_address, row[2], msg.as_string())
