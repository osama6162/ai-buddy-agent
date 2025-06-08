🛡️ AI Buddy – Phishing Analysis Assistant

🔍 Overview

AI Buddy is an intelligent, offline-first, phishing email analysis assistant designed for security analysts. It combines the reasoning power of LLaMA (via Ollama) with file analysis, indicator extraction, and an intuitive chat interface. This tool allows SOC analysts and cybersecurity professionals to upload .eml email files, extract indicators, classify the message as phishing/spam/safe, and interact with an AI assistant for deeper threat context.

🎯 Key Benefits

✅ Private & Offline: No cloud APIs, runs fully on your system.

🤖 Local LLaMA Reasoning: Use llama3 model through Ollama to classify threats.
📎 IOC Extraction: Automatically extracts URLs, domains, and IPs from email content.
💬 Conversational Agent: Built-in chat powered by the same local AI model.
📤 EML Support: Upload .eml files for in-depth parsing and evaluation.
🌐 Modern Web UI: Responsive interface built with React and Tailwind CSS.

⚙️ Tech Stack
Backend >> Python 3.13, FastAPI
LLM Model >> LLaMA 3 via Ollama
Frontend >> React, Tailwind CSS
Parsing >> .eml email files
Deployment >> Kali Linux

📁 Project Structure

/root/ai-buddy-agent/
├── backend/
│   ├── main.py              # FastAPI backend API
│   ├── categorize.py        # Runs Ollama LLaMA3 to classify emails
│   ├── eml_parser.py        # Parses uploaded .eml files
│   ├── indicators.py        # Extracts URLs, domains, IPs from content
│   ├── .venv/               # Python virtual environment
│   ├── run_backend.sh       # Script to run backend manually
│   └── requirements.txt     # Backend Python dependencies
│
├── frontend/
│   ├── public/              # Static files
│   └── src/
│       ├── App.js           # Main UI component
│       ├── App.css          # Global styling (dark/light)
│       ├── ChatBox.js       # Chat interface with LLaMA
│       ├── FileUploader.js  # Email upload + results
│       └── index.js         # React entry point
│
└── systemd/
    ├── ai-buddy-backend.service   # FastAPI backend systemd service
    └── ai-buddy-frontend.service  # React frontend systemd service

Real Project Test Case:
1. 1st Uploaded email for AI Buddy help to analyze the email
![Test Email](https://github.com/user-attachments/assets/5107e9d0-e9c2-434b-b3ef-0da2eb4e8ddd)

🧠 AI Reasoning Example

A typical response from AI Buddy after analyzing an email:
"After analyzing the email, I classify it as phishing. It contains suspicious links, mismatched sender domains, and an urgent request for credential confirmation."

2. Then Started to chat with the AI buddy for further assistance
![AI Buddy chatting](https://github.com/user-attachments/assets/f2c35fe1-f22e-4afc-97bb-6aacd20f3474)


🚀 Installation & Startup

1️⃣ Backend Setup (FastAPI + Ollama)

cd ~/ai-buddy-agent/backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

Note: Make sure you have Ollama installed and have pulled the llama3 model

2️⃣ Frontend Setup (React)

cd ~/ai-buddy-agent/frontend
npm install
npm run build

3️⃣ Serve Frontend

serve -s build -l 9001
Or via systemd:
sudo systemctl restart ai-buddy-frontend

🧪 API Endpoints for Testing

# Check backend
curl -X POST http://localhost:9002/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hi"}'

# Upload .eml file
curl -X POST http://localhost:9002/analyze-eml \
  -F 'file=@/path/to/email.eml'

🔄 Services & Troubleshooting

# Enable services on boot
sudo systemctl enable ai-buddy-backend
&
sudo systemctl enable ai-buddy-frontend
---------------------------------------
sudo systemctl start ai-buddy-backend
&
sudo systemctl start ai-buddy-frontend
---------------------------------------
# If port conflict
sudo lsof -i :9002
sudo kill <PID>
---------------------------------------

🌍 Access URLs

Frontend UI: http://localhost:9001
FastAPI Docs: http://localhost:9002/docs

👤 Author
Osama Elsherbiny
