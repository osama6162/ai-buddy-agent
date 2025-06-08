from categorize import classify_email, query_ollama_llama
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from eml_parser import parse_eml
#from indicators import extract_urls, extract_domains, extract_ips
from pydantic import BaseModel
import tempfile
#from eml_parser import parse_eml
from indicators import extract_indicators


last_uploaded_email = {}

app = FastAPI(title="AI Buddy – Your AI Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def index():
    return {"message": "Welcome to AI Buddy. Use /docs or frontend to chat/upload .eml"}

@app.post("/analyze-eml")
def analyze_eml(file: UploadFile = File(...)):
    email_data = parse_eml(file.file)
    indicators = extract_indicators(email_data)
    classification = classify_email(email_data, indicators)  # ← This must come before use

    global last_uploaded_email
    last_uploaded_email = {
        "filename": file.filename,
        "classification": classification,
        "indicators": indicators,
        "raw_body": email_data['body'],
        "subject": email_data['subject']
    }

    return {
        "classification_result": classification,
        "indicators": indicators
    }


class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(chat: ChatRequest):
    try:
        global last_uploaded_email
        context = ""

        if last_uploaded_email:
            context = f"""
You previously analyzed an email titled "{last_uploaded_email['subject']}".
The classification was: {last_uploaded_email['classification']}.
Indicators extracted:
- URLs: {', '.join(last_uploaded_email['indicators']['urls']) or 'None'}
- Domains: {', '.join(last_uploaded_email['indicators']['domains']) or 'None'}
- IPs: {', '.join(last_uploaded_email['indicators']['ips']) or 'None'}

The body of the email was:
{last_uploaded_email['raw_body']}

You can now answer follow-up questions based on this analysis.
"""

        prompt = f"""
You are AI Buddy, a Cyber Security assistant. {context}
User: {chat.message}
AI Buddy:
"""

        print("[Prompt to Ollama]:", prompt)
        response = query_ollama_llama(prompt)
        return {"response": response.strip()}

    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"response": "AI Buddy backend error."}

