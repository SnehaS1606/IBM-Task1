from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are an AI College Assistant.
Your job is to understand student requests and use the correct tools.
If multiple tasks are asked, use multiple tools.
Provide clear and well-structured answers."""),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])
