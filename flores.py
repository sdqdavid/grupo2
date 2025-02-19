# -*- coding: utf-8 -*-
"""
Clase 16-09-2024
"""
import pickle
import streamlit as st
import joblib
import numpy as np
from PIL import Image  # Para cargar la imagen

# Cargar el modelo desde el archivo
model_filename = 'modelo.pkl'
loaded_model = joblib.load(model_filename)

# Función para mostrar información en Streamlit
def mostrar_inicio():
    st.title("Bienvenido al clasificador de flores Iris")
    st.write("""
    Esta aplicación utiliza un modelo de machine learning para predecir la especie de una flor Iris 
    basado en las características ingresadas.
    """)
    imagen = Image.open("inicio.jpg")
    st.image(imagen, caption="Clasificador de Flores Iris", use_container_width=True)

def mostrar_acerca_de():
    st.header("Acerca de esta aplicación")
    st.subheader("Clasificador de flores Iris")
    st.write("""
    Esta aplicación fue desarrollada para demostrar el uso de Streamlit en la creación de interfaces de usuario multipágina que integran modelos de machine learning.
    
    **Autores:** Jenny, Lorena, David  
    **Repositorio:** [GitHub - grupo2](https://github.com/sdqdavid/grupo2)
    """)

def mostrar_prediccion():
    st.header("Realizar una predicción")
    st.write("Ingresa las características de la flor Iris para predecir su especie.")

    # Campos para que el usuario ingrese los datos
    sepal_length = st.number_input("Longitud del sépalo (cm)", min_value=0.0, format="%.2f")
    sepal_width = st.number_input("Ancho del sépalo (cm)", min_value=0.0, format="%.2f")
    petal_length = st.number_input("Longitud del pétalo (cm)", min_value=0.0, format="%.2f")
    petal_width = st.number_input("Ancho del pétalo (cm)", min_value=0.0, format="%.2f")

    # Botón para realizar la predicción
    if st.button("Predecir"):
        # Crear un array con los datos ingresados por el usuario
        input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        
        # Realizar la predicción
        prediction = loaded_model.predict(input_data)
        
        # Mostrar el resultado de la predicción con imagen
        if prediction[0] == 0:
            st.success("La especie predicha es: **Setosa**")
            imagen = Image.open("setosa.jpg")
            st.image(imagen, caption="Iris Setosa", use_container_width=True)
        elif prediction[0] == 1:
            st.success("La especie predicha es: **Versicolor**")
            imagen = Image.open("versicolor.jpg")
            st.image(imagen, caption="Iris Versicolor", use_container_width=True)
        elif prediction[0] == 2:
            st.success("La especie predicha es: **Virginica**")
            imagen = Image.open("virginica.jpg")
            st.image(imagen, caption="Iris Virginica", use_container_width=True)
        else:
            st.error("No se pudo determinar la especie.")

# Crear un menú desplegable en Streamlit
st.sidebar.title("Menú Desplegable")
opcion = st.sidebar.selectbox(
    "Selecciona una opción:",
    ["Inicio", "Acerca de", "Predicción", "Salir"]
)

# Manejar la selección del menú
if opcion == "Inicio":
    mostrar_inicio()
elif opcion == "Acerca de":
    mostrar_acerca_de()
elif opcion == "Predicción":
    mostrar_prediccion()
elif opcion == "Salir":
    st.stop()  # Detener la ejecución de la aplicación

