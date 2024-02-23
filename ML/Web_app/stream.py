import streamlit as st
import pandas as pd
import pickle as pk

def main():
    st.title("Modelo do Titanic")
    st.text("Selecione os parâmetros e descubra quem sobreviveu ??????")

    with st.sidebar:
        st.header("Sexo")
        sex = st.radio("Marque o sexo", ["Masculino", "Feminino"])
        if sex == 'Masculino':
            sex_model = 1
        else:
            sex_model = 0

        st.header("Classe")
        classe = st.radio("Marque a classe",  ["**S**", "**C**", "**A**"])
        if classe == '**S**':
            st.write("Classe S, a mais alta do navio")
            class_model = 1
        elif classe == '**C**':
            st.write("Classe C, mais baixo do navio")
            class_model = 2
        elif classe == '**A**':
            st.write("Classe A, a pequena burguesia")
            class_model = 3

        st.header("Fare")
        slider = st.slider("Range do ticket", 10000.0, 100000.0)
        st.write("O valor da passagem ", slider, "$")

        if st.button("Submit 💀"):
          
            with open("ML/Web_app/titanic_RFC.pkl", "rb") as file:
                model = pk.load(file)

          
            features = [[sex_model, class_model, slider]]
          
            prediction = model.predict(features)

            
            if prediction[0] == 1:
                st.write("Este passageiro teria sobrevivido.")
                st.image()
            else:

                st.write("Este passageiro teria morrido.")

    st.header("Redes sociais")
    st.write("[Linkedin](www.linkedin.com/in/luis-henrique-telo-ladeira-mota-6a848124a)")
    st.write("[Instagram]()")
    st.write("[GitHub]()")

if __name__ == "__main__":
    main()
