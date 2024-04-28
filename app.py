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

    # Text input for user question
    user_input = st.text_input("Type your question here:", key="user_input", on_change=None)

    # Send button
    send_button = st.button("Send")

    # Container to display the conversation
    chat_container = st.container()

    if send_button and user_input:
        # Append user message to conversation
        st.session_state.conversation.append(("You", user_input))
        # Get AI response
        response = get_response(user_input)
        # Append AI response to conversation
        st.session_state.conversation.append(("Assistant", response))
        # Clear input
        st.session_state.user_input = ""

    # Display messages
    for speaker, message in st.session_state.conversation:
        if speaker == "You":
            chat_container.write(f"You: {message}", unsafe_allow_html=True)
        else:
            chat_container.write(f"Assistant: {message}", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
