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


faturamento_dia_anterior = calculando_faturamento_dia_anterior(data_inicial, df_vendas)

#calculando Ticket Médio
ticket_medio = faturamento_dia_anterior/qtd_nfe_30dias


# Calculando faturamento de 7 dias atrás
faturamento_7dias_anterior = calculando_faturamento_7dias_anterior(data_inicial, df_vendas)


# Calculando faturamento de 30 dias atrás
faturamento_30dias_anterior = calculando_faturamento_30dias_anterior(data_inicial, df_vendas)


# Preparando o relatório para envio por e-mail
relatorio = pd.DataFrame({
    'Descrição': ['ONTEM', 'ÚLTIMOS 7 DIAS', 'ÚLTIMOS 30 DIAS'],
    'Valor': [faturamento_dia_anterior,faturamento_7dias_anterior, faturamento_30dias_anterior]
})

relatorio1= ''
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
        background-color: #FFFFFF;
        border: 1px solid #808080;
        border-radius: 5px;
        padding: 20px;
        box-shadow:
        3px 3px 5px rgba(0, 0, 0, 0.2), /* Sombra inferior direita */
        -3px -3px 5px rgba(255, 255, 255, 0.7);
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
        border: 0.5px solid #808080;
        padding: 8px;
        text-align: left;
    }}
    th {{
        background-color: #6495ED;
    }}
</style>
</head>
<body>
    <div class="container">
    <div class="logo">
            <img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/22000061898/logo/CS%20Tecnologia%20final%202012%20peq.jpg" alt="Logo" width="200">
        </div>
        <h1>JENIUS-COMPRESS</h1>
        <h2>Seu Resumo Periódico da CsTecnologia </h2>
        <h3>Total de Vendas:</h3>
        {relatorio.to_html(index=False)}
        <hr>
         <div class="highlight">
            <h3>Principais Destaques de Ontem:</h3>
            <p><strong>Produto Mais Vendido:</strong> Produto A (quantidade e valor)</p>
            <p><strong>Maior Região de Vendas:</strong> Região X (valor total)</p>
            <p><strong>Ticket Médio:</strong><b>R$ {ticket_medio:.2f}<b></p>
        </div>
    </div>
    
    <p>Atenciosamente,<br>CsTecnologia</p>
</body>
</html>
"""

# Enviando o 
with open('config/config.yml', 'r') as file:
    config = yaml.safe_load(file)
    email = config['gmail']['email']
    password = config['gmail']['password']
    to_email = config['gmail']['destinatario']

load_vendas_data(relatorio1, to_email, email, password, texto_adicional_html)
