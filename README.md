# Competitor Analysis Agent

> Give it a company name — get a full structured competitor analysis report in seconds.

![LangGraph](https://img.shields.io/badge/LangGraph-0.2+-blue)
![Groq](https://img.shields.io/badge/Groq-llama--3.3--70b-orange)
![Tavily](https://img.shields.io/badge/Tavily-Search-green)
![Docker](https://img.shields.io/badge/Docker-containerized-2496ED)
![Python](https://img.shields.io/badge/Python-3.11-yellow)

---

## What it does

Manually researching competitors is slow and inconsistent. This agent takes a company name, identifies 3–5 real competitors using live web search, researches each one individually, and generates a structured Markdown report — covering features, strengths/weaknesses, and pricing — all in under a minute.

---

## Agent Flow

```
Company Name
     │
     ▼
┌──────────────┐
│   planner    │  Groq identifies 3–5 relevant competitors
└──────┬───────┘
       │ competitor_list
       ▼
┌──────────────┐
│  researcher  │  Tavily runs live web search per competitor (loops)
└──────┬───────┘
       │ research_data
       ▼
┌──────────────┐
│   analyzer   │  Groq synthesizes findings into structured insights
└──────┬───────┘
       │ analysis
       ▼
┌──────────────┐
│   reporter   │  Groq generates final Markdown report
└──────┬───────┘
       │
       ▼
  reports/COMPANY_DATE_report.md
```

---

## Tech Stack

| Tool | Purpose |
|---|---|
| [LangGraph](https://github.com/langchain-ai/langgraph) | Agent orchestration & state management |
| [Groq](https://groq.com) | Fast LLM inference (llama-3.3-70b-versatile) |
| [Tavily](https://tavily.com) | Live web search per competitor |
| [Docker](https://docker.com) | Containerized runtime |

---

## How to Run

### 1. Clone the repo
```bash
git clone https://github.com/zulsinar031/competitor-analysis-agent.git
cd competitor-analysis-agent
```

### 2. Set up your API keys
```bash
cp .env.example .env
```

Edit `.env`:
```env
GROQ_API_KEY=your_groq_key_here
TAVILY_API_KEY=your_tavily_key_here
```

Get your keys here:
- Groq: https://console.groq.com (free)
- Tavily: https://app.tavily.com (free tier: 1000 searches/month)

### 3. Build and run
```bash
docker compose build
docker compose run agent "Analyze competitors of Notion"
```

---

## Example Output

**Terminal:**
```
[Planner]    Identified competitors: Asana, Trello, Evernote, Microsoft OneNote
[Researcher] Research done for Asana.
[Researcher] Research done for Trello.
[Researcher] Research done for Evernote.
[Researcher] Research done for Microsoft OneNote.
[Analyzer]   Analysis complete for NOTION.
[Reporter]   Report generated → reports/NOTION_20260503_143216_report.md
```

**Generated report snippet** (`reports/NOTION_20260503_report.md`):

```markdown
# Competitor Analysis Report

## Executive Summary
Analysis of NOTION's competitors in the project management and note-taking
market, including Asana, Trello, Evernote, and Microsoft OneNote...

## Competitor Overview
| Competitor        | Core Product             | Market Position              |
|-------------------|--------------------------|------------------------------|
| Asana             | Project management       | Established enterprise player|
| Trello            | Kanban-style boards      | Popular visual PM tool       |
| Evernote          | Note-taking & organising | Facing increased competition |
| Microsoft OneNote | Digital notes + Office   | Bundled enterprise player    |
| NOTION            | All-in-one workspace     | Rapidly growing challenger   |

## Strengths & Weaknesses
| Competitor | Strengths                          | Weaknesses                        |
|------------|------------------------------------|-----------------------------------|
| Asana      | Reliable, structured               | Limited flexibility               |
| Trello     | Visual, easy to use                | Weak for complex projects         |
| Evernote   | Robust note-taking                 | Outdated infrastructure           |
| OneNote    | Deep Microsoft integration         | Limited collaboration features    |
| NOTION     | Flexible, all-in-one               | Steep learning curve              |

## Pricing Comparison
| Competitor | Free | Paid Plans                                      |
|------------|------|-------------------------------------------------|
| Asana      | Yes  | Premium $9.99 / Business $24.99 per user/month  |
| Trello     | Yes  | Standard $5 / Premium $10 per user/month        |
| Evernote   | Yes  | Plus $7.99 / Premium $9.99 per user/month       |
| OneNote    | Yes  | Included in Microsoft 365 or $6.99/user/month   |
| NOTION     | Yes  | Personal $4 / Team $8 per user/month            |
```

---

## Project Structure

```
competitor-analysis-agent/
├── nodes/
│   ├── planner.py       # Groq identifies competitor list
│   ├── researcher.py    # Tavily live search per competitor
│   ├── analyzer.py      # Groq synthesizes research into insights
│   └── reporter.py      # Groq generates final Markdown report
├── state.py             # Shared LangGraph state
├── graph.py             # Node wiring & loop logic
├── main.py              # Entrypoint
├── reports/             # Generated reports (gitignored)
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## Notes

- Works best with well-known companies that have public web presence
- Tavily free tier allows 1000 searches/month — each run uses ~5 searches
- Report quality improves for companies with more online coverage
