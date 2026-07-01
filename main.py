from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from tools import (
    attendance_checker,
    grade_calculator,
    fee_balance_calculator,
    library_fine_calculator,
    hostel_fee_calculator
)

# Initialize LLM
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0
)

# Define tools
tools = [
    attendance_checker,
    grade_calculator,
    fee_balance_calculator,
    library_fine_calculator,
    hostel_fee_calculator
]

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", """You are an AI College Assistant.
Your job is to understand student requests and use the correct tools.
If multiple tasks are asked, use multiple tools.
Provide clear and well-structured answers."""),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])

# Create Agent
agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

# Create Executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

print("=" * 60)
print("COLLEGE ASSISTANT")
print("=" * 60)

while True:
    user_input = input("\nStudent: ")
    
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    response = agent_executor.invoke(
        {"input": user_input}
    )
    print(f"\nAssistant: {response['output']}")
