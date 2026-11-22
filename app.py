import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.header('Análise de anúncios de veículos')

st.write('Explore os dados dos veículos utilizando os gráficos abaixo.')

if st.button('Mostrar histograma'):
    fig = px.histogram(df, x='price', title='Distribuição dos preços dos veículos')
    st.plotly_chart(fig)

if st.button('Mostrar gráfico de dispersão'):
    fig = px.scatter(df, x='odometer', y='price',
                     title='Relação entre quilometragem e preço')
    st.plotly_chart(fig)
