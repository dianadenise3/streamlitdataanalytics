import streamlit as st
import pandas as pd

st.title('Esto es un título')
st.header('Esto es un header')
st.markdown('*italica*')

df=pd.read_csv('train.csv') #Como lo vamos a subir a streamlit, metemos el archivo en esta carpeta
st.dataframe(df)