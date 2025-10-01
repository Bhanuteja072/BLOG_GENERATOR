from src.state.blogstate import BlogState
class BlogNode:
    def __init__(Self,llm):
        Self.llm = llm

    def generate_blog_title(self, state: BlogState):
        """
        Generate a blog title based on the topic
        """

        if "topic" in state and state["topic"]:
            prompt="""
                   You are an expert blog content writer. Use Markdown formatting. Generate
                   a blog title for the {topic}. This title should be creative and SEO friendly

                   """
            system_msg = prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_msg)

            return {"blog" : {"title" : response.content}}
        
    def generate_blog_content(self,state : BlogState):
        if "topic" in state and state["topic"]:
            system_prompt = """You are expert blog writer. Use Markdown formatting.
            Generate a detailed blog content with detailed breakdown for the {topic}"""
            system_message = system_prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)
            return {"blog" : {"title" : state['blog']['title'], "content" : response.content}}
