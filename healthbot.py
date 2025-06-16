import ollama
#from safety import is_unsafe

SYSTEM_PROMPT = """
You are MediBot, a friendly AI assistant for general health information. 
Rules:
1. Explain medical concepts simply
2. NEVER give medical advice/diagnosis
3. For emergencies/serious symptoms, say: "Please see a doctor immediately"
4. Be reassuring and clear
5. Warn about medication interactions
"""

def health_chatbot():
    print("MediBot: Hi! I can answer general health questions (type 'quit' to exit)")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'quit':
            break
        
        response = ollama.chat(
            model='mistral',
            messages=[
                {'role': 'system', 'content': SYSTEM_PROMPT},
                {'role': 'user', 'content': user_input}
            ]
        )['message']['content']
        
        # Safety check
       # if is_unsafe(response):
        #    print("\nMediBot: I'm not qualified to answer that. Please consult a doctor.")
        #else:
        print(f"\nMediBot: {response}")

if __name__ == "__main__":
    health_chatbot()