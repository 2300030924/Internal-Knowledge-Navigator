import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyAuSN2HIPf1Dt44J6PROrl3efgNOyh_D_Y"))

model = genai.GenerativeModel("gemini-2.5-flash")
response = model.generate_content("Hello, Gemini! Are you working?")
print(response.text)
