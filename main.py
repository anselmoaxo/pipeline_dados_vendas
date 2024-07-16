import pandas as pd
from scripts.extract import extract_sql_vendas
from scripts.transform import transformando_data_inicial, calculando_faturamento_dia_anterior, calculando_faturamento_7dias_anterior, calculando_faturamento_30dias_anterior, calculando_qtd_nfe_30dias_anterior
from scripts.load import load_vendas_data
import yaml

# Definindo a data inicial
data_inicial = transformando_data_inicial()

# Extraindo dados de vendas
df_vendas = extract_sql_vendas()

# Calculando faturamento do dia anterior

# Calculando faturamento do dia anterior
qtd_nfe_30dias = calculando_qtd_nfe_30dias_anterior(data_inicial, df_vendas)
print(f"Quantidade Emitidas de NFE dia 30 atrás : {int(qtd_nfe_30dias)}")

faturamento_dia_anterior = calculando_faturamento_dia_anterior(data_inicial, df_vendas)
print(f"Faturamento do dia anterior: {faturamento_dia_anterior}")

# Calculando faturamento de 7 dias atrás
faturamento_7dias_anterior = calculando_faturamento_7dias_anterior(data_inicial, df_vendas)
print(f"Faturamento de 7 dias atrás: {faturamento_7dias_anterior}")

# Calculando faturamento de 30 dias atrás
faturamento_30dias_anterior = calculando_faturamento_30dias_anterior(data_inicial, df_vendas)
print(f"Faturamento de 30 dias atrás: {faturamento_30dias_anterior}")

# Preparando o relatório para envio por e-mail
relatorio = pd.DataFrame({
    'Descrição': ['Quantidade Emitidas de NFE dia 30 atrás','Faturamento do dia anterior', 'Faturamento de 7 dias atrás', 'Faturamento de 30 dias atrás'],
    'Valor': [qtd_nfe_30dias,faturamento_dia_anterior, faturamento_7dias_anterior, faturamento_30dias_anterior]
})


# Formatar texto adicional com HTML para e-mail
texto_adicional_html = f"""
<html>
<head>
<style>
    body {{
        font-family: Arial, sans-serif;
        line-height: 1.6;
        background-color: #f2f2f2;
        padding: 20px;
    }}
    .container {{
        max-width: 800px;
        margin: 0 auto;
        background-color: #fff;
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 20px;
    }}
    h1 {{
        color: #333;
    }}
    p {{
        color: #666;
    }}
    table {{
        width: 100%;
        border-collapse: collapse;
    }}
    th, td {{
        border: 1px solid #ddd;
        padding: 8px;
        text-align: left;
    }}
    th {{
        background-color: #f2f2f2;
    }}
</style>
</head>
<body>
    <div class="container">
    <div class="logo">
            <img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/22000061898/logo/CS%20Tecnologia%20final%202012%20peq.jpg" alt="Logo" width="200">
        </div>
        <h1>Relatório de Vendas</h1>
        <p>Prezados,</p>
        <p>Segue o relatório de vendas atualizado conforme solicitado:</p>
        <h2>Relatório Detalhado</h2>
        {relatorio.to_html(index=False)}
    </div>
    <p>Atenciosamente,<br>Equipe de Vendas</p>
</body>
</html>
"""

# Enviando o 
with open('config/config.yml', 'r') as file:
    config = yaml.safe_load(file)
    email = config['gmail']['email']
    password = config['gmail']['password']
    to_email = config['gmail']['destinatario']

load_vendas_data(relatorio, to_email, email, password, texto_adicional_html)
