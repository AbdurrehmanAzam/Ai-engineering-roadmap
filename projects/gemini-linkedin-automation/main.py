import google.genai as genai
import os
import time
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=gemini_api_key)

prompt = "Write a concise, professional LinkedIn connection message to a Senior Data Scientist."

max_retries = 3
for attempt in range(1, max_retries + 1):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=prompt
        )
        generated_message = response.text.strip()
        print("Generated LinkedIn message:")
        print(generated_message)
        break  # success, exit the retry loop
    except genai.errors.ServerError:
        if attempt < max_retries:
            print(f"Server busy – retrying (attempt {attempt}/{max_retries})...")
            time.sleep(2)
        else:
            print("Server still busy after 3 retries. Try again later.")
