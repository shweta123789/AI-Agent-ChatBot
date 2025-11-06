from dotenv import load_dotenv
load_dotenv()

import os
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    # Only Groq for now
    llm = ChatGroq(model=llm_id)

    # No search tools for simplicity
    tools = []

    # Create agent without state_modifier
    agent = create_react_agent(model=llm, tools=tools)

    # Pass system prompt as the first message in conversation
    state = {
        "messages": [{"type": "system", "content": system_prompt}] +
                    [{"type": "user", "content": msg} for msg in query]
    }

    # Invoke agent
    response = agent.invoke(state)

    # Extract AI messages
    messages = response.get("messages", [])
    ai_messages = [msg.content for msg in messages if isinstance(msg, AIMessage)]

    return ai_messages[-1] if ai_messages else "No response from agent"
