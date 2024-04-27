import streamlit as st

def response_filter(response):
    # Check for inappropriate content
    keywords = ["openai", "gpt", "model", "api"]
    for keyword in keywords:
        if keyword in response.lower():
            return "Let's keep our focus on your interview."
    return response

def safe_print(response):
    # Ensure all responses are appropriate
    safe_response = response_filter(response)
    return safe_response

def introduction():
    name = st.text_input("Can you please tell me your name and a little about your background?")
    if name:
        conversation_history.append({'role': 'user', 'content': name})
    return name

def get_user_input(prompt, key):
    user_input = st.text_input(f"Interviewer: {prompt}", key=key)
    if user_input:
        conversation_history.append({'role': 'user', 'content': user_input})
    return user_input

def discuss_experience():
    last_role = get_user_input("What was your last role and what were your main responsibilities?", key='last_role')
    contributions = get_user_input("How did your role contribute to the overall goals of your previous company?", key='contributions')

def assess_skills():
    skills = get_user_input("What specific skills have you developed in your previous roles that are relevant to this job?", key='skills')

def evaluate_company_fit():
    fit = get_user_input("How do you think you align with the culture of our company?", key='fit')

def additional_questions():
    questions = ["Why do you want this job?", "What's a tough problem you've solved?", "What are the biggest challenges you have faced?",
                 "Can you describe the best or worst designs you have seen?", "Do you have ideas for improving an existing product?",
                 "How do you work best, as an individual and as part of a team?", "Which of your skills or experiences would be assets in the role and why?"]
    responses = {q: get_user_input(q, key=f'q{idx}') for idx, q in enumerate(questions)}

def handle_candidate_questions():
    has_questions = get_user_input("Do you have any questions for us about the job or the company?", key='has_questions')
    if has_questions.lower() in ['yes', 'y']:
        continue_questions()
    else:
        st.write("Interviewer: No worries! Let's proceed.")

def continue_questions():
    suggested_questions = [
        "How large is your team?",
        "What does your dev cycle look like? Do you do waterfall/sprints/agile?",
        "Are rushes to deadlines common? Or is there flexibility?",
        "How are decisions made in your team?",
        "How many meetings do you have per week?",
        "Do you feel your work environment helps you concentrate?",
        "What are you working on?",
        "What do you like about it?",
        "What is the work life like?",
        "How is the work/life balance?"
    ]
    answers = [
        "Our team consists of 10 developers and 3 project managers.",
        "We primarily use agile methodologies with two-week sprints.",
        "We try to maintain a flexible schedule, but occasional deadline rushes can occur.",
        "Decisions are made collaboratively in our team, often after brainstorming and consensus.",
        "We usually have around three meetings per week to align on our goals and progress.",
        "Yes, we have dedicated quiet zones and ergonomic setups to help everyone concentrate.",
        "Currently, we're working on a new mobile application aimed at improving user engagement.",
        "I enjoy the creativity involved in design and the satisfaction of seeing users enjoy our products.",
        "The work life at our company is dynamic and exciting but also demanding at times.",
        "We strive for a balanced work/life approach, encouraging team members to take time off as needed."
    ]
    question_index = st.selectbox("Select a question to ask:", list(range(len(suggested_questions))), format_func=lambda x: suggested_questions[x])
    if st.button("Ask"):
        st.write(f"You: {suggested_questions[question_index]}")
        st.write(f"Interviewer: {answers[question_index]}")
        if st.button("Done with questions", key='done_questions'):
            st.write("Interviewer: Thank you for your questions.")


def conclude_interview():
    st.write("Interviewer: Thank you for your time. We will get back to you soon. Have a great day!")

conversation_history = []

def main():
    st.title("Interview Chatbot")
    introduction_completed = introduction()
    if introduction_completed:
        interview_type = st.radio("Select the type of interview", ('job', 'user_research', 'feedback'))
        if interview_type == 'job':
            discuss_experience()
            assess_skills()
            evaluate_company_fit()
            additional_questions()
        handle_candidate_questions()
        conclude_interview()

if __name__ == "__main__":
    main()
