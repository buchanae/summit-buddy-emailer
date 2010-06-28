import csv
import smtplib
import sys

from email.mime.text import MIMEText


if len(sys.argv) != 2:
    print """Usage:  python emailer.py recipients.csv"""
    exit()

filename = sys.argv[1]
reader = csv.reader(open(filename, "rb"))

from_address = 'Mozilla Summit 2010 <summit2010@mozilla.com>'
subject = 'Hey Mozilla Summiteer, meet your Buddy!'
content = """
Welcome {recipient} and {buddy} to the Mozilla Summit 2010 Buddy Program.   We've
got some great fun lined up for you two in Whistler. (More on that in an
upcoming newsletter.) But before we get there, we wanted to introduce you to
each other. So, {recipient} meet {buddy}, {buddy} meet {recipient}.

While we think the Buddy Program is going to be a blast, you're not required to
participate in all of the games we've got set up, but we would like you two to
find each other at the welcome dinner and at least say hi and share a bit about
what you do at Mozilla.

In order to make that easier, you might want to use this virtual introduction
to let each other know where you're coming from and maybe share a photo or
description of yourself so you'll be easier to find at the reception.

We know you're going to have a great time at the Mozilla Summit 2010 and we
hope you'll participate in all of the good times we're preparing for our 300
buddy pairs.

Looking forward to it,
The Summit Buddy Team
"""

s = smtplib.SMTP()
s.connect()

for row in reader:
    r_email, r_first, r_last, b_email, b_first, b_last = row
    r_full = ' '.join((r_first, r_last))
    b_full = ' '.join((b_first, b_last))
    msg_text = content.format(recipient=r_full, buddy=b_full)
    msg = MIMEText(msg_text)
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = r_email
    msg['Cc'] = b_email
    s.sendmail(from_address, [r_email, b_email], msg.as_string())

s.quit()
