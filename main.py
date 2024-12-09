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

    st.title("Log In")
    st.text_input("Enter your email", key="supabase_email")
    st.text_input("Enter your password", key="supabase_password")

    print(st.session_state.supabase_email, st.session_state.supabase_password)


if __name__ == '__main__':
    main()
