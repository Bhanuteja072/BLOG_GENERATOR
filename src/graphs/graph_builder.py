from langgraph.graph import StateGraph , START, END
from src.llms.groqllm import GroqLLM

from src.state.blogstate import BlogState

from src.nodes.blog_node import BlogNode

class GraphBuilder:
    def __init__(self,llm):
        self.llm = llm
        self.graph = StateGraph(BlogState)

    def build_topic_graph(self):
        """
        Build a graph to generate blog based on the topic
        """

        self.blog_node_obj = BlogNode(self.llm)

        self.graph.add_node("title",self.blog_node_obj.generate_blog_title)
        self.graph.add_node("content",self.blog_node_obj.generate_blog_content)

        self.graph.add_edge(START, "title")
        self.graph.add_edge("title", "content")
        self.graph.add_edge("content", END)

        return self.graph
    
    def setup_graph(self,usecase):
        if usecase == "topic":
            self.build_topic_graph()
        return self.graph.compile()

            
