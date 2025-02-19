# -*- coding: utf-8 -*-
"""
Clase 16-09-2024
"""
import streamlit as st
import joblib
import numpy as np 

model_filename = 'arnes.pkl'
# Cargamos el modelo desde el archivo
loaded_model = joblib.load(model_filename)