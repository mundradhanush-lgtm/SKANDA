from backend.ai.providers.gemini import gemini_request, gemini_computer_request
from backend.ai.providers.groq import groq_request, groq_computer_request

def ai_request(user_input, retrieved_relevent_history):
    try:
        response=gemini_request(user_input, retrieved_relevent_history)
        return response
    except Exception:
        try:
            response=groq_request(user_input, retrieved_relevent_history)
            return response
        except Exception:
            raise RuntimeError("All AI providers failed.")

def computer_ai_request(user_input, screenshot_text_representation):
    try:
        computer_response=gemini_computer_request(user_input, screenshot_text_representation)
        return computer_response
    except Exception:
        try:
            computer_response=groq_computer_request(user_input, screenshot_text_representation)
            return computer_response
        except Exception:
            raise RuntimeError("SKANDA cannot interact with the device right now.")