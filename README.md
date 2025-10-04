# AI Blog Generator

Professional, minimal README for the AI Blog Generator project.

## Overview
AI Blog Generator creates SEO-friendly blog titles and long-form blog content from a short topic. Optionally translates generated content to supported languages (hindi, french). The app uses a graph-based node runner (langgraph) and an LLM client (Groq) to orchestrate generation steps.

## Features
- Generate SEO-friendly blog title and long-form content from a topic.
- Optional translation of the generated blog to hindi or french.
- Streamlit UI for interactive usage.
- Graph-based pipeline (title → content → optional translation).

## Prerequisites
- Windows 10/11
- Python 3.10+
- Virtual environment (recommended)
- A Groq (or other provider) API key if using remote LLMs

## Quick setup (Windows)
1. Clone the repo:
   git clone <repo-url>
   cd AI_BLOG_GENERATOR

2. Create & activate venv:
   .\.venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Configure environment:
   - Create a `.env` file in the project root or set environment variables.
   - Minimum required:
     GROQ_API_KEY=your_api_key_here

   Example `.env`:

```
GROQ_API_KEY=your_api_key_here
```

5. Run the app:
   streamlit run app.py

6. Open displayed URL (usually http://localhost:8501) in your browser.

## Files of interest
- app.py — Streamlit UI (main entry)
- src/llms/groqllm.py — LLM factory / configuration
- src/graphs/graph_builder.py — Builds langgraph StateGraph(s)
- src/nodes/blog_node.py — Node handlers: title, content, translation
- src/state/blogstate.py — Pydantic / TypedDict state models
- langgraph.json — graph spec used for testing / packaging

## Important notes & troubleshooting
- Graph compilation: call `graph.compile()` before invoking. Use `compiled.invoke({...})`.
- Do not leave test/compile code at module import time in `graph_builder.py` — it should not compile graphs on import.
- Model/tooling: some features (function-calling / structured output) require provider/model support.
  - If your provider/model does not support function/tool calling, remove structured-output calls and parse plain-text responses.
- If you see `ValueError: Graph must have an entrypoint`, ensure your graph has at least one edge from `START` to a node.
- If you see `AttributeError: 'StateGraph' object has no attribute 'invoke'`, you are calling `invoke` on the uncompiled graph object — compile it first.

## Minimal environment checklist before running
- .venv active
- requirements installed
- GROQ_API_KEY set (or configure in `src/llms/groqllm.py`)
- `src/graphs/graph_builder.py` has no side-effect compile calls at import

## Contributing
- Create a branch per feature/fix.
- Run existing code locally and keep changes focused.
- Open a PR with description and test steps.

