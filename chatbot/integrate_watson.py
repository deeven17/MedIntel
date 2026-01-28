from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import requests  # To call Flask API
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Watson credentials from environment variables
WATSON_API_KEY = os.getenv('WATSON_API_KEY', 'YOUR_WATSON_API_KEY')
WATSON_URL = os.getenv('WATSON_URL', 'YOUR_WATSON_URL')
WATSON_ASSISTANT_ID = os.getenv('WATSON_ASSISTANT_ID', 'YOUR_ASSISTANT_ID')

# Check if credentials are properly configured
if WATSON_API_KEY == 'YOUR_WATSON_API_KEY' or WATSON_URL == 'YOUR_WATSON_URL':
    print("⚠️ WatsonX.ai credentials not configured. Please set environment variables.")
    print("   Required: WATSON_API_KEY, WATSON_URL, WATSON_ASSISTANT_ID")
    watson_available = False
else:
    watson_available = True

# Initialize Watson Assistant if credentials are available
if watson_available:
    try:
        authenticator = IAMAuthenticator(WATSON_API_KEY)
        assistant = AssistantV2(version='2021-06-14', authenticator=authenticator)
        assistant.set_service_url(WATSON_URL)
        
        # Create session
        session_response = assistant.create_session(assistant_id=WATSON_ASSISTANT_ID)
        session = session_response.get_result()['session_id']
        print("✅ WatsonX.ai Assistant initialized successfully")
    except Exception as e:
        print(f"❌ Error initializing WatsonX.ai Assistant: {e}")
        watson_available = False
        session = None
else:
    assistant = None
    session = None

def send_message(message):
    """
    Send message to Watson Assistant with fallback logic
    """
    if not watson_available or assistant is None or session is None:
        # Fallback response when Watson is not available
        if 'heart' in message.lower():
            return "I notice you're asking about heart-related concerns. While my AI assistant is currently unavailable, I recommend consulting with a healthcare professional for accurate heart health assessment."
        elif 'alzheimer' in message.lower() or 'dementia' in message.lower():
            return "I understand you have questions about Alzheimer's disease. For proper cognitive assessment and guidance, please consult with a neurologist or healthcare provider."
        else:
            return "I'm here to help with your health questions, but my advanced AI assistant is currently unavailable. For specific medical concerns, please consult with a healthcare professional."
    
    try:
        # Send message to Watson Assistant
        response = assistant.message(
            assistant_id=WATSON_ASSISTANT_ID, 
            session_id=session, 
            input={'text': message}
        ).get_result()
        
        # Extract the response text
        if 'output' in response and 'generic' in response['output'] and len(response['output']['generic']) > 0:
            watson_response = response['output']['generic'][0]['text']
            
            # Check for medical conditions and provide additional info
            if 'heart' in message.lower():
                # Call heart prediction API
                try:
                    api_resp = requests.post('http://localhost:8000/predict/heart', 
                                            json={'symptoms': message.split()}, 
                                            timeout=10)
                    if api_resp.status_code == 200:
                        prediction = api_resp.json()
                        risk_info = f"\n\nHeart Risk Assessment: {prediction.get('risk_level', 'Unknown')} ({prediction.get('risk_percentage', 0)}%)"
                        return watson_response + risk_info
                except Exception as e:
                    print(f"❌ Error calling heart prediction API: {e}")
                    return watson_response + "\n\nNote: Heart risk assessment temporarily unavailable."
            
            return watson_response
        else:
            return "I received your message but had trouble generating a response. Please try again."
            
    except Exception as e:
        print(f"❌ Error communicating with Watson Assistant: {e}")
        
        # Fallback response
        if 'heart' in message.lower():
            return "I'm experiencing technical difficulties with my AI assistant. For heart-related concerns, please consult with a healthcare professional."
        elif 'alzheimer' in message.lower() or 'dementia' in message.lower():
            return "I'm experiencing technical difficulties with my AI assistant. For cognitive health concerns, please consult with a neurologist or healthcare provider."
        else:
            return "I'm experiencing technical difficulties right now. Please try again later or consult with a healthcare professional for medical concerns."

def reset_session():
    """Reset the Watson Assistant session"""
    global session
    if watson_available and assistant is not None:
        try:
            # Delete old session
            if session:
                assistant.delete_session(assistant_id=WATSON_ASSISTANT_ID, session_id=session)
            
            # Create new session
            session_response = assistant.create_session(assistant_id=WATSON_ASSISTANT_ID)
            session = session_response.get_result()['session_id']
            print("✅ Watson session reset successfully")
            return True
        except Exception as e:
            print(f"❌ Error resetting Watson session: {e}")
            return False
    return False

# Example usage and test function
def test_watson_integration():
    """Test the Watson integration"""
    test_messages = [
        "Hello, I need help with heart health",
        "What are the symptoms of Alzheimer's disease?",
        "I have chest pain, what should I do?"
    ]
    
    print("🧪 Testing WatsonX.ai Integration...")
    for msg in test_messages:
        print(f"\n📤 User: {msg}")
        response = send_message(msg)
        print(f"🤖 Assistant: {response}")

if __name__ == "__main__":
    test_watson_integration()