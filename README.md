# HealthBot - Symptom Checker

HealthBot is a simple **rule-based medical chatbot** written in Python.  
It asks the user for symptoms, checks them against a small knowledge base,  
and suggests possible diseases with basic advice.  

**Disclaimer:** This project is for **educational purposes only** and should not be used as a substitute for professional medical advice.  

---

## Features
- Accepts multiple symptoms as input.
- Matches symptoms against a knowledge base of common illnesses.
- Provides basic advice for each possible disease.
- Covers **Flu, Common Cold, Malaria, COVID-19, and Strep Throat**.

---

## How It Works
1. The program asks the user to input symptoms (comma-separated).  
   Example:
   Symptoms: fever, cough, sore throat

3. It cleans and standardizes the input (e.g., `"sore throat"` → `"sore_throat"`).  

4. It compares the input symptoms with its **knowledge base**.  
If **all required symptoms** of a disease are present, it suggests that disease.  

5. The program provides advice from its **advice base**.  

---

## Project Structure
├── diagnose.py # Main chatbot script

├── README.md # Project documentation


---

## Running the Program
Make sure you have Python installed.  

Run the chatbot with:
```bash
python diagnose.py
```
```
Welcome to HealthBot!
Enter your symptoms (comma-separated): 
Symptoms: fever, cough, sore throat

Based on your symptoms, you might have:
- Flu
  Advice: Drink fluids, rest, and consult a doctor if symptoms worsen.
```


