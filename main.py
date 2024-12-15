import streamlit as st
from dotenv import load_dotenv
from supabase import create_client
import time
import os
import re


def main():
    if "supabase" not in st.session_state or st.session_state["supabase"] is None:
        # Load Environment Variables
        load_dotenv()

        # Connect to Supabase Client
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")

        st.session_state.supabase = create_client(url, key)

    if "response" not in st.session_state or st.session_state["response"] is None:
        login_page()
    else:
        home_page()


def home_page():
    st.title("Home Page")
    st.sidebar.button("Logout", on_click=logout)


def login_page():
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        auth_mode = st.radio("Login or Sign Up?", ("Login", "Sign Up"))

        if auth_mode == "Login":
            st.title("Log In")
            with st.form(key="login_form"):
                email = st.text_input("Enter your email")
                password = st.text_input("Enter your password", type="password")

                submit = st.form_submit_button("Login")

                if submit:
                    if email and password:
                        print(email, password)
                        time.sleep(1)
                        if login(email, password):
                            st.rerun()
                    else:
                        st.error("Please enter your email and password")
        else:
            st.title("Sign Up")
            with st.form(key="sign_up_form"):
                email = st.text_input("Enter your email")
                password = st.text_input("Enter your password", type="password")
                confirm_password = st.text_input("Confirm your password", type="password")

                submit = st.form_submit_button("Sign Up")

                if submit:
                    if email and password and confirm_password:
                        print(email, password, confirm_password)
                        if check_password(password):
                            if password == confirm_password:
                                if signup(email, password):
                                    st.success("Check Your Email to Confirm Your Account")
                                    st.rerun()
                            else:
                                st.error("Passwords do not match")
                    else:
                        st.error("Please enter your email and password")


def login(email: str, password: str):
    try:
        st.session_state.response = st.session_state.supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        return st.session_state.response.session is not None
    except Exception as e:
        st.error(f"Login failed: {str(e)}")
        return False


def signup(email: str, password: str):
    try:
        st.session_state.response = st.session_state.supabase.auth.sign_up({
            "email": email,
            "password": password
        })
        st.success("Account created successful")
        return st.session_state.response.session is not None

    except Exception as e:
        st.error(f"Sign up failed: {str(e)}")
        return False


def check_password(password):
    if len(password) < 8:
        st.error("Password must be at least 8 characters")
        return False
    if not re.search(r"[A-Z]", password):
        st.error("Password must contain at least one uppercase letter")
        return False
    if not re.search(r"[a-z]", password):
        st.error("Password must contain at least one lowercase letter")
        return False
    if not re.search(r"[0-9]", password):
        st.error("Password must contain at least one number")
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        st.error("Password must contain at least one special character")
        return False
    return True


def logout():
    try:
        if "response" in st.session_state:
            st.session_state.supabase.auth.sign_out()
            st.session_state.response = None
    except Exception as e:
        st.sidebar.error(f"Logout failed: {str(e)}")


if __name__ == '__main__':
    main()
