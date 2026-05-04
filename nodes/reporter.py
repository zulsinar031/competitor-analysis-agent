from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from state import AgentState


def get_llm() -> ChatGroq:
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.1,
        max_tokens=2048,
    )


def reporter_node(state: AgentState) -> dict:
    llm = get_llm()
    target_company = state["target_company"]
    analysis = state["analysis"]

    response = llm.invoke([
        SystemMessage(content="""You are a business report writer. Format the analysis into a clean professional Markdown report with these sections:

# Competitor Analysis Report

## Executive Summary

## Competitor Overview

## Feature Comparison

## Strengths & Weaknesses

## Conclusion & Recommendations

Use tables where appropriate. Be concise and professional."""),
        HumanMessage(content=f"Target company: {target_company}\n\nAnalysis:\n{analysis}")
    ])

    return {
        "final_report": response.content,
        "steps_log": [f"[Reporter] Report generated for {target_company}."],
    }