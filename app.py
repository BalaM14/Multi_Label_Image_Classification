import streamlit as st
import pandas as pd
import tensorflow as tf
import numpy as np
from PIL import Image
import zipfile

"""
### Created By : Bala Murugan
#### LinkedIn : https://www.linkedin.com/in/balamurugan14/
# Binary Image Classification
"""
model = tf.keras.models.load_model("model.h5")
file_uploaded = st.file_uploader("Upload", type=["png","jpg","jpeg"], accept_multiple_files=True)
st.header('PREDICTED OUTPUT', divider='rainbow')
row_size=4
grid = st.columns(row_size)
col = 0
for file in file_uploaded:
    if file is not None:
        # To read file as bytes:
        #bytes_data = uploaded_file.getvalue()
        #st.write(bytes_data)


        image = Image.open(file)
        img = image.resize((224,224))
        img_array = np.array(img)
        img_array = np.expand_dims(img_array, axis=0) # [batch_size, row, col, channel]
        result = model.predict(img_array) # [[0.99, 0.01], [0.99, 0.01]]

        argmax_index = np.argmax(result, axis=1) # [0, 0]
        with grid[col]:
            if argmax_index[0] == 0:
                st.image(image)
                st.header('\t :blue[CAT]')
            else:
                st.image(image)
                st.header('\t :red[DOG]')
        col = (col + 1) % row_size