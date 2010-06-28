import csv
import smtplib
import sys

from email.mime.text import MIMEText


if len(sys.argv) != 2:
    print """Usage:  python emailer.py recipients.csv"""
    exit()

filename = sys.argv[1]
reader = csv.reader(open(filename, "rb"))

from_address = 'summit2010@mozilla.com'
content = """
Hi {recipient},

Your buddy is {buddy}

Thanks,
"""

s = smtplib.SMTP()
s.connect()

for row in reader:
    r_first, r_last, r_email, b_first, b_last, b_email = row
    r_full = ' '.join((r_first, r_last))
    b_full = ' '.join((b_first, b_last))
    msg_text = content.format(recipient=r_full, buddy=b_full)
    msg = MIMEText(msg_text)
    msg['Subject'] = 'Summit Buddies'
    msg['From'] = from_address
    msg['To'] = r_email
    msg['Cc'] = b_email
    s.sendmail(from_address, [r_email, b_email], msg.as_string())

s.quit()
