import json

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

from state import AgentState


def get_llm() -> ChatGroq:
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.1,       # Low temp = more factual, less creative
        max_tokens=2048,
    )


def planner_node(state: AgentState) -> dict:
    llm = get_llm()
    messages = [
        SystemMessage(content="""You are a business analyst. Given a company name, identify the target company and 3-5 of its main competitors.

Respond ONLY in valid JSON with exactly these keys:
{
    "target_company": "the company name",
    "competitors": ["competitor1", "competitor2", "competitor3"]
}

No explanation, no markdown, just the JSON.
"""),
        HumanMessage(content=f"Query: {state['query']}")
    ]

    response = llm.invoke(messages)

    # Parse the JSON response
    try:
        data = json.loads(response.content.strip())
        target_company = data.get("target_company", "UNKNOWN").upper()
        competitors = data.get("competitors", target_company)
        current_competitor_index = 0
    except (json.JSONDecodeError, AttributeError):
        # Fallback: treat the query itself as a target_company
        target_company = state["query"].upper().strip().split()[0]
        competitors = []
        current_competitor_index = 0

    return {
        "target_company": target_company,
        "competitors": competitors,
        "current_competitor_index": current_competitor_index,
        "steps_log": [f"[Planner] Identified {competitors} ({target_company}). Plan created."],
    }