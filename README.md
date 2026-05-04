# Competitor Analysis Agent
> Give it a company name, get a full competitor analysis report.

![LangGraph](https://img.shields.io/badge/LangGraph-0.2+-blue)
![Groq](https://img.shields.io/badge/Groq-llama--3.3--70b-orange)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED)
![Tavily](https://img.shields.io/badge/Tavily-search-green)

## What it does
Takes a company name, identifies 3-5 competitors, researches each one using live web search, and generates a structured Markdown report with feature comparison, strengths/weaknesses, and pricing.

## Agent Flow

```
START → Planner → Researcher (loops per competitor) → Analyzer → Reporter → END
```

## Tech Stack
- **LangGraph** — agent orchestration and state management
- **Groq** — LLM inference (llama-3.3-70b-versatile)
- **Tavily** — live web search per competitor
- **Docker** — containerized, runs anywhere

## How to Run

1. Clone the repo
2. Add your API keys:
```bash
cp .env.example .env
# add GROQ_API_KEY and TAVILY_API_KEY
```
3. Build and run:
```bash
docker compose build
docker compose run agent "Analyze competitors of Notion"
```

## Example Output

```
[Planner] Identified ['Asana', 'Trello', 'Evernote', 'Microsoft OneNote'] (NOTION).
[Researcher] Research done for Asana.
[Researcher] Research done for Trello.
[Researcher] Research done for Evernote.
[Researcher] Research done for Microsoft OneNote.
[Analyzer] Analysis complete for NOTION.
[Reporter] Report generated for NOTION.
```

Report saved to `reports/NOTION_20260503_143216_report.md`

## API Keys
- Groq: [console.groq.com](https://console.groq.com) (free)
- Tavily: [tavily.com](https://tavily.com) (free tier: 1000 searches/month)
