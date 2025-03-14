import streamlit as st
import random

def quiz_game():
    st.title("🧠 Quiz Game 🎯")
    
    questions = [
        ("What is the capital of France?", {"A": "London", "B": "Paris", "C": "Berlin", "D": "Madrid"}, "B"),
        ("What is 5 + 7?", {"A": "10", "B": "12", "C": "15", "D": "9"}, "B"),
        ("Who developed the theory of relativity?", {"A": "Isaac Newton", "B": "Galileo Galilei", "C": "Albert Einstein", "D": "Nikola Tesla"}, "C"),
        ("What is the boiling point of water?", {"A": "90°C", "B": "100°C", "C": "110°C", "D": "120°C"}, "B"),
        ("Which planet is known as the Red Planet?", {"A": "Venus", "B": "Mars", "C": "Jupiter", "D": "Saturn"}, "B")
    ]
    
    if "score" not in st.session_state:
        st.session_state.score = 0
        st.session_state.question_index = 0
        st.session_state.feedback = ""
        st.session_state.submitted = False
    
    if st.session_state.question_index < len(questions):
        question, options, correct_answer = questions[st.session_state.question_index]
        st.write(f"### {question}")
        
        options_display = {key: f"{key}) {value}" for key, value in options.items()}
        user_answer = st.radio("Choose an option:", list(options_display.values()), key=f"question_{st.session_state.question_index}")
        
        if st.button("Submit") and user_answer:
            selected_option = user_answer[0]  # Extract the first character (A, B, C, or D)
            if selected_option == correct_answer:
                st.session_state.feedback = f"✅ Correct! 🎉 {selected_option}) {options[selected_option]}"
                st.session_state.score += 1
            else:
                st.session_state.feedback = f"❌ Incorrect! You chose {selected_option}) {options[selected_option]}. The correct answer is {correct_answer}) {options[correct_answer]}."
            
            st.session_state.submitted = True
            st.rerun()
        
        if st.session_state.submitted:
            st.write(st.session_state.feedback)
            if st.button("Next Question"):
                st.session_state.question_index += 1
                st.session_state.submitted = False
                st.session_state.feedback = ""
                st.rerun()
    else:
        st.write(f"## 🎯 Final Score: {st.session_state.score}/{len(questions)} 🎯")
        if st.button("Restart Quiz"):
            st.session_state.score = 0
            st.session_state.question_index = 0
            st.session_state.feedback = ""
            st.session_state.submitted = False
            st.rerun()

quiz_game()
