import plotly.express as px
from utils import *

grafico_map_estado = px.scatter_geo(
    df_rec_estado,
    lat='lat',
    lon='lon',
    scope='south america',
    size= 'Preço',
    template='seaborn',
    hover_name='Local da compra',
    hover_data={'lat':False, 'lon':False},
    title='Receita por Estado'
)

grafico_rec_mensal = px.line(
    df_rec_mensal, 
    x = 'mes',
    y = 'Preço',
    markers= True,
    range_y= (0, df_rec_mensal[['Preço']].max()),
    color= 'ano',
    line_dash= 'ano',
    title= 'Receita Mensal'

)

grafico_rec_mensal.update_layout(yaxis_title = 'Receita')

grafico_rec_estado = px.bar(
    df_rec_estado.sort_values(by='Preço', ascending=False).head(10),
    x = 'Local da compra',
    y = 'Preço',
    text_auto= True,
    title='Top Receita Por estados',
    color_discrete_sequence=px.colors.qualitative.T10
)

grafico_rec_categoria = px.bar(
    df_rec_categoria.head(10),
    text_auto=True,
    title='Top 10 Categorias maior receita',
    color_discrete_sequence=px.colors.qualitative.Prism
)

#3 - grafico vendedores

grafico_rec_vendedores = px.bar(
    df_vendedores.head(10).sort_values(by='soma_receita', ascending=True),
    x = 'soma_receita',
    y = 'Vendedor',
    text_auto=True,
    title='Top 10 vendedores com receita'
   
)


grafico_cont_vendedores = px.bar(
    df_vendedores.head(10).sort_values(by='contagem_receita', ascending=True),
    x = 'contagem_receita',
    y = 'Vendedor',
    text_auto=True,
    title='Top 10 vendedores por volume'

)