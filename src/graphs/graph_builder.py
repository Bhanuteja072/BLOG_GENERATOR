from langgraph.graph import StateGraph , START, END
from src.llms.groqllm import GroqLLM

from src.state.blogstate import BlogState

from src.nodes.blog_node import BlogNode

class GraphBuilder:
    def __init__(self, llm):
        self.llm = llm

    def build_topic_graph(self):
        """
        Build a graph to generate blog based on the topic
        """
        graph = StateGraph(BlogState)
        blog_node_obj = BlogNode(self.llm)

        graph.add_node("title", blog_node_obj.generate_blog_title)
        graph.add_node("content", blog_node_obj.generate_blog_content)

        graph.add_edge(START, "title")
        graph.add_edge("title", "content")
        graph.add_edge("content", END)

        return graph
    

    def build_language_graph(self):
        """
        Build a graph to generate blog based on the language
        """
        graph = StateGraph(BlogState)
        blog_node_obj = BlogNode(self.llm)

        graph.add_node("title", blog_node_obj.generate_blog_title)
        graph.add_node("content", blog_node_obj.generate_blog_content)
        graph.add_node("route", blog_node_obj.route)
        graph.add_node("hindi_translation", lambda state: blog_node_obj.translation({**state, "current_language": "hindi"}))
        graph.add_node("french_translation", lambda state: blog_node_obj.translation({**state, "current_language": "french"}))

        # Edges
        graph.add_edge(START, "title")
        graph.add_edge("title", "content")
        graph.add_edge("content", "route")
        graph.add_conditional_edges(
            "route",
            blog_node_obj.route_decision,
            {
                "hindi": "hindi_translation",
                "french": "french_translation"
            }
        )
        graph.add_edge("hindi_translation", END)
        graph.add_edge("french_translation", END)
        return graph
    
    def setup_graph(self, usecase):
        if usecase == "topic":
            graph = self.build_topic_graph()
        elif usecase == "language":
            graph = self.build_language_graph()
        else:
            raise ValueError("Unsupported usecase: {}".format(usecase))
        return graph.compile()

            

#Below code if for langgraph testing purpose only
llm = GroqLLM().get_llm()
graph_builder = GraphBuilder(llm)
# g=graph_builder.build_topic_graph().compile()
g = graph_builder.build_language_graph().compile()


