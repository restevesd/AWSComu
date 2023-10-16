# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 23:01:13 2023

@author: info
"""

import streamlit as st
import openai
from audio_recorder_streamlit import audio_recorder
import requests
from PIL import Image
import os

openai.api_key = "xxxxxxxxxxxxxxxxxxxxxxx"

uploaded_file = st.file_uploader("Choose a file",type=["ogg","mp3"])
upload_path = ""


#audio_bytes = audio_recorder()

if uploaded_file is not None:
    print(uploaded_file.name)
    # To read file as bytes:
    audio_bytes = uploaded_file.read()
    with open(os.path.join(upload_path,uploaded_file.name),"wb") as f:
        f.write((uploaded_file).getbuffer())
        
    st.audio(audio_bytes, format='audio/ogg')
    
    audio_file = open(os.path.join(upload_path,uploaded_file.name), "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    st.write(transcript["text"])
    with st.spinner('Generando Imagen...'):
        imagen = openai.Image.create(
            prompt=transcript["text"],
            n=2,
            size="1024x1024"
            )
        
        
        url = imagen["data"][0]["url"]
        myfile = requests.get(url)
        open('openIA2.png', 'wb').write(myfile.content)
        
        image = Image.open('openIA2.png')
    
        st.image(image, caption=transcript["text"])