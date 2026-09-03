
from langgraph.graph import StateGraph, START, END
from pydantic import BaseModel

class state(BaseModel):
    user_input:str
    response:str


def hello_node(state:state):
    name=state.user_input
    return {"response":f"Hello {name}! welcome to langgraph journey"}

graph_builder=StateGraph(state)

graph_builder.add_node("Hello Node",hello_node)

graph_builder.add_edge(START,"Hello Node")
graph_builder.add_edge("Hello Node",END)

graph=graph_builder.compile()

with open("graph.png","wb") as f:
    f.write(graph.get_graph().draw_mermaid_png())

name=input("Enter your name: ")
initial_state=state(user_input=name,response="")

result=graph.invoke(initial_state)

print(result)