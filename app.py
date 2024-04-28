import streamlit as st
import openai

# Initialize session state for the conversation history if not already present
if 'history' not in st.session_state:
    st.session_state['history'] = []

def get_response(user_input):
    openai.api_key = st.secrets["OPENAI_API_KEY"]
    conversation_history = st.session_state['history']
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation_history + [{"role": "user", "content": user_input}],
            max_tokens=150
        )
        # Append both user and assistant messages to the history
        conversation_history.append({"role": "user", "content": user_input})
        conversation_history.append({"role": "assistant", "content": response.choices[0].message['content']})
        st.session_state['history'] = conversation_history
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

def load_css():
    st.markdown("""
        <style>
        .stTextInput>label {display: none;}
        .stButton>label {display: none;}
        .info, .success {
            border-radius: 10px;
            padding: 10px;
        }
        </style>
        """, unsafe_allow_html=True)

def main():
    load_css()
    st.title("Interactive Interview Experience Chatbot")
    ...



def main():
    st.title("Interactive Interview Experience Chatbot")

    # Define container for the chat display
    chat_container = st.container()
    input_container = st.container()

    with input_container:
        user_input = st.text_input("Type your message here:", key="chat_input")
        if st.button("Send"):
            if user_input:
                get_response(user_input)
                st.session_state.chat_input = ""  # Clear input field

    with chat_container:
        for i, message in enumerate(st.session_state['history']):
            # Differentiate user and assistant messages in layout
            if message['role'] == 'user':
                col1, col2 = st.columns([1, 5])
                with col1:
                    st.write("You:")
                with col2:
                    st.info(message['content'])
            elif message['role'] == 'assistant':
                col1, col2 = st.columns([5, 1])
                with col1:
                    st.success(message['content'])
                with col2:
                    st.write("Assistant:")

if __name__ == "__main__":
    main()
