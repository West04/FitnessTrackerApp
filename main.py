import streamlit as st
from dotenv import load_dotenv
from supabase import create_client, Client
import os


def main():
    # Load Environment Variables
    load_dotenv()

    # Connect to Supabase
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)

    # Create a container to center the content
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.title("Log In")
        st.text_input("Enter your email", key="supabase_email")
        st.text_input("Enter your password", key="supabase_password")

        if 'supabase_email' in st.session_state and 'supabase_password' in st.session_state:
            if st.button("Log In") and st.session_state.supabase_email and st.session_state.supabase_password:
                print(st.session_state.supabase_email, st.session_state.supabase_password)


if __name__ == '__main__':
    main()
