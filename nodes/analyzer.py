import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from state import AgentState


def get_llm() -> ChatGroq:
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.1,
        max_tokens=2048,
    )


def analyzer_node(state: AgentState) -> dict:
    llm = get_llm()
    research = state["research"]
    target_company = state["target_company"]

    research_text = "\n\n".join(
        f"### {competitor}\n{findings}"
        for competitor, findings in research.items()
    )

    response = llm.invoke([
        SystemMessage(content="""You are a business analyst. Compare the competitors and analyze them against the target company across:
- Core product/features
- Market position
- Strengths and weaknesses
- Pricing model
- Target audience

Be structured and concise."""),
        HumanMessage(content=f"Target company: {target_company}\n\nCompetitor research:\n{research_text}")
    ])

    return {
        "analysis": response.content,
        "steps_log": [f"[Analyzer] Analysis complete for {target_company}."],
    }