from huggingface_hub import InferenceClient
import streamlit as st

st.header("Research Tool")

client = InferenceClient(
    model="google/flan-t5-base",
    token="your"
)

user_input = st.text_input("Enter your prompt")

if st.button("Search"):
    if user_input:
        response = client.text_generation(user_input)
        st.write(response)