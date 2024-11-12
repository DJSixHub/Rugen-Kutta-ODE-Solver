import streamlit as st
import os

st.set_page_config(layout="wide")

st.title("Proyecto de Ecuaciones Diferenciales Ordinarias")
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

with st.sidebar:
    st.header("Menu")
    option = st.radio("Selecciona una opción:", ["Graficadora", "Informe", "Acerca de"])

if option == "Graficadora":
    
    st.subheader("Graficadora")
    
    interface_path = './UI/interface.py'
    
    with open(interface_path, 'r') as file:
        code = file.read()
        
    exec(code)
    
    
    
elif option == "Informe":
    st.subheader("Informe")
    
elif option == "Acerca de:":
    st.subheader("Acerca de")
    


