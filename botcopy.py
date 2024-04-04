import streamlit as st
from collections import Counter

# Define the questionnaire with VARK categories tagged properly in the options.
questions = {
    "If you are unsure whether a word should be spelled 'dependent' or 'dependant', would you:": [
        "Visual: Write both words on paper and choose one.",
        "Auditory: Think about how each word sounds and choose one.",
        "Read/Write: Find it in a dictionary.",
        "Kinesthetic: See the words in your mind and choose by the way they look."
    ],
    "I like websites that have:": [
        "Visual: Interesting design and visual features.",
        "Auditory: Audio channels where I can hear music, radio programs, or interviews.",
        "Read/Write: Interesting written descriptions, lists, and explanations.",
        "Kinesthetic: Things I can click on, shift, or try."
    ],
    "A group of tourists wants to learn about the parks or wildlife reserves in your area. You would:": [
        "Visual: Show them internet pictures, photographs, or picture books.",
        "Auditory: Talk about or arrange a talk for them about parks or wildlife reserves.",
        "Read/Write: Give them a book or pamphlets about the parks or wildlife reserves.",
        "Kinesthetic: Take them to a park or wildlife reserve and walk with them."
    ]
}

knowledge_question = "My current level of knowledge on the subject is:"

knowledge_options = [
    "Novice - You're just starting out. It's like you've just planted a seed and are waiting for it to sprout.",
    "Competent - You've got some experience. It's like your seed has sprouted and is starting to grow.",
    "Proficient - You're really getting the hang of it. It's like your plant has grown and is starting to bloom.",
    "Expert - You're a pro. It's like your plant is fully grown and flourishing.",
    "Master - You're at the top. It's like not only do you have a beautiful, fully-grown plant, but you're also able to create new varieties."
]

def calculate_vark_results(answers):
    # Tally the VARK type selected in each answer.
    vark_results = Counter(answer.split(":")[0] for answer in answers.values() if ":" in answer)  # Only include answers with a VARK tag

    # Classify learning preference based on the counts of each VARK type.
    modal_counts = sum(count > 0 for count in vark_results.values())
    
    learning_classification = "Single Modal"  # Default classification
    if modal_counts == 4:
        learning_classification = "Quad-modal"
    elif modal_counts == 3:
        learning_classification = "Tri-modal"
    elif modal_counts == 2:
        learning_classification = "Bi-modal"
    
    return vark_results, learning_classification

def main():
    st.title("VARK Questionnaire")
    st.write("## Instructions: Consider how you generally learn best. Choose ONE answer per question.")

    answers = {}

    # Display VARK questions and record answers.
    for question, options in questions.items():
        answer = st.radio(question, options)
        answers[question] = answer

    # Separately handle the knowledge question to ensure it doesn't affect VARK modal calculation
    knowledge_answer = st.selectbox(knowledge_question, knowledge_options)

    if st.button("Submit"):
        vark_results, learning_classification = calculate_vark_results(answers)

        # Display learning preference classification and knowledge level.
        st.write(f"Your learning preference classification is: {learning_classification}")
        
        if learning_classification != "Single Modal":
            preferred_styles = ', '.join(k for k, v in vark_results.items() if v > 0)
            st.write(f"You prefer the following learning styles: {preferred_styles}")
        else:
            primary_preference = max(vark_results, key=vark_results.get, default="N/A")
            st.write(f"Your primary learning preference is: {primary_preference}")
        
        st.write(f"Your current level of knowledge on the subject is: {knowledge_answer}")

if __name__ == "__main__":
    main()


## https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4190729/pdf/jcdr-8-GC01.pdf