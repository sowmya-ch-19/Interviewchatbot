import streamlit as st
import openai

# Set your OpenAI API key securely
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Adjust the model as needed
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
    st.title("Interactive Interview Experience")

    # Create a form for user input
    with st.form(key='user_interaction'):
        user_input = st.text_input("Describe your interview experience or ask a question about improving interview skills:", "")
        submit_button = st.form_submit_button("Submit")

    if submit_button and user_input:
        response = get_response(user_input)
        conversation_text = f"You: {user_input}\nAssistant: {response}"
        st.text_area("Conversation", value=conversation_text, height=200, key="conversation")

if __name__ == "__main__":
    main()
