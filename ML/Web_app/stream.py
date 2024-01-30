import streamlit as st
import pandas as pd
import pickle as pk


st.title("Modelo do Titanic")
st.text("Selecione os parâmetros e descubra quem sobreviveu ??????")
st.image('chopper.jpeg')


with st.sidebar:
    st.header("Sexo")
    sex = st.radio("Marque o sexo", ["Masculino", "Feminino"])
    if (sex == 'Masculino'):
        st.write("CaaAvVaLLo")


    st.header("Classe")
    classe = st.radio("Marque a classe",  ["**S**", "**C**", "**A**"])

    if (classe == '**S**'):
        st.write("Classe S, a mais alta do navio")
    elif (classe == '**C**'):
        st.write("Classe C, mais baixo do navio")
    elif (classe == '**A**'):
        st.write("Classe A, a pequena burguesia")
    else:
        st.write("Nada foi selecionado")

    
    st.button("Submit")

st.header("Redes sociais")
st.write("[Linkedin]()")
st.write("[Instagram]()")
st.write("[GitHub]()")

