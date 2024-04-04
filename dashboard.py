import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

# Carregar os dados
@st.cache_data
def load_data(path):
    df = pd.read_csv(path, sep=';')
    return df

# Carregar o modelo de machine learning
@st.cache_data
def load_model():
    # Carregar o modelo previamente treinado
    # Substitua isso com a carga do seu próprio modelo
    return 1

# Função para exibir a primeira página do dashboard
def main_page(df):
    st.title('Dashboard da Passos Mágicos')
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Criar uma layout de duas colunas
    col1, col2 = st.columns(2)

    # Visualização simples da distribuição das pontuações usando matplotlib
    with col1:
        st.subheader('Distribuição das Pontuações')
        plt.hist(df['IEG'], bins=20, edgecolor='black')
        st.pyplot()

    # Visualização da pontuação média por ano
    with col2:
        st.subheader('Pontuação Média por Ano')
        st.bar_chart(df.groupby('ano')['IEG'].mean())

    # Análise da distribuição das notas por tipo de pedra
    st.subheader('Distribuição das Notas por Tipo de Pedra')
    for pedra in df['PEDRA'].unique():
        pedra_data = df[df['PEDRA'] == pedra]
        plt.hist(pedra_data['IEG'], bins=20, alpha=0.5, label=pedra)
    plt.xlabel('IEG')
    plt.ylabel('Frequência')
    plt.legend()
    st.pyplot()

# Função para exibir a segunda página com o formulário
def form_page(modelo):
    st.title('Formulário de Previsão de Ponto de Virada')
    st.write('Preencha os campos abaixo para prever o Ponto de Virada do Aluno:')
    aluno_id = st.text_input('ID do Aluno:')
    IEG = st.slider('IEG:', min_value=0.0, max_value=10.0, step=0.1)
    INDE = st.slider('INDE:', min_value=0.0, max_value=10.0, step=0.1)
    IAN = st.slider('IAN:', min_value=0.0, max_value=10.0, step=0.1)
    IPS = st.slider('IPS:', min_value=0.0, max_value=10.0, step=0.1)
    IAA = st.slider('IAA:', min_value=0.0, max_value=10.0, step=0.1)
    ano = st.selectbox('Ano:', options=[2020, 2021, 2022])
    submit_button = st.button('Prever Ponto de Virada')

    if submit_button:
        # Criar um dataframe com os dados do formulário
        input_data = pd.DataFrame({
            'IEG': [IEG],
            'INDE': [INDE],
            'IAN': [IAN],
            'IPS': [IPS],
            'IAA': [IAA],
            'ano': [ano]
        })

        # Fazer a previsão usando o modelo de machine learning
        predicao = modelo.predict(input_data)

        # Exibir o resultado da previsão
        st.write('Ponto de Virada Previsto:', predicao[0])

# Executar o dashboard
if __name__ == '__main__':
    df = load_data('dados/dados_processados/pede_passos.csv')
    modelo = load_model()
    menu = st.sidebar.radio("Menu", ('Dashboard', 'Formulário'))
    
    if menu == 'Dashboard':
        main_page(df)
    elif menu == 'Formulário':
        form_page(modelo)
