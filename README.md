# System Design for the LLM Era: code for every lecture

Python code for the **Learn System Design for the LLM Era** series by **@addywithai**. Each folder matches one lecture and has its own `README.md`.

## How to run any lecture

```bash
cd <folder>
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt   # if the folder has one
cp .env.example .env              # only if the folder has one, then paste your own key
```

Then follow the run steps in that folder's `README.md`. Never commit your `.env` file; it is already in `.gitignore`.

Python 3.10 or newer.

## Lectures

| # | Lecture | Code |
|---|---|---|
| 1 | Learn System Design for the LLM Era: What Changes | No code for this one |
| 2 | Learn LLM Building Blocks for System Design: Tokens, Embeddings and Context | [02-llm-building-blocks](02-llm-building-blocks) |
| 3 | Learn Deterministic vs Creative: Designing Around Unpredictable LLM Outputs | [03-designing-for-unpredictable-outputs](03-designing-for-unpredictable-outputs) |
| 4 | Learn Retrieval for System Design: Chunking, Vector Search and Hybrid Search | [04-retrieval-for-system-design](04-retrieval-for-system-design) |
| 5 | Learn Knowledge Graphs and GraphRAG for LLM Systems | [05-knowledge-graphs-and-graphrag](05-knowledge-graphs-and-graphrag) |
| 6 | Learn How AI Understands Code: ASTs, Call Graphs and Code Search | Coming soon |
| 7 | Learn Agents, Context Engineering and Multimodal Inputs as System Components | Coming soon |
| 8 | Learn Non-Functional Requirements for AI Apps: Latency, Cost, Compliance and Benchmarks | Coming soon |
| 9 | Learn the LLM Gateway Pattern | Coming soon |
| 10 | Learn Circuit Breakers, Timeouts and Fallback Models for LLM Apps | Coming soon |
| 11 | Learn Low-Latency LLM Design: Streaming, Sync vs Async and Queues | Coming soon |
| 12 | Learn LLM Caching: Exact, Semantic and Proactive Caches | Coming soon |
| 13 | Learn Cost Optimization for LLM Systems: Model Routers and Prompt Compression | Coming soon |
| 14 | Learn Grounding Patterns: Ingestion Pipelines, Hybrid RAG and Function Calling | Coming soon |
| 15 | Learn Testing LLM Systems: Golden Datasets, LLM-as-a-Judge and Negative Tests | Coming soon |
| 16 | Learn Observability for LLM Systems: The New Metrics | Coming soon |
| 17 | Learn Security and Privacy Patterns for LLM System Design | Coming soon |
| 18 | Learn Data Storage for LLM Apps: Postgres, Vector DBs, Graph DBs and Caches | Coming soon |
| 19 | Learn the LLM System Design Interview Method: Requirements to Blueprint | Coming soon |
| 20 | Learn to Design an AI Coding Assistant (Part 1): Context Engine and Code Sync | Coming soon |
| 21 | Learn to Design an AI Coding Assistant (Part 2): Fast Completions, Chat and Agents | Coming soon |
| 22 | Learn to Design an Adaptive Learning Platform with LLMs | Coming soon |
| 23 | Learn to Design AI Search for an Online Store (Part 1): Query Understanding and Caches | Coming soon |
| 24 | Learn to Design AI Search for an Online Store (Part 2): Vector Search at Scale and Ranking | Coming soon |
| 25 | Learn to Design an AI Customer Support Agent | Coming soon |
| 26 | Learn Failure Mode Analysis for AI Systems | Coming soon |
| 27 | Learn LLM System Design End to End: Capstone and Cheat Sheet | Coming soon |
