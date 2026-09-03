from langgraph.graph import StateGraph,END,START
from pydantic import BaseModel

class state(BaseModel):
    num1:int
    num2:int
    add_response:int

def add_node(state:state):
    num1=state.num1
    num2=state.num2
    return {"add_response":num1+num2}

graph_builder=StateGraph(state)

graph_builder.add_node("ADD Numbers",add_node)

graph_builder.add_edge(START,"ADD Numbers")
graph_builder.add_edge("ADD Numbers",END)

graph=graph_builder.compile()

initial_state=state(num1=2,num2=2,add_response=0)

result=graph.invoke(initial_state)

print(f"add of your two numbers in {result["add_response"]}")