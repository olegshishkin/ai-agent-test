from langgraph.constants import END
from langgraph.graph import StateGraph

from agent import nodes
from agent.state import State

workflow = StateGraph(State)
workflow.set_entry_point(nodes.CLASSIFICATION_NODE_NAME)

workflow.add_node(nodes.CLASSIFICATION_NODE_NAME, nodes.classify)
workflow.add_node(nodes.EXTRACTION_NODE_NAME, nodes.extract)
workflow.add_node(nodes.SUMMARIZATION_NODE_NAME, nodes.summarize)

workflow.add_edge(nodes.CLASSIFICATION_NODE_NAME, nodes.EXTRACTION_NODE_NAME)
workflow.add_edge(nodes.EXTRACTION_NODE_NAME, nodes.SUMMARIZATION_NODE_NAME)
workflow.add_edge(nodes.SUMMARIZATION_NODE_NAME, END)

graph = workflow.compile()
