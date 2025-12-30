import streamlit as st
from faq_data import faq

st.title("💬 FAQ Chatbot")

user_question = st.text_input("Ask a question:")

if user_question:
    found = False
    for question, answer in faq.items():
        if user_question.lower() in question.lower():
            st.success(answer)
            found = True
            break

    if not found:
        st.warning("Sorry, I don't have an answer for that.")
