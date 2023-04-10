import streamlit as st
import requests
from streamlit_lottie import st_lottie 

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    else:
        return r.json()

#--- Load Assets ---
lottie_professor = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_Fy9W8c.json")
def homeWork():
    with st.container():
        left_column,right_column = st.columns(2)
        with left_column:
            st.write('##')
            st.write('##')
            st.title("Hey Fellas!")
            st.subheader("I am the AI Professor")
            ##fill the below function with some suitable short description
            st.write("""
            The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 
            1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by 
            English versions from the 1914 translation by H. Rackham.
            """)
        with right_column:
            st.write("##")
            st_lottie(lottie_professor, height=400)

    st.write("---")

    
