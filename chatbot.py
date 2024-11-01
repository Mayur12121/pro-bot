# app.py
import os
import streamlit as st
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Model configuration
generation_config = {
    "temperature": 0.9,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 10000,
}

# Initialize model
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction=
    
    """
    
    you are a chatbot on my website whose work is to give informative about our web project
    which is intestine cancer detection using cnn and flask framework is used to build it, it uses colonoscopy images and predicts if it is cancerous or non cancerous using machine learning,
    this project is made by Mayur, Prathamesh, Rushikesh and himanshu and is a collaborative work of them.
    provide answers related to the project and basic topics like what is cancer, how to prevent and early detection.
    if someone asks very irrelevent or bad questions tell them that the question is not related and ask for some project related question.
    
    """
)

# Initialize chat history
if "history" not in st.session_state:
    st.session_state["history"] = []

st.title("Proffessional Chatbot")

# Input for the user's question
user_input = st.text_input("Ask any question:")

# When the user clicks the "Send" button
if st.button("Send") and user_input:
    # Create a chat session with history
    chat_session = model.start_chat(history=st.session_state["history"])
    
    # Send the user's message to the chat session
    response = chat_session.send_message(user_input)
    model_response = response.text
    
    # Update history with user and model responses
    st.session_state["history"].append({"role": "user", "parts": [user_input]})
    st.session_state["history"].append({"role": "model", "parts": [model_response]})

    # Display the model's response
    st.write("Assistant:", model_response)
    st.markdown("<br><hr><br>", unsafe_allow_html=True)
# Display the chat history
st.write("Chat History:")
for message in st.session_state["history"]:
    if message["role"] == "user":
        st.write("You:", message["parts"][0])
    elif message["role"] == "model":
        st.write("Assistant:", message["parts"][0])
    st.write("")  
    
