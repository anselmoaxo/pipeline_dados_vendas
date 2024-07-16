from models.connect import ConexaoPostgresql
import os
import pandas as pd

def extract_sql(query_file):
    engine = ConexaoPostgresql.create_connect()
    root_dir = os.getcwd()
    file_path = os.path.join(root_dir, 'data', 'input', query_file)
    if os.path.exists(file_path):
        # Agora você pode usar o arquivo
        with open(file_path, 'r') as file:
            sql_query = file.read()
            df = pd.read_sql(sql_query, engine)
            return df
    else:
        print("O arquivo não foi encontrado:", file_path)
        return None

def extract_sql_vendas():
    return extract_sql('venda.sql')

def extract_sql_faturamento():
    return extract_sql('faturamento_anual.sql')



