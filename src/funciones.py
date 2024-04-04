import streamlit as st
import base64


def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

        pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="500" type="application/pdf"></iframe>'

        # Displaying File
        st.markdown(pdf_display, unsafe_allow_html=True)
