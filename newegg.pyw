import email
import os
import sys
import smtplib
import time
import urllib

email_addr = 'pete@johnson4.org'
email_passwd = '########'
email_smtp_info = 'smtp.1and1.com', 587
email_text_addr = '##########@mms.att.net'

def in_stock():
    text = urllib.urlopen(url1).read()
    if 'In stock' in text:
        return True
    elif 'OUT OF STOCK' in text:
        return False
    else:
        raise Exception
    
def alert():
    you = email_addr, email_text_addr
    msg = email.mime.text.MIMEText(url2)
    msg['Subject'] = 'Intel 310 80GB is in stock'
    msg['From'] = email_addr
    msg['To'] = ','.join(you)
    s = smtplib.SMTP(*email_smtp_info)
    s.login(email_addr, email_passwd)
    s.sendmail(email_addr, you, msg.as_string())
    s.quit()

url1 = 'http://content.newegg.com/LandingPage/ItemInfo4ProductDetail.aspx?Item=N82E16820167040'
url2 = 'http://www.newegg.com/Product/Product.aspx?Item=N82E16820167040'

cd = os.getcwd()
stock = os.path.join(cd, 'stock.txt')
history = os.path.join(cd, 'history.txt')
log = os.path.join(cd, 'log.txt')

try:
    print cd, stock, history, log
    
    previous = False
    with open(stock) as f:
        previous = eval(f.read())
    current = in_stock()
    
    if current and previous != current:   
        alert()
    with open(stock, 'w+') as f:
        f.write(str(current))
    with open(history, 'a+') as f:
        f.write(time.strftime('%c') + ' ' + str(current) + '\n')
        
except Exception as e:
    with open(log, 'a+') as f:
        f.write(time.strftime('%c') + ' ' + str(e) + '\n')
