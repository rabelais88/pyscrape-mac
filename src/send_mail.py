"""
# /src/private.py(gitignored)
user_for_mail = 'abcd@gmail.com' # google account
password_for_email = 'abcd'
# BEWARE! this SMTP is not allowed from google by default
# in order to enable this: 보안 설정>보안 수준이 낮은 앱 허용: 사용 안함>사용 함
# in English: Google Account>Sign-in & security>Allow less secure apps: OFF>ON
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from private import mail, password_for_email

msg = MIMEText('the mail content goes here')
msg['subject'] = Header('Test Mail Header', 'utf-8')
msg['from'] = 'sungryeolp@gmail.com'
msg['to'] = 'railguns@gmail.com'

with smtplib.SMTP_SSL('smtp.gmail.com') as smtp:
  smtp.login(mail, password_for_email)
  smtp.ehlo()
  smtp.send_message(msg)
