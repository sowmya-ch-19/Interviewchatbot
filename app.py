import streamlit as st
import openai

# Set your OpenAI API key securely
openai.api_key = st.secrets['OPENAI_API_KEY']

def get_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant trained to ask insightful follow-up questions about interview experiences."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=150
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    st.title("Interactive Interview Experience Chatbot")
    
    # Initialize conversation in session state if it does not exist
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []
        initial_prompt = "Hello! Please describe your recent interview experience or ask any question about improving your interview skills."
        st.session_state.conversation.append(("Assistant", initial_prompt))

    # Display each message directly on the page
    for speaker, message in st.session_state.conversation:
        if speaker == "Assistant":
            st.info(f"{speaker}: {message}")  # Use st.info for assistant messages for visual distinction
        else:
            st.text(f"{speaker}: {message}")  # Use st.text for user messages

    # Input and button are placed at the bottom
    if 'input_key' not in st.session_state:
        st.session_state.input_key = 0

    user_input = st.text_input("Your response:", key=f"input_{st.session_state.input_key}")
    send_button = st.button("Send")

    # If the user sends a response
    if send_button and user_input:
        # Append user message to conversation
        st.session_state.conversation.append(("You", user_input))
        # Get AI response
        response = get_response(user_input)
        # Append AI response to conversation
        st.session_state.conversation.append(("Assistant", response))
        # Increment the input key to reset the text input field
        st.session_state.input_key += 1

if __name__ == "__main__":
    main()
