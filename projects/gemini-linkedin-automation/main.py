import google.genai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ==========================================
# Generate LinkedIn message with Gemini API
# ==========================================
gemini_api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=gemini_api_key)

prompt = "Write a concise, professional LinkedIn connection message to a Senior Data Scientist."
response = client.models.generate_content(
    model="gemini-2.5-flash", contents=prompt  # free, fast, excellent for text
)
generated_message = response.text.strip()

print("Generated LinkedIn message:")
print(generated_message)
