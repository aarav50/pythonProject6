import streamlit
import  main

x=main.load_data()
with streamlit.expander('Data'):
    streamlit.write(x[0])
streamlit.radio('show summary',('yes','no'))