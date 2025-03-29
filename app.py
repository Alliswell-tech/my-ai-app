import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or input("Enter your Google AI API key: ")

# Configure with correct API version
genai.configure(api_key=GOOGLE_API_KEY)

def list_available_models():
    """Check which models are available with your API key"""
    print("Available models:")
    for model in genai.list_models():
        print(f"- {model.name}")

def chat_with_ai():
    try:
        # Try the newest model name first
        try:
            model = genai.GenerativeModel('gemini-1.5-pro-latest')
        except:
            model = genai.GenerativeModel('gemini-pro')
        
        print("🌟 Your AI Assistant (Press 'q' to quit) 🌟")
        chat = model.start_chat(history=[])
        
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'q':
                break
            
            response = chat.send_message(user_input)
            print("\nAI:", response.text, "\n")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        list_available_models()  # Show what models you can access

if __name__ == "__main__":
    chat_with_ai()
