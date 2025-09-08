from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-1.5-pro')
result=model.invoke("government pilot secondary school is in which city of sindh?")
print(result.content)