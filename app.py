import streamlit as st
from agents import agent_router

st.set_page_config(page_title=" RAG Assistant", layout="wide")

# Header Section
st.markdown("""
    <h1 style='text-align: center; color: #4B8BBE;'> Smart RAG Assistant</h1>
    <p style='text-align: center; color: grey;'>Ask me anything – I'll calculate, define, or retrieve from documents intelligently!</p>
    <hr style="border:1px solid #ccc" />""", unsafe_allow_html=True)

# Main Input Area
with st.container():
    st.markdown("###  Ask a Question")
    query = st.text_input("Enter your query", placeholder="e.g. calculate 10 + 5 or define AI", key="input")

    if st.button(" Submit"):
        if query.strip() == "":
            st.warning("Please enter a query to proceed.")
        else:
            with st.spinner(" Searching"):
                response = agent_router(query)

            # Response Section
            st.markdown("###  Response")
            st.markdown(f"""
                <div style="background-color: black; padding: 1rem; border-radius: 10px; border: 1px solid #ccc;">
                    {response}
                </div> """, unsafe_allow_html=True)

            
            with st.expander(" Tool Used / Route Info"):
                if "calculate" in query.lower():
                    st.info(" Tool Used: Calculator")
                elif "define" in query.lower():
                    st.info(" Tool Used: Dictionary")
                else:
                    st.info(" Route: RAG + LLM")
