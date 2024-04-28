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

    # Handle input key for resetting the input field
    if 'input_key' not in st.session_state:
        st.session_state.input_key = 0

    # Send button
    send_button = st.button("Send")

    # Text input for user question. Increment key before displaying the input field if send_button was clicked.
    if send_button:
        st.session_state.input_key += 1  # Increment the input key to reset the text input field

    user_input = st.text_input("Type your question here:", key=f"input_{st.session_state.input_key}")

    if send_button and user_input:
        # Append user message to conversation
        st.session_state.conversation.append(("You", user_input))
        # Get AI response
        response = get_response(user_input)
        # Append AI response to conversation
        st.session_state.conversation.append(("Assistant", response))

    # Display messages in a container
    with st.container():
        for speaker, message in st.session_state.conversation:
            st.text(f"{speaker}: {message}")

if __name__ == "__main__":
    main()
