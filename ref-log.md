# Reflection: Multi-Agent Workflow Implementation

## What I Learned

Implementing a multi-agent workflow offered a hands-on understanding of how specialized AI roles can collaborate to produce higher-quality results. By structuring the system into a Planner Agent (responsible for generating itineraries) and a Reviewer Agent (responsible for verification and refinement), I observed how clearly defined responsibilities lead to more coherent and trustworthy outputs.  
This setup mirrors human collaboration — creativity and planning from one agent balanced by factual validation from another — and demonstrated how structured orchestration improves reasoning depth, factuality, and output consistency.

## Challenges Faced and Solutions

A key challenge involved environment variable handling within a development container.  
Despite using `.env` files and `os.environ.setdefault()` for configuration, the OpenAI SDK consistently raised the error:

This occurred because the `.env` variables were not properly propagated inside the dev container. I read through the OpenAI Agents SDK documentation and experimented with `set_default_client()` and `set_default_api_key()` methods, but these did not resolve the issue.  

Ultimately, the fix was to define the API keys directly in the dev container’s `devcontainer.json` configuration and rebuild the environment. Once the container was rebuilt, the environment variables were properly recognized, and the authentication errors disappeared.  
This experience deepened my understanding of how environment variables are scoped in containerized development and the importance of initializing SDK clients at the correct lifecycle stage.

## Creative Design Choices

I designed distinct agent personas:
- **Planner Agent** – a creative, detail-oriented travel expert generating structured itineraries.  
- **Reviewer Agent** – a factual, analytical validator using real-time tools (e.g., Tavily) to cross-check feasibility.  

Refining prompt instructions and tone significantly improved coherence and realism, highlighting how prompt design and role definition are crucial to multi-agent success. (used a recent personal trip experience to test the performace and accuracy of the system)

## External Tools & Assistance

- OpenAI Agents SDK – for orchestration and multi-agent logic.  
- Tavily API – for live search and fact-checking.  
- Streamlit – for the front-end interface and live tool tracing.  
- ChatGPT – used to draft, debug, and refine the final documentation (this ref log) from my rough points into a complete document for clarity and precision.
