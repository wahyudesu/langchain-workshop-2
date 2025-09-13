"""
Building a Multi-Agent Financial Analysis System using LangGraph
"""

"""
In this tutorial, we will build a multi-agent financial analysis system using LangGraph. This system utilizes the multi-agent supervisor pattern, where a supervisor agent orchestrates multiple specialized agents to accomplish complex tasks.

In addition to the supervisor, our system will include the following agents:

Web Search Agent: Equipped with the Tavily web search tool to gather information from the web.
Financial Analysis Agent: Uses the Alpha Vantage API to access stock market data.
Code Agent: Has access to a Python REPL for generating code for data visualization.
"""

# Imports and Setup
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.utilities.alpha_vantage import AlphaVantageAPIWrapper
from langchain_experimental.tools import PythonREPLTool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import create_react_agent
# from langgraph.checkpoint.memory import InMemorySaver

from typing import Annotated, Literal, Sequence
from typing_extensions import TypedDict
from pydantic import BaseModel
import operator
import functools

# Load environment variables
from dotenv import load_dotenv

load_dotenv()

# Define the LLM

llm = ChatOpenAI(model="gpt-4.1", temperature=0)

"""
1. Current Date Tool
We define a simple tool to get the current date. This can be useful for time-based queries.
"""

from langchain_core.tools import tool
from datetime import datetime

@tool
def get_current_date():
    """Returns the current date and time. Use this tool first for any time-based queries."""
    return f"The current date is: {datetime.now().strftime('%d %B %Y')}"

"""
2. Tavily Web Search Tool
We initialize the Tavily search tool for the Web Search Agent.
"""

# Tavily Search Tool
tavily_tool = TavilySearchResults(max_results=5)

"""
3. Alpha Vantage Tool
We create a custom tool for the Alpha Vantage API to fetch financial data.
"""

# define custom tool for alpha vantage
from langchain_core.tools import BaseTool

class AlphaVantageQueryRun(BaseTool):
    """Tool that queries the Alpha Vantage API."""

    name: str = "alpha_vantage"
    description: str = (
        "A wrapper around Alpha Vantage API. "
        "Useful for getting financial information about stocks, "
        "forex, cryptocurrencies, and economic indicators. "
        "Input should be the name of the stock ticker."
    )
    api_wrapper: AlphaVantageAPIWrapper = AlphaVantageAPIWrapper()

    def _run(self, ticker: str) -> str:
        """Use the tool."""
        return self.api_wrapper._get_time_series_daily(ticker)

alpha_vantage_tool = AlphaVantageQueryRun()

"""
4. Python REPL Tool
We initialize the Python REPL tool for the Code Agent. Note: This tool can execute arbitrary code. Use with caution.
"""
python_repl_tool = PythonREPLTool()

"""
Creating the Agents
We will create three agents, each with specific roles and tools.
"""

# Web Search Agent
system_prompt = "You are a web search agent. Your role is to use web search tools to find information and return comprehensive answers to queries."
web_search_agent = create_react_agent(llm, tools=[tavily_tool, get_current_date], prompt=system_prompt)

# Financial Analysis Agent
system_prompt = "You are a financial analysis agent. Your role is to use the Alpha Vantage tool to gather financial data and provide concise, informative answers. " \
               "Do not generate charts or plots. Only use the tools provided to you and return a clear, text-based analysis or result."
financial_agent = create_react_agent(llm, tools=[alpha_vantage_tool, get_current_date], prompt=system_prompt)

# Code Agent
system_prompt = "You are a visualization agent. Your role is to create visual representations of data using Python. " \
                "Only use the Python REPL tool provided to generate plots, charts, or other visualizations. " \
                "Do not perform any data analysis or gather information. Your sole purpose is to take the given data " \
                "and create appropriate visualizations. Return the code for the visualization without executing it."

code_agent = create_react_agent(llm, tools=[python_repl_tool], prompt=system_prompt)

# Define team members
members = {
    "WebSearchAgent": "An agent that performs web searches to gather information",
    "FinancialAgent": "An agent that analyzes financial data using Polygon tools to acquire stock market information.",
    "CodeAgent": "An agent that executes Python code and performs computations. Use this to generate plots and tables."
}

# Supervisor Prompt Template
# The supervisor agent manages the workflow by deciding which agent should handle the next task.
system_prompt = (
    "You are a highly efficient supervisor managing a collaborative conversation between specialized agents:"
    "\n{members_description}"
    "\nYour role is to:"
    "\n1. Analyze the user's request and the ongoing conversation."
    "\n2. Determine which agent is best suited to handle the next task."
    "\n3. Ensure a logical flow of information and task execution."
    "\n4. If the user's request has been fulfilled, or if the last agent's response contains a final answer, code for a plot, or a completed visualization, respond with 'FINISH'."
    "   For example, if the CodeAgent returns code for drawing a plot or visualization, and the user's goal was to get a plot, consider the task complete and respond with 'FINISH'."
    "   If the answer is complete and no further agent action is needed, respond with 'FINISH'."
    "\n5. Facilitate seamless transitions between agents as needed."
    "\n6. Conclude the process by responding with 'FINISH' when all objectives are met."
    " Remember, each agent has unique capabilities, so choose wisely based on the current needs of the task."
)

members_description = "\n".join([f"- {k}: {v}" for k, v in members.items()])

system_prompt = system_prompt.format(members_description=members_description)

# Possible options for the supervisor
options = ["FINISH"] + list(members.keys())

# Define the supervisor's output schema
class RouteResponse(BaseModel):
    """
    The supervisor's response to the user's request.
    """
    next: Literal["FINISH", "WebSearchAgent", "FinancialAgent", "CodeAgent"]

# Supervisor Prompt
supervisor_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="messages"),
        (
            "system",
            "Based on the conversation, who should act next? Choose one of: {options}",
        ),
    ]
).partial(options=str(options), members=", ".join([f"{k}: {v}" for k, v in members.items()]))

# Supervisor Agent Function
def supervisor_agent(state):
    supervisor_chain = supervisor_prompt | llm.with_structured_output(RouteResponse)
    return supervisor_chain.invoke(state)

# Define the state
class AgentState(TypedDict):
    messages: Annotated[Sequence[HumanMessage], operator.add]
    next: str
# Helper Function for Agent Nodes
def agent_node(state, agent, name):
    result = agent.invoke({"messages": state["messages"]})
    # Add the agent's response to the conversation
    return {
        "messages": [AIMessage(content=result["messages"][-1].content, name=name)]
    }

# Web Search Node
web_search_node = functools.partial(agent_node, agent=web_search_agent, name="WebSearchAgent")

# Financial Analysis Node
financial_node = functools.partial(agent_node, agent=financial_agent, name="FinancialAgent")

# Code Agent Node
code_node = functools.partial(agent_node, agent=code_agent, name="CodeAgent")

# Initialize the graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("WebSearchAgent", web_search_node)
workflow.add_node("FinancialAgent", financial_node)
workflow.add_node("CodeAgent", code_node)
workflow.add_node("Supervisor", supervisor_agent)

# Define edges
for member in members:
    # Each agent reports back to the supervisor
    workflow.add_edge(member, "Supervisor")

# Supervisor decides the next agent or to finish
conditional_map = {member: member for member in members}
conditional_map["FINISH"] = END
workflow.add_conditional_edges("Supervisor", lambda x: x["next"], conditional_map)

# Entry point
workflow.add_edge(START, "Supervisor")

# Compile the graph with memory checkpointing
# memory = InMemorySaver()
graph = workflow.compile(
    # checkpointer=memory
    )