from langgraph.graph import StateGraph,END,START
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from pydantic import BaseModel

from main import graph_builder

load_dotenv(override=True)

llm=ChatMistralAI(
    model="open-mixtral-8x7b",
    temperature=0
)

class state(BaseModel):
    input_message:str
    response:str

def chat_node(state:state):
    result=llm.invoke(state.input_message)
    return {"response":result.content}

graph_builder=StateGraph(state)

graph_builder.add_node("chat_bot",chat_node)

graph_builder.add_edge(START,"chat_bot")
graph_builder.add_edge("chat_bot",END)

graph=graph_builder.compile()

initial_state=state(input_message="what is python function",response="")

result=graph.invoke(initial_state)

print(result)