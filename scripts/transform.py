import pandas as pd
from datetime import datetime, timedelta

def transformando_data_inicial():
    data_inicial_str = "2023-11-09"
    data_inicial = datetime.strptime(data_inicial_str, "%Y-%m-%d")
    return data_inicial

def calculando_faturamento_dia_anterior(data_inicial, df_vendas):
    dia_anterior = data_inicial - timedelta(days=1)
    df_vendas['ped01_emissao'] = pd.to_datetime(df_vendas['ped01_emissao'])
    filtro_dia_anterior = df_vendas['ped01_emissao'].dt.date == dia_anterior.date()
    vendas_dia_anterior = df_vendas[filtro_dia_anterior]['valor_total'].sum().round(2)
    return vendas_dia_anterior

def calculando_faturamento_7dias_anterior(data_inicial, df_vendas):
    data_7_dias_atras = data_inicial - timedelta(days=7)
    df_vendas['ped01_emissao'] = pd.to_datetime(df_vendas['ped01_emissao'])
    filtro_7_dias = df_vendas['ped01_emissao'].between(data_7_dias_atras, data_inicial)
    vendas_7_dias = df_vendas[filtro_7_dias]['valor_total'].sum().round(2)
    return vendas_7_dias

def calculando_faturamento_30dias_anterior(data_inicial, df_vendas):
    data_30_dias_atras = data_inicial - timedelta(days=30)
    df_vendas['ped01_emissao'] = pd.to_datetime(df_vendas['ped01_emissao'])
    filtro_30_dias = df_vendas['ped01_emissao'].between(data_30_dias_atras, data_inicial)
    vendas_30_dias = df_vendas[filtro_30_dias]['valor_total'].sum().round(2)
    return vendas_30_dias

def calculando_qtd_nfe_30dias_anterior(data_inicial, df_vendas):
    data_30_dias_atras = data_inicial - timedelta(days=1)
    df_vendas['ped01_emissao'] = pd.to_datetime(df_vendas['ped01_emissao'])
    filtro_30_dias = df_vendas['ped01_emissao'].between(data_30_dias_atras, data_inicial)
    qtd_nfe = df_vendas[filtro_30_dias]['valor_total'].count()
    return qtd_nfe