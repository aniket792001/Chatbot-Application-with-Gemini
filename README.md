<<<<<<< Updated upstream
# Chatbot-Application-with-Gemini

# ⚡ Gemini Flash-Lite Intelligence Portal

A full-stack, professional AI chatbot platform built with **LangChain**, **Google Gemini 2.0/2.5 Flash-Lite**, and **Streamlit**. This project features a modular architecture, secure user authentication, and persistent conversation memory.

## 🚀 Key Features
- **User Authentication:** Secure Sign-up/Login system with SHA-256 password hashing.
- **Multi-User Memory:** Isolated chat histories per user using LangChain's `RunnableWithMessageHistory`.
- **Ultra-Fast Responses:** Optimized using the `gemini-2.0-flash-lite` model for low-latency performance.
- **Streaming UI:** Real-time "typewriter" response effect for a modern UX.
- **Persistent Storage:** Local SQLite database integration for user data management.
- **Modular Design:** Clear separation of concerns between Database, AI Logic, and UI components.



## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **LLM Framework:** LangChain
- **Model:** Google Gemini 2.0/2.5 Flash-Lite
- **Database:** SQLite
- **Environment Management:** Python-Dotenv

## 📂 Project Structure
```text
├── app.py              # Main Streamlit UI and Routing logic
├── chatbot.py          # LangChain & Gemini API integration
├── database.py         # SQLite authentication and hashing logic
├── requirements.txt    # Project dependencies
├── .env                # API Keys (Excluded via .gitignore)
└── users.db            # Local database (Generated automatically)
=======
# Chatbot-Application-with-Gemini 
# Chatbot-Application-with-claude
>>>>>>> Stashed changes
