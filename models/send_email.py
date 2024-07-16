import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailSender:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        try:
            self.server.login(email, password)
        except smtplib.SMTPAuthenticationError as e:
            print(f'Falha na autenticação: {e}')

    def send_email(self, to_email, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'html'))

        try:
            self.server.sendmail(self.email, to_email, msg.as_string())
            print(f'E-mail enviado para {to_email}')
        except smtplib.SMTPException as e:
            print(f'Erro ao enviar e-mail: {e}')

    def quit(self):
        self.server.quit()
