import os
import streamlit as st
import openai

# Set your OpenAI API key securely
openai.api_key = st.secrets['OPENAI_API_KEY']

def main():
    st.title("Interactive Interview Experience Chatbot")

    # Initialize conversation history if not already present
    if 'history' not in st.session_state:
        st.session_state['history'] = []

    # Text input for user message
    user_input = st.text_input("Type your message here:", key="user_input")

    # Button to submit new message
    if st.button("Send"):
        if user_input:  # Ensure the user has typed something
            # Add user's input to history
            st.session_state['history'].append(f"You: {user_input}")
            
            # Get the model's response
            response = get_response(user_input)
            st.session_state['history'].append(f"Assistant: {response}")
            
            # Clear the input box after sending
            st.session_state['user_input'] = ""

    # Display conversation history
    for message in st.session_state['history']:
        st.text_area("", value=message, height=100, disabled=True, key=message[:15])

if __name__ == "__main__":
    main()
