# -*- coding: utf-8 -*-
"""
Clase 16-09-2024
"""
import pickle
import streamlit as st
import joblib
import numpy as np

# Cargar el modelo desde el archivo
model_filename = 'modelo.pkl'
loaded_model = joblib.load(model_filename)

# Función para mostrar información en Streamlit
def mostrar_acerca_de():
    st.info("Esta es una aplicación de ejemplo.")

def mostrar_prediccion():
    st.info("Aquí puedes realizar predicciones.")

# Crear un menú desplegable en Streamlit
st.sidebar.title("Menú Desplegable")
opcion = st.sidebar.selectbox(
    "Selecciona una opción:",
    ["Acerca de", "Predicción", "Salir"]
)

# Manejar la selección del menú
if opcion == "Acerca de":
    mostrar_acerca_de()
elif opcion == "Predicción":
    mostrar_prediccion()
elif opcion == "Salir":
    st.stop()  # Detener la ejecución de la aplicación