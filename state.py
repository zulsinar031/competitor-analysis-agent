from typing import Annotated, TypedDict
import operator


class AgentState(TypedDict):
    query: str
    target_company: str
    competitors: list[str]
    research: dict[str, str]
    current_competitor_index: int
    analysis: str
    final_report: str
    steps_log: Annotated[list[str], operator.add]