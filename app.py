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

    # Sidebar for input
    with st.sidebar:
        user_input = st.text_input("Type your question here:", key="user_input")
        send_button = st.button("Send")

    # Initialize or extend conversation history in session state
    if 'conversation' not in st.session_state:
        st.session_state['conversation'] = []

    # Handle input and response
    if send_button and user_input:
        # Update conversation with user input
        st.session_state['conversation'].append(f"You: {user_input}")
        # Get response from the model
        response = get_response(user_input)
        # Update conversation with the model's response
        st.session_state['conversation'].append(f"Assistant: {response}")

    # Display conversation
    if st.session_state['conversation']:
        for message in st.session_state['conversation']:
            # Check who is speaking and format accordingly
            speaker, msg = message.split(":", 1)
            if speaker == 'You':
                st.text_area("", value=msg, height=50, key=message[:30], style={"text-align": "right", "color": "blue"})
            else:
                st.text_area("", value=msg, height=50, key=message[:30], style={"text-align": "left", "color": "green"})

if __name__ == "__main__":
    main()
