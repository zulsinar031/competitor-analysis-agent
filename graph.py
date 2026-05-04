from langgraph.graph import StateGraph, START, END
from state import AgentState

from nodes.planner import planner_node
from nodes.researcher import researcher_node
from nodes.analyzer import analyzer_node
from nodes.reporter import reporter_node

def should_continue(state: AgentState) -> str:
    if state["current_competitor_index"] < len(state["competitors"]):
        return "researcher"
    return "analyzer"

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("planner", planner_node)
    graph.add_node("analyzer", analyzer_node)
    graph.add_node("reporter", reporter_node)
    graph.add_node("researcher", researcher_node)

    graph.add_edge(START, "planner")

    graph.add_edge("planner", "researcher")
    graph.add_conditional_edges(
        "researcher",        
        should_continue,     
        {
            "researcher": "researcher",  
            "analyzer": "analyzer",      
        }
    )

    graph.add_edge("analyzer", "reporter")
    graph.add_edge("reporter", END)

    return graph.compile()
