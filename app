import openai

def setup_openai():
    openai.api_key = 'your-openai-api-key'

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
    print(safe_response)

def start_interview(interview_type):
    safe_print("Interviewer: Let's begin our discussion.")
    safe_print(f"Starting the {interview_type} interview.\n")
    introduction()
    if interview_type == 'job':
        discuss_experience()
        assess_skills()
        evaluate_company_fit()
        additional_questions()
    handle_candidate_questions()
    conclude_interview()

def introduction():
    name = input("Can you please tell me your name and a little about your background?\nYou: ")
    conversation_history.append({'role': 'user', 'content': name})

def get_user_input(prompt):
    user_input = input(f"Interviewer: {prompt}\nYou: ")
    conversation_history.append({'role': 'user', 'content': user_input})
    return user_input

def discuss_experience():
    last_role = get_user_input("What was your last role and what were your main responsibilities?")
    contributions = get_user_input("How did your role contribute to the overall goals of your previous company?")

def assess_skills():
    skills = get_user_input("What specific skills have you developed in your previous roles that are relevant to this job?")

def evaluate_company_fit():
    fit = get_user_input("How do you think you align with the culture of our company?")

def additional_questions():
    desire_for_job = get_user_input("Why do you want this job?")
    tough_problem = get_user_input("What's a tough problem you've solved?")
    biggest_challenge = get_user_input("What are the biggest challenges you have faced?")
    design_evaluation = get_user_input("Can you describe the best or worst designs you have seen?")
    product_improvement = get_user_input("Do you have ideas for improving an existing product?")
    work_preferences = get_user_input("How do you work best, as an individual and as part of a team?")
    skill_assets = get_user_input("Which of your skills or experiences would be assets in the role and why?")

def handle_candidate_questions():
    has_questions = get_user_input("Do you have any questions for us about the job or the company?")
    if has_questions.lower() in ['yes', 'y']:
        continue_questions()
    else:
        safe_print("Interviewer: No worries! Let's proceed.")

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
    print("Interviewer: Here are some questions you might consider asking:\n" + "\n".join(f"{i+1}. {q}" for i, q in enumerate(suggested_questions)))
    index = int(get_user_input("Please select the number of the question you would like to ask:")) - 1
    safe_print(f"You: {suggested_questions[index]}")
    safe_print(f"Interviewer: {answers[index]}")  # Provide the answer
    additional = get_user_input("Do you have any more questions?")
    if additional.lower() in ['no', 'no more questions', "that's all"]:
        safe_print("Interviewer: Thank you for your questions.")
    else:
        continue_questions()

def conclude_interview():
    safe_print("Interviewer: Thank you for your time. We will get back to you soon. Have a great day!")

conversation_history = []
setup_openai()

if __name__ == "__main__":
    interview_type = input("Enter interview type (job/user_research/feedback): ")
    start_interview(interview_type)
