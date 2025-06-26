import streamlit as st
import qrcode
from datetime import datetime

st.title("QR Code Generator")

if 'clear_input' not in st.session_state:
    st.session_state.clear_input = False
if 'qr_generated' not in st.session_state:
    st.session_state.qr_generated = False

input_key = "input_data_cleared" if st.session_state.clear_input else "input_data"
data = st.text_input("Enter URL", key="input_data")

if st.button("Generate QR Code"):
    if data:
        img = qrcode.make(data)
        img_path = f'qrcodeimg/qrcode_{datetime.now().strftime("%Y%m%d%H%M%S")}.png'
        img.save(img_path)

        st.image(img_path, caption="QR Code", width=300)
        st.success("QR Code generated successfully")

        st.session_state.clear_input = True
        st.session_state.qr_generated = True
    else:
        st.error("Please enter a URL")

if st.session_state.clear_input:
    st.session_state.clear_input = False
