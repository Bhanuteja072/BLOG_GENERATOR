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
    

    def build_language_graph(self):
        """
        Build a graph to generate blog based on the language
        """

        self.blog_node_obj = BlogNode(self.llm)

        self.graph.add_node("title",self.blog_node_obj.generate_blog_title)
        self.graph.add_node("content",self.blog_node_obj.generate_blog_content)
        self.graph.add_node("route",)
        self.graph.add_node("hindi_translation",)
        self.graph.add_node("french_translation",)


        #Edges
        self.graph.add_edge(START, "title")
        self.graph.add_edge("title", "content")
        self.graph.add_edge("content","route")
        self.graph.add_conditional_edges(
            "route",
            self.blog_node_obj.route_decision,
            {
                "hindi": "hindi_translation",
                "french": "french_translation"
            }
        )
        self.graph.add_edge("hindi_translation", END)
        self.graph.add_edge("french_translation", END)
        return self.graph
    
    def setup_graph(self,usecase):
        if usecase == "topic":
            self.build_topic_graph()
        if usecase == "language":
            self.build_language_graph()
        return self.graph.compile()

            

#Below code if for langgraph testing purpose only
llm = GroqLLM().get_llm()
graph_builder = GraphBuilder(llm)
g=graph_builder.build_topic_graph().compile()


