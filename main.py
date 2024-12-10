import streamlit as st
from dotenv import load_dotenv
from supabase import create_client, Client
import os


def main():
    # Load Environment Variables
    load_dotenv()

    # Connect to Supabase Client
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        auth_mode = st.radio("Login or Sign Up?", ("Login", "Sign Up"))

        if auth_mode == "Login":
            st.title("Log In")
            email = st.text_input("Enter your email")
            password = st.text_input("Enter your password")

            # if login(supabase, email, password):
            #    st.switch_page("home.py")

        else:
            st.title("Log In")
            email = st.text_input("Enter your email")
            password1 = st.text_input("Enter your password")
            password2 = st.text_input("Confirm your password")

            # if password1 == password2:
            #    signup(supabase, email, password1)
            # else:
            #    st.error("Passwords don't match")


def login(supabase: Client, email: str, password: str):
    try:
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        return response.session is not None
    except Exception as e:
        st.error(f"Login failed: {str(e)}")
        return False


def signup(supabase: Client, email: str, password: str):
    try:
        response = supabase.auth.sign_up({
            "email": email,
            "password": password
        })
        st.success("Account created successful")
        return response.session is not None

    except Exception as e:
        st.error(f"Sign up failed: {str(e)}")
        return False


if __name__ == '__main__':
    main()
