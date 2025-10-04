import os
import streamlit as st
from src.llms.groqllm import GroqLLM
from src.graphs.graph_builder import GraphBuilder

st.set_page_config(page_title="AI Blog Generator", page_icon="📝", layout="wide")




# Header
st.title("AI Blog Generator")
st.markdown('<div class="muted">Generate SEO-friendly blog titles and full blog content. Optionally translate content to supported languages.</div>', unsafe_allow_html=True)
st.markdown("")

# Input card
st.markdown('<div class="card">', unsafe_allow_html=True)

topic = st.text_input("Topic", placeholder="e.g. How to optimize Python code for performance")
language = st.selectbox("Translate to (optional)", ["", "hindi", "french"])

col1, col2 = st.columns([3, 1])

with col2:
    generate = st.button("Generate Blog")
    st.write("")

st.markdown("</div>", unsafe_allow_html=True)

# Generation flow (unchanged logic, only use spinner context for better UX)
if generate:
    if not topic:
        st.error("Please enter a topic.")
    else:
        with st.spinner("Generating..."):
            try:
                groqllm = GroqLLM()
                llm = groqllm.get_llm()
                gb = GraphBuilder(llm)
                if language:
                    graph = gb.setup_graph(usecase="language")
                    compiled = graph  # setup_graph returns compiled graph
                    state = compiled.invoke({"topic": topic, "current_language": language})
                else:
                    graph = gb.setup_graph(usecase="topic")
                    compiled = graph
                    state = compiled.invoke({"topic": topic})

                st.success("Generation finished")

                # Display results (same behaviour as before)
                blog = state.get("blog") if isinstance(state, dict) else getattr(state, "blog", None)
                if blog:
                    title = blog.get("title") if isinstance(blog, dict) else None
                    content = blog.get("content") if isinstance(blog, dict) else None
                    if title:
                        st.markdown(f"## {title}")
                    if content:
                        st.markdown(content, unsafe_allow_html=True)
                else:
                    st.info("No structured 'blog' field found. Showing raw state below.")
                    st.json(state)

                st.subheader("Raw state")
                st.json(state)
            except Exception as e:
                st.error(f"Error: {e}")
                st.exception(e)

st.markdown("</div>", unsafe_allow_html=True)
# ...existing code...