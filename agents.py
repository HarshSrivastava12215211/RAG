from tools import calculator_tool, dictionary_tool
from llm import rag_pipeline
import logging

# Set up logging
logging.basicConfig(filename="logs/agent.log", level=logging.INFO)

def agent_router(query: str) -> str:
    query_lower = query.lower()

    if "calculate" in query_lower:
        logging.info(f"Routed to calculator for query: '{query}'")
        return calculator_tool(query)

    elif "define" in query_lower:
        logging.info(f"Routed to dictionary for query: '{query}'")
        return dictionary_tool(query)

    else:
        logging.info(f"Routed to RAG pipeline for query: '{query}'")
        return rag_pipeline(query)
