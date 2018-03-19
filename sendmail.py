from smtplib import SMTP
import sys

if len(sys.argv) > 1:
    fromaddrs = sys.argv[1]
    toaddrs = sys.argv[2]
    msg = 'Subject: ' + sys.argv[3] + '\r\n'

with SMTP("vm-exchange", 2525) as smtp:
    smtp.ehlo()
    smtp.sendmail(fromaddrs, toaddrs, msg)
    print("Sent with msg: {}".format(msg))
    