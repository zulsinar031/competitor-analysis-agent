import sys
from pathlib import Path
from datetime import datetime

from dotenv import load_dotenv
load_dotenv()

from graph import build_graph
from state import AgentState


def run_agent(query: str) -> None:
    graph = build_graph()

    initial_state: AgentState = {
        "query": query,
        "target_company": "",
        "competitors": [],
        "research": {},
        "current_competitor_index": 0,
        "analysis": "",
        "final_report": "",
        "steps_log": [],
    }

    print("Starting agent...")
    full_state = graph.invoke(initial_state)

    report = full_state.get("final_report", "No report generated.")
    target_company = full_state.get("target_company", "UNKNOWN")

    print("\n--- REPORT ---\n")
    print(report)

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = reports_dir / f"{target_company}_{timestamp}_report.md"
    report_path.write_text(report)

    print(f"\nReport saved to: {report_path}")

    print("\nExecution trace:")
    for step in full_state.get("steps_log", []):
        print(f"  {step}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py \"Analyze competitors of Notion\"")
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    run_agent(query)