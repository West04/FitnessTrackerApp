import streamlit as st
from main import logout

st.title("Home Page")

st.sidebar.button("Logout", on_click=logout)
st.header("Welcome to the Website")

col1, col2 = st.columns(2)

with col1:
    st.header("Would you like to log your work?")
    if st.button("Press Here", key="workout"):
        st.switch_page("2_Workouts.py")

with col2:
    st.header("Would you like to track your progress?")
    if st.button("Press Here", key="tracking"):
        st.switch_page("3_Progress.py")
