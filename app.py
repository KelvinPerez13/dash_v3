import streamlit as st
import plotly.express as px
from dataset import df
from utils import format_number
from graficos import *
from utils import df_rec_mensal

st.set_page_config(layout='wide')
st.title('Dash de vendas :shopping_trolley:')

st.sidebar.title('Filtros Disponiveis')

filtro_vendedor = st.sidebar.multiselect(
    'Vendedores',
    df['Vendedor'].unique(),

)
if filtro_vendedor:
    st.write('Vendedores Mostrado sao:', filtro_vendedor)
else:
    st.write('Vendedores Mostrado sao:', "Todos")

if filtro_vendedor:
    df = df[df['Vendedor'].isin(filtro_vendedor)]

###slider de preco

st.sidebar.title('Filtro de Preço')

min = df['Preço'].min()
max = df['Preço'].max()



filtro_preco = st.sidebar.slider(
        'Selecione um valor',
        min,
        max,
        (min,max)
)
st.write('Preço Mostrado ate:', filtro_preco)

if filtro_preco:
    df = df.query(f"Preço >= {filtro_preco[0]} and Preço <= {filtro_preco[1]}")

aba1, aba2, aba3 = st.tabs(['Dataset','Receita','Vendedores'])
with aba1:
    st.dataframe(df)
    
with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Receita Total', format_number(df['Preço'].sum(),"R$"))
        st.plotly_chart(grafico_map_estado, use_container_width=True)
        st.plotly_chart(grafico_rec_estado, use_container_width=True)
    with coluna2:
        st.metric('Quantidade de Vendas', format_number(df.shape[0]))
        st.plotly_chart(grafico_rec_mensal, use_container_width=True)
        st.plotly_chart(grafico_rec_categoria, use_container_width=True)
with aba3:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.plotly_chart(grafico_rec_vendedores, use_container_width=True)
    with coluna2:
        st.plotly_chart(grafico_cont_vendedores, use_container_width=True)
        
