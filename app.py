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

    # Initialize conversation list in session state if not already present
    if 'conversation' not in st.session_state:
        st.session_state['conversation'] = []

    # Text input for user query
    user_input = st.text_input("Your question:", "")

    # On pressing Enter after input
    if st.session_state['conversation'] or user_input:
        if user_input:
            st.session_state['conversation'].append(f"You: {user_input}")
            response = get_response(user_input)
            st.session_state['conversation'].append(f"Assistant: {response}")
            user_input = ''  # Clear input box after processing the input

    # Display conversation history
    if st.session_state['conversation']:
        conversation_text = "\n".join(st.session_state['conversation'])
        st.text_area("Conversation", value=conversation_text, height=300, key="conversation_area", disabled=True)

if __name__ == "__main__":
    main()
