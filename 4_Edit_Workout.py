import streamlit as st

tab1, tab2 = st.tabs(["Select", "Edit"])

with tab1:
    st.title("Select")

    col1, col2 = st.columns(2)

    date_choice = None
    exercise_choice = None

    with col1:
        if st.button("Select by Date"):
            date_choice = True
            exercise_choice = False

    with col2:
        if st.button("Edit by Exercise"):
            exercise_choice = True
            date_choice = False

    if date_choice:
        with st.form(key="select_by_date"):
            date = st.date_input("Enter the Date of the Workout")

            data_submit = st.form_submit_button("Search")

            if data_submit:
                query_response_date = (
                    st.session_state.supabase
                    .table("Workout")
                    .select("*")
                    .eq("create_at", date).execute()
                )

                if query_response_date.error:
                    st.error(f"An Error occurred: {query_response_date.error}")
                elif query_response_date.data:
                    st.success("Workout Found")
                    # Add more logic to correctly store query from database
                    st.write(query_response_date.data)
                else:
                    st.success("There is not a workout under that date")

    if exercise_choice:
        with st.form(key="edit_by_exercise"):
            exercise_options = ['Squat', 'Bench Press', 'Dead lift', 'Overhead Press', ]  # Implement database interaction here
            exercise = st.selectbox("Enter the Exercise You Want to Search By", exercise_options)

            exercise_submit = st.form_submit_button("Search")

            if exercise_submit:
                query_response_exercise = (
                    st.session_state.supabase
                    .table("Workout")
                    .select("*")
                    .eq("create_at", date).execute()
                )  # Need to redo this query

                if query_response_exercise.error:
                    st.error(f"An Error occurred: {query_response_exercise.error}")
                elif query_response_exercise.data:
                    st.success("Workout Found")
                    # Add more logic to correctly store query from database
                    st.write(query_response_exercise.data)
                else:
                    st.success("There is not a workout under that exercise")

with tab2:
    st.title("Edit")

