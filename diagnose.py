# ==============================
# HealthBot: Simple Symptom Checker
# ==============================
# Author: [Your Name]
# Description:
#   This is a simple rule-based medical chatbot that infers possible 
#   diseases based on user-provided symptoms. It uses a small knowledge 
#   base of diseases, their symptoms, and an advice base to provide 
#   treatment suggestions. 
#
# Disclaimer: 
#   This program is for educational purposes only. 
#   It is not a substitute for professional medical advice. 
# ==============================

# ------------------------------
# Knowledge Base: Diseases & Symptoms
# ------------------------------
# Each disease is mapped to its list of symptoms. 
knowledge_base = {
    "flu": {"symptoms": ["fever", "cough", "sore_throat"]},
    "common_cold": {"symptoms": ["sneezing", "runny_nose", "mild_fever"]},
    "malaria": {"symptoms": ["fever", "chills", "sweating", "headache"]},
    "covid19": {"symptoms": ["fever", "cough", "shortness_of_breath", "loss_of_taste"]},
    "strep throat": {"symptoms": ["sore_throat", "swollen_lymph_nodes", "fever"]}
}

# ------------------------------
# Advice Base: Treatment Suggestions
# ------------------------------
# Each disease is mapped to simple advice for the user.
advice_base = {
    "flu": "Drink fluids, rest, and consult a doctor if symptoms worsen.",
    "common_cold": "Get rest, drink warm liquids, and use over-the-counter cold medicine.",
    "malaria": "Seek immediate medical attention as malaria requires prescription treatment.",
    "covid19": "Self-isolate and get tested immediately. Monitor your oxygen levels.",
    "strep_throat": "See a doctor for antibiotics as strep throat requires medical treatment."
}


# ------------------------------
# Function: Get User Symptoms
# ------------------------------
def get_user_symptoms():
    """
    Prompts the user to enter symptoms in a comma-separated format.
    Converts them into a clean, lowercase, underscore-separated list.
    
    Returns:
        symptoms (list): A list of cleaned symptom strings.
    """
    print("Welcome to HealthBot!")
    print("Enter your symptoms (comma-separated): ")
    user_input = input("Symptoms: ").lower()
    
    # Clean and normalize input (replace spaces with underscores)
    symptoms = [symptom.strip().replace(" ", "_") for symptom in user_input.split(",")]
    return symptoms


# ------------------------------
# Function: Infer Disease
# ------------------------------
def infer_disease(user_symptoms):
    """
    Infers possible diseases based on the user's symptoms.
    
    Rule:
        If ALL required symptoms for a disease exist in the user's input,
        that disease is considered a possible match.
    
    Args:
        user_symptoms (list): Symptoms entered by the user.
    
    Returns:
        possible_diseases (list): A list of matching diseases.
    """
    possible_diseases = []

    for disease, data in knowledge_base.items():
        required_symptoms = data["symptoms"]
        if all(symptom in user_symptoms for symptom in required_symptoms):
            possible_diseases.append(disease)

    return possible_diseases


# ------------------------------
# Function: Run Chatbot
# ------------------------------
def run_chatbot():
    """
    Runs the HealthBot:
        1. Collects user symptoms.
        2. Infers possible diseases.
        3. Prints matching diseases with advice.
    """
    user_symptoms = get_user_symptoms()
    diseases = infer_disease(user_symptoms)

    if diseases:
        print("\nBased on your symptoms, you might have:")
        for disease in diseases:
            # Format disease name (capitalize nicely for display)
            formatted_disease = disease.capitalize() if disease == "flu" else disease.replace("_", " ").title()
            print(f"- {formatted_disease}")
            print(f"  Advice: {advice_base[disease]}")
    else:
        print("\nNo matching disease found.")
        print("Please consult a healthcare professional.")


# ------------------------------
# Main Program Execution
# ------------------------------
run_chatbot()
