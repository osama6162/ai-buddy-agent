import requests

def query_ollama_llama(prompt):
    try:
        res = requests.post("http://localhost:11434/api/generate", json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        })
        data = res.json()
        return data.get("response", "[No response from LLaMA]")
    except Exception as e:
        print("[Ollama API error]", str(e))
        raise

def classify_email(email_data, indicators):
    text = f"""
You are AI Buddy, a phishing analysis expert.
Classify the following email as phishing, spam, or safe.

Subject: {email_data['subject']}
From: {email_data['from']}
To: {email_data['to']}

Body:
{email_data['body']}

Indicators:
URLs: {indicators['urls']}
Domains: {indicators['domains']}
IPs: {indicators['ips']}

Explain your decision.
"""
    return query_ollama_llama(text)

