import streamlit as st
import openai

# Set your OpenAI API key securely
openai.api_key = st.secrets['OPENAI_API_KEY']

def get_response(user_input, chat_history):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_history + [{"role": "user", "content": user_input}],
            max_tokens=150
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    st.title("Interview Prep Chatbot")

    # Initialize conversation list in session state if not already present
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = [
            {"role": "system", "content": "You are a helpful assistant trained to provide guidance on interview preparation, answer questions about interview experiences, and offer tips on interview techniques."}
        ]

    # Text input for user query
    user_input = st.text_input("How can I help you prepare for your interview?", "")

    # Process the input when the user submits a question
    if user_input:
        st.session_state['chat_history'].append({"role": "user", "content": user_input})
        response = get_response(user_input, st.session_state['chat_history'])
        st.session_state['chat_history'].append({"role": "assistant", "content": response})
        st.session_state['conversation'] = [f"{chat['role']}: {chat['content']}" for chat in st.session_state['chat_history']]
        user_input = ''  # Clear input box after processing the input

    # Display conversation history
    if 'conversation' in st.session_state:
        conversation_text = "\n".join(st.session_state['conversation'])
        st.text_area("Conversation", value=conversation_text, height=300, key="conversation_area", disabled=True)

if __name__ == "__main__":
    main()
