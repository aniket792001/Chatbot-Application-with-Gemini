import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

# Load variables from .env
load_dotenv()

# 1. Setup Gemini Model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite", 
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# 2. Create a prompt with "history" for memory
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
])

# 3. Build the Chain (Modern LCEL Syntax)
chain = prompt | llm

# 4. Manage Memory (Streamlit-friendly)
store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

wrapped_chain = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)
# 5. Define Chat Response Function
# MODIFY THIS FUNCTION:
# TO THIS:
def chat_response(user_input, session_id="default"):
    # This session_id ensures User A doesn't see User B's chat history
    return wrapped_chain.stream(
        {"input": user_input},
        config={"configurable": {"session_id": session_id}}
    )
    