
from models.send_email import EmailSender
import pandas as pd


def load_data_and_send_email(df, subject, to_email, email, password, text=None):
    email_sender = EmailSender(email, password)
    
    # Verifica se df é do tipo DataFrame do Pandas
    if isinstance(df, pd.DataFrame):
        body = df.to_html(index=False)
    else:
        body = str(df)  # Converte para string se não for um DataFrame
    
    if text:
        # Combina o texto adicional com o corpo do email
        body = f"{text}<br><br>{body}"
    
    email_sender.send_email(to_email, subject, body)
    email_sender.quit()

def load_vendas_data(df_vendas, to_email, email, password, text):
    subject = "Seu Resumo Periódico da CSTecnologia (JENIUS-COMPRESS)"
    load_data_and_send_email(df_vendas, subject, to_email, email, password, text)