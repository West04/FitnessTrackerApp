import streamlit as st
from Exercise import Exercise
from main import logout

st.sidebar.button("Logout", on_click=logout)


def save_draft():
    print("Draft Saved")
    # Need to implement connection with database here


def save_workout():
    print("Workout Saved")

    # Need to implement connection with database here


def add_an_exercise():
    st.session_state.new_workout.append(Exercise())


def delete_an_exercise():
    if st.session_state.new_workout:
        st.session_state.new_workout.pop()


def render_workout_form():
    exercise_options = ['Squat', 'Bench Press', 'Dead lift', 'Overhead Press', ]  # Implement database interaction here

    if "new_workout" not in st.session_state:
        st.session_state.new_workout = list()

    new_workout = st.session_state.new_workout
    for i in range(len(new_workout)):
        st.markdown(f"## Exercise {i + 1}")

        selected_exercise = st.selectbox(
            f'Choose Exercise',
            exercise_options,
            key=f'exercise_select_{i}'
        )
        new_workout[i].change_name(selected_exercise)

        sets = st.number_input("Number of Sets", min_value=1, step=1, key=f'num_sets_{i}')
        new_workout[i].add_set(sets)

        for set_num in range(sets):
            st.markdown(f"#### Set {set_num + 1}")
            weight_col, reps_col = st.columns(2)

            with weight_col:
                weight = st.number_input(f"Weight for Set {set_num + 1} (lbs)", min_value=0, step=5, key=f'weight_set_{i}_{set_num}')

            with reps_col:
                rep = st.number_input(f"Reps per Set {set_num + 1}", min_value=1, step=1, key=f'rep_set_{i}_{set_num}')

            new_workout[i].change_set_weight(set_num, weight)
            new_workout[i].change_set_rep(set_num, rep)

        st.markdown("---")
    st.session_state.new_workout = new_workout


def add_exercise_form():
    with st.form(key='add_exercise'):

        new_exercise = st.text_input("Enter the Exercise Here")
        new_exercise = new_exercise.lower().title()

        submit = st.form_submit_button("Add Exercise")

        if submit:
            query_response = (
                st.session_state.supabase
                .table("Exercises")
                .select("*")
                .eq("exercise", new_exercise).execute()
            )

            if query_response.error:
                st.error(f"An Error occurred: {query_response.error}")
            elif query_response.data:
                st.success("The Exercise is Already in the System")
            else:
                st.success("The Exercise is being Added Now")

                insert_response = (
                    st.session_state.supabase
                    .table("Exercises")  # Assuming the correct table is "Exercises"
                    .insert({"exercise": new_exercise})
                    .execute()
                )

                if insert_response.error:
                    st.error(f"An Error occurred: {insert_response.error}")
                else:
                    st.success("The Exercise has been Added")


st.title("Workout Tracker", )

tab1, tab2, tab3 = st.tabs(["Add Workout", "Add Exercise", "Finish Draft"])

with tab1:
    st.title("Create a Workout Here")

    render_workout_form()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.button('Add Exercise', key='add_exercise', on_click=add_an_exercise)

    with col2:
        st.button('Delete Exercise', key='delete_exercise', on_click=delete_an_exercise)

    with col3:
        if st.button("Save As Workout", key='save_workout'):
            save_workout()

    with col4:
        if st.button("Save As Draft", key='save_draft'):
            save_draft()

    if st.button("Testing", key='testing'):
        for exercise in st.session_state.new_workout:
            print(exercise)

with tab2:
    st.write("Do you have an exercise that you do not see in the workout creation tab? You can add it here.")

    add_exercise_form()


with tab3:
    st.title("Drafts")

    # Load Drafts from the database
    # Put them in a list in session state
    exercises = st.session_state.new_workout  # Tester while the database is not connected
    workouts = [exercises]

    for index, workout in enumerate(workouts):
        st.markdown(f"## Workout {index + 1}")
        for exercise_index, exercise in enumerate(workout):
            st.markdown(f"### {exercise.name} for {exercise.number_of_sets} sets")

            for set_index, exercise_sets in enumerate(exercise.sets):
                st.markdown(f"#### Set {set_index + 1}")
                st.markdown(f"##### {exercise_sets.weight} for {exercise_sets.reps} sets")


