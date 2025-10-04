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