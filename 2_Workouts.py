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
            col1, col2 = st.columns(2)

            with col1:
                weight = st.number_input(f"Weight for Set {set_num + 1} (lbs)", min_value=0, step=5, key=f'weight_set_{i}_{set_num}')

            with col2:
                rep = st.number_input(f"Reps per Set {set_num + 1}", min_value=1, step=1, key=f'rep_set_{i}_{set_num}')

            new_workout[i].change_set_weight(set_num, weight)
            new_workout[i].change_set_rep(set_num, rep)

        st.markdown("---")
    st.session_state.new_workout = new_workout


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

with tab2:
    st.write("Do you have an exercise that you do not see in the workout creation tab? You can add it here.")


with tab3:
    st.title("Drafts")

