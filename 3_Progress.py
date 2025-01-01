import streamlit as st
from main import logout

st.title('Progress')
st.sidebar.button("Logout", on_click=logout)

