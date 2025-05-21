#Knowledge base
knowledge_base = {
    "flu": {"symptoms": ["fever", "cough", "sore_throat"]},
    "common_cold": {"symptoms": ["sneezing", "runny_nose", "mild_fever"]},
    "malaria": {"symptoms": ["fever", "chills", "sweating", "headache"]},
    "covid19": {"symptoms": ["fever", "cough", "shortness_of_breath", "loss_of_taste"]},
    "strep throat": {"symptoms": ["sore_throat", "swollen_lymph_nodes", "fever"]}
}

# Advice base 
advice_base = {
    "flu": "Drink fluids, rest, and consult a doctor if symptoms worsen.",
    "common_cold": "Get rest, drink warm liquids, and use over-the-counter cold medicine.",
    "malaria": "Seek immediate medical attention as malaria requires prescription treatment.",
    "covid19": "Self-isolate and get tested immediately. Monitor your oxygen levels.",
    "strep_throat": "See a doctor for antibiotics as strep throat requires medical treatment."
}

def get_user_symptoms():
    print("Welcome to HealthBot!")
    print("Enter your symptoms (comma-separated): ")
    user_input = input("Symptoms: ").lower()
    
    # Clean and split the input
    symptoms = [symptom.strip().replace(" ", "_") for symptom in user_input.split(",")]
    return symptoms

def infer_disease(user_symptoms):
    possible_diseases = []

    # Loop through the knowledge base and apply FOL-style rule
    for disease, data in knowledge_base.items():
        required_symptoms = data["symptoms"]
        # Check if all required symptoms exist in user input
        if all(symptom in user_symptoms for symptom in required_symptoms):
            possible_diseases.append(disease)

    return possible_diseases

def run_chatbot():
    user_symptoms = get_user_symptoms()
    diseases = infer_disease(user_symptoms)

    if diseases:
        print("\nBased on your symptoms, you might have:")
        for disease in diseases:
            formatted_disease = disease.capitalize() if disease == "flu" else disease.replace("_", " ").title()
            print(f"- {formatted_disease}")
            print(f"  Advice: {advice_base[disease]}")
    else:
        print("\nNo matching disease found.")
        print("Please consult a healthcare professional.")

run_chatbot()