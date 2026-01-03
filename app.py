import streamlit as st
import database as db
from chatbot import chat_response
import time

# 1. INITIALIZE DATABASE
db.init_db()

# 2. PAGE CONFIGURATION
st.set_page_config(
    page_title="Gemini Flash-Lite Portal",
    page_icon="⚡",
    layout="wide"
)

# 3. INITIALIZE SESSION STATES
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- AUTHENTICATION INTERFACE ---
def show_auth_page():
    st.title("🔐 AI Secure Access")
    
    # Create tabs for a cleaner look
    tab1, tab2 = st.tabs(["Login", "Sign Up"])
    
    with tab1:
        st.subheader("Existing User Login")
        login_user = st.text_input("Username", key="l_user")
        login_pwd = st.text_input("Password", type="password", key="l_pwd")
        
        if st.button("Login", use_container_width=True):
            if db.verify_user(login_user, login_pwd):
                st.session_state.logged_in = True
                st.session_state.username = login_user
                st.success(f"Welcome back, {login_user}!")
                st.rerun()
            else:
                st.error("Invalid credentials. Please check your username/password.")

    with tab2:
        st.subheader("Create New Account")
        reg_user = st.text_input("Choose Username", key="r_user")
        reg_pwd = st.text_input("Choose Password", type="password", key="r_pwd")
        
        if st.button("Register Account", use_container_width=True):
            if reg_user and reg_pwd:
                if db.add_user(reg_user, reg_pwd):
                    st.success("Registration successful! You can now log in.")
                else:
                    st.error("Username already taken.")
            else:
                st.warning("Please fill in both fields.")

# --- MAIN CHAT INTERFACE ---
def show_chat_page():
    # Sidebar with User Info
    with st.sidebar:
        st.title(f"👤 {st.session_state.username}")
        st.caption("Active Session")
        st.divider()
        
        # Resume-boosting stats
        st.write("**Model:** Gemini-2.5-Flash-Lite")
        st.write("**Engine:** LangChain LCEL")
        
        if st.button("Logout", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.messages = []
            st.rerun()

    # Chat Header
    st.title(f"⚡ Welcome, {st.session_state.username}!")
    st.markdown("Your high-speed AI assistant is ready.")

    # Display Chat History
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat Input Logic
    if prompt := st.chat_input("Ask a technical question..."):
        # 1. User Message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # 2. Assistant Response (The fixed indentation block)
        with st.chat_message("assistant"):
            with st.status("Gemini is thinking...", expanded=False) as status:
                st.write("Fetching response from Flash-Lite...")
                
                # We use the session_id to isolate this user's memory
                stream = chat_response(prompt, session_id=st.session_state.username)
                full_response = st.write_stream(stream)
                
                status.update(label="Response complete!", state="complete", expanded=False)

        # 3. Store response
        st.session_state.messages.append({"role": "assistant", "content": full_response})

# --- ROUTING ---
if not st.session_state.logged_in:
    show_auth_page()
else:
    show_chat_page()