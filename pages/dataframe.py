import streamlit as st
from dataset import df
from utils import convert_csv, mensagem_sucesso

st.title('Dataset de Vendas')
with st.expander('Colunas'):
    colunas = st.multiselect(
        'Selecione as colunas',
        list(df.columns),
        list(df.columns)
        )
st.sidebar.title('Filtros')

with st.sidebar.expander('Categoria do Produto'):
    categorias = st.multiselect(
        'Selecione as categorias',
        df['Categoria do Produto'].unique(),
        df['Categoria do Produto'].unique()
        )
    
min_preco = df['Preço'].min()
max_preco = df['Preço'].max()

with st.sidebar.expander('Preço dos Produtos'):
    preco = st.slider(
        'Selecione a Faixa de Preço',
        min_preco,
        max_preco,
        (min_preco,max_preco)
    )


with st.sidebar.expander('Data da Compra'):
    data_compra = st.date_input(
        'Selecione um intervalo de Datas',
        (df['Data da Compra'].min(),
        df['Data da Compra'].max()),
        max_value=df['Data da Compra'].max()
    )





if categorias:
    df = df.query(f"`Categoria do Produto` in {categorias}")

if preco:
    df = df.query(f"Preço >= {preco[0]} and Preço <= {preco[1]}")


mx_data = df['Data da Compra'].max()
max_data = data_compra[1]


def log_error(mensagem):
    # Função para registrar o erro em um arquivo de log
    with open("log_erro.txt", "a") as arquivo:
        arquivo.write(mensagem + "\n")

try:
    if data_compra:
        if data_compra[0] and data_compra[1]:
            df = df.query(f"`Data da Compra` >= '{data_compra[0]}' and `Data da Compra` <= '{data_compra[1]}'")
except IndexError:
    log_error("Selecione a Data Final")
    pass


df = df[colunas]
### visuais



st.dataframe(df)

st.markdown(f'A tabela possui :blue[{df.shape[0]}] linhas e :blue[{df.shape[1]}] colunas')

st.markdown('Escreva um nome para o arqquivo')

coluna1, coluna2 = st.columns(2)

with coluna1:
    nome_arquivo = st.text_input(
        '',
        label_visibility='collapsed'
    )
    nome_arquivo += '.csv'

with coluna2:
    st.download_button(
        'Baixar arquivo',
        data=convert_csv(df),
        file_name=nome_arquivo,
        mime='text/csv',
        on_click=mensagem_sucesso

    )