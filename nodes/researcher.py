import json
import os

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

from state import AgentState
from tavily import TavilyClient


def get_llm() -> ChatGroq:
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.1,       # Low temp = more factual, less creative
        max_tokens=2048,
    )


def researcher_node(state: AgentState) -> dict:
    current_competitor_index = state["current_competitor_index"]
    target_company = state["target_company"]
    competitor = state["competitors"][current_competitor_index]

    try:
        api_key = os.getenv("TAVILY_API_KEY", "")
        if not api_key or api_key == "your_tavily_api_key_here":
            raise ValueError("No Tavily key configured")

        client = TavilyClient(api_key=api_key)
        results = client.search(
            query=f"{target_company} {competitor} company analysis",
            max_results=5,
            search_depth="advanced",
        )

        articles = results.get("results", [])
        news_text = "\n\n".join(
            f"• {a['title']}: {a['content'][:300]}"
            for a in articles[:5]
        )
        web_news = f"Analysis for {target_company}:\n{news_text}"

    except Exception:
        # Graceful fallback: ask the LLM to simulate recent context
        llm = get_llm()
        msg = llm.invoke([HumanMessage(
            content=f"Conduct detailed company analysis of {competitor} ({target_company}). Be concise and factual. 150 words max."
        )])
        web_news = f"[LLM-generated context — configure TAVILY_API_KEY for live news]\n{msg.content}"

    return {
        "research": {**state.get("research", {}), competitor: web_news},
        "current_competitor_index": current_competitor_index + 1,
        "steps_log": [f"[Researcher] Research done for {competitor}."],
    }