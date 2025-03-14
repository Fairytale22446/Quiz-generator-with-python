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
    
    random.shuffle(questions)
    
    if "score" not in st.session_state:
        st.session_state.score = 0
        st.session_state.question_index = 0
        st.session_state.user_answer = None
        st.session_state.show_result = False
    
    if st.session_state.question_index < len(questions):
        question, options, correct_answer = questions[st.session_state.question_index]
        st.write(f"### {question}")
        
        options_display = {key: f"{key}) {value}" for key, value in options.items()}
        user_answer = st.radio("Choose an option:", list(options_display.values()), index=None, key=f"question_{st.session_state.question_index}")
        
        if st.button("Submit"):
            if user_answer:
                selected_option = user_answer[0]
                st.session_state.user_answer = selected_option
                st.session_state.show_result = True
                st.rerun()
            else:
                st.warning("⚠️ Please select an option before submitting!")
        
        if st.session_state.show_result:
            selected_option = st.session_state.user_answer
            if selected_option == correct_answer:
                st.success(f"✅ Correct! 🎉 {selected_option}) {options[selected_option]}")
                st.session_state.score += 1
            else:
                st.error(f"❌ Incorrect! You chose {selected_option}) {options[selected_option]}. The correct answer is {correct_answer}) {options[correct_answer]}.")
            
            if st.button("Next Question"):
                st.session_state.question_index += 1
                st.session_state.user_answer = None
                st.session_state.show_result = False
                st.rerun()
    else:
        st.write(f"## 🎯 Final Score: {st.session_state.score}/{len(questions)} 🎯")
        if st.button("Restart Quiz"):
            st.session_state.score = 0
            st.session_state.question_index = 0
            st.session_state.user_answer = None
            st.session_state.show_result = False
            st.rerun()

quiz_game()