from dataset import df
import pandas as pd
import streamlit as st
import time


def format_number(value, prefix = ''):
    for unit in ['','mil']:
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'
    return f'{prefix} {value:.2f} milhoes'

#receita por estado
df_rec_estado = df.groupby(['Local da compra'])[['Preço']].sum()
df_rec_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra','lat','lon']].merge(df_rec_estado, left_on='Local da compra', right_index=True).sort_values(by='Preço', ascending=False)


#receita mensal
df_rec_mensal = df.set_index('Data da Compra').groupby(pd.Grouper(freq='M'))['Preço'].sum().reset_index()


df_rec_mensal['ano'] = df_rec_mensal['Data da Compra'].dt.year
df_rec_mensal['mes'] = df_rec_mensal['Data da Compra'].dt.month

de_para_mes = {
    1:'Janeiro',
    2:'Fevereiro',
    3:'Março',
    4:'Abril',
    5:'Maio',
    6:'Junho',
    7:'Julho',
    8:'Agosto',
    9:'Setembro',
    10:'Outubro',
    11:'Novembro',
    12:'Dezembro'
}

df_rec_mensal['mes'] = df_rec_mensal['mes'].map(de_para_mes)

#3 -  Dataframe Receita

df_rec_categoria = df.groupby('Categoria do Produto')[['Preço']].sum().sort_values('Preço', ascending=False)


df_vendedores = pd.DataFrame(df.groupby(['Vendedor'])[['Preço']].agg(['sum','count']))
df_vendedores.columns = ['soma_receita','contagem_receita']
df_vendedores = df_vendedores.reset_index() 

#print(df_vendedores)

@st.cache_data

def convert_csv(df):
    return df.to_csv(index=False).encode('utf-8')

def mensagem_sucesso():
    success = st.success(
        'Arquivo baixado com sucesso',
        icon='✔'
    )
    time.sleep(3)
    success.empty()

