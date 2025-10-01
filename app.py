from src.llms.groqllm import GroqLLM
from src.graphs.graph_builder import GraphBuilder
from fastapi import FastAPI, Request
import uvicorn
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


@app.post("/blogs")
async def create_blog(request: Request):
    data = await request.json()
    topic = data.get("topic","")

    groqllm = GroqLLM()
    llm = groqllm.get_llm()


    graph_buider=GraphBuilder(llm)

    if topic:
        graph = graph_buider.setup_graph(usecase="topic")
        state = graph.invoke({"topic" : topic})

    return {"data" : state}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
