# Análise de Anúncios de Veículos

Este projeto foi desenvolvido durante o Sprint 5 da TripleTen. O objetivo é criar um aplicativo web simples para explorar dados de anúncios de veículos.

A aplicação utiliza Python e Streamlit para apresentar gráficos interativos a partir de um conjunto de dados de veículos usados.

## Funcionalidades

- **Histograma de preços:** permite visualizar a distribuição dos preços dos veículos anunciados.
- **Gráfico de dispersão:** mostra a relação entre a quilometragem e o preço dos veículos.

Os gráficos são criados com Plotly Express e aparecem quando o usuário clica nos respectivos botões.

## Tecnologias utilizadas

- Python
- Pandas
- Streamlit
- Plotly Express

## Como executar o projeto

Instale as dependências:

```bash
pip install -r requirements.txt
```

Inicie a aplicação:

```bash
streamlit run app.py
```

Depois, acesse o endereço local informado pelo Streamlit no terminal.

## Conjunto de dados

O projeto utiliza o arquivo `vehicles_us.csv`, disponibilizado pela TripleTen, que contém informações sobre anúncios de venda de veículos.
