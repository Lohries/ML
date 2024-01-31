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
        sex_model = 1


    st.header("Classe")
    classe = st.radio("Marque a classe",  ["**S**", "**C**", "**A**"])

    if (classe == '**S**'):
        st.write("Classe S, a mais alta do navio")
        class_model = 1
    elif (classe == '**C**'):
        st.write("Classe C, mais baixo do navio")
        class_model = 2
    elif (classe == '**A**'):
        st.write("Classe A, a pequena burguesia")
        class_model = 3


    st.header("Fare")
    slider = st.slider("Range do ticket", 10000.0, 100000.0)
    st.write("O valor da passagem ", slider, "$")

    st.button("Submit 💀")


with open("ML/Web_app/titanic_RFC.pkl", "rb") as file:
    model = pk.load(file)



st.header("Redes sociais")
st.write("[Linkedin]()")
st.write("[Instagram]()")
st.write("[GitHub]()")