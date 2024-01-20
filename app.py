from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
import os 

import io
from PIL import Image

import requests


#load_dotenv()

#bearer = "Bearer "+os.getenv('HUGGINGFACEHUB_API_TOKEN')
token=st.secrets["HUGGINGFACEHUB_API_KEY"]
st.info(token)
bearer = "Bearer "+str(token)

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": bearer}


def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content



def generar_imagen_diffusor(input_text):
    image_bytes = query({"inputs": input_text})

    image = Image.open(io.BytesIO(image_bytes))

    if image is None:
        st.info("Error...")
        return None

    return image




choise = st.sidebar.selectbox("Selecciona ", ["HOME", "txt-to-img"])

if choise == "HOME":
    st.title("Generacion de imagenes con stable diffusion")
    with st.expander("Esta app..."):
        st.write("tiene 2 funciones: txt-to-img , img-to-img . genera y manipula imagenes con HuggingFace diffusors")

if choise == "txt-to-img":
    st.subheader("Generacion de imagenes con HugginFace Diffusors")
    input_text = st.text_input("Agrega texto para generar una imagen")
    if input_text is not None:
        if st.button("Generar imagen"):
            st.info(input_text)
            image_url = generar_imagen_diffusor(input_text)
            st.image(image_url)

            #if image_url is not None:
            #    image_buffer = BytesIO()
            #    image_url.save(image_buffer, format="PNG")
            #    st.download_button(
            #        label="Descargar imagen",
            #        data=image_buffer.getvalue(),
            #        file_name="imagen_generada.png",
            #        mime="image/png",
            #    )
