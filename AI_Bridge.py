from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()
API_KEY = os.getenv("Gemini_API_KEY")

genai.configure(api_key=API_KEY)


model = genai.GenerativeModel('gemini-1.5-flash')

with open("today_cves.txt", "r", encoding="utf-8") as file:
    data = file.read()

query = f"{data}This is list of CVES. find me weakpoints in bullets and what algorithms like SQLi can be used to exploit them. mention weekpoints and algorithms seperatly in one word lists"

try:
    response = model.generate_content(query)
    print("Gemini Response:\n", response.text)
    print("\n\n")
    with open("AI_Response.txt", "w", encoding="utf-8") as file:
        file.write(response.text)

except Exception as e:
    print("Error while querying Gemini API:", e)