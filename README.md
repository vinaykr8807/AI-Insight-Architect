# AI Research Explainer Engine

<div align="center">

**🤖 AI-Powered Research Intelligence & Multi-Level Explanation System**

[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-green)](https://fastapi.tiangolo.com/)
[![Groq](https://img.shields.io/badge/Groq-LLaMA%203.3--70B-orange)](https://www.groq.com/)
[![License](https://img.shields.io/badge/License-MIT-purple)](LICENSE)

**Transform Complex Research Topics into Structured, Multi-Level Explanations**

[Features](#features) • [Quick Start](#quick-start) • [Architecture](#architecture) • [Usage](#usage) • [Contributing](#contributing)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Problem Statement & Solution](#problem-statement--solution)
- [Key Features](#features)
- [Architecture](#architecture)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage Guide](#usage-guide)
- [API Endpoints](#api-endpoints)
- [System Components](#system-components)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Development Roadmap](#development-roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

**AI Research Explainer Engine** is an end-to-end intelligence system that transforms complex research topics—sourced from web scraping, vector-based knowledge retrieval, and real-time search—into **structured, multi-level explanations**. 

By combining a **Hybrid RAG Pipeline** with an **Ensemble LLM Architecture**, the platform:

- 🔍 **Intelligently searches** across 5+ live web sources and local knowledge bases
- 📊 **Vectorizes & retrieves** relevant context using FAISS and Sentence-Transformers
- 🧠 **Synthesizes** multi-level explanations (Beginner → Intermediate → Advanced) using Groq LLaMA 3.3-70B
- 🎨 **Visualizes** system architecture through interactive D2/Kroki diagrams
- 📚 **Enriches content** with Wikipedia images and YouTube tutorials
- 📝 **Generates reports** as interactive web views or professional PDFs
- 🎓 **Teaches adaptively** via Quiz Mode, Socratic Tutoring, and "Teach the AI" evaluation

---

## Scenarios

**Scenario 1: Students & Self-Learners**
Students often struggle to interpret complex technical documentation and research papers, which can lead to surface-level understanding and knowledge gaps. Manual research across multiple sources is time-consuming and lacks structured depth.

AI Research Explainer Engine removes these bottlenecks by automatically retrieving relevant data from 5+ live web sources, analyzing scraped content through FAISS vector retrieval, and synthesizing multi-level explanations. A student, for instance, can ask *"Explain Transformers in Deep Learning"* and instantly receive a Beginner intuition, Core Mechanics breakdown, Advanced mathematical foundations with LaTeX, an interactive D2 architecture diagram, and a Python implementation — all in a single structured report.

**Scenario 2: Researchers & Educators**
Researchers and educators frequently need comprehensive insights across different technical domains for curriculum design and academic planning. Manually aggregating information from papers, blogs, and documentation is a massive undertaking. AI Research Explainer Engine streamlines this by allowing experts to query complex topics in plain language and immediately receive multi-domain analysis. For example, an educator can query *"Analyze the mathematical foundations of Diffusion Models"* and the system will surface historical context, architectural diagrams, and AI-synthesized expert advisories.

---

## Architecture Overview

The AI Research Explainer Engine uses a **FastAPI-based backend** with a vanilla HTML/CSS/JS frontend for user interaction and visualization, backed by modular Python services for Web Search, RAG Retrieval, and Ensemble LLM Inference. These layers communicate through high-performance in-process API calls, enabling real-time synthesis and immediate UI updates.

At the core, queries pass through a **Search & Intent Router** (DuckDuckGo DDGS) before reaching the RAG-ML Engine. This engine applies vector similarity rules to retrieve the most relevant content chunks. Simultaneously, the Data Integration Layer retrieves relevant context from the Local Knowledge Base and live data from the web. Response generation leverages a **Triple-Layer Pipeline** (Sentence-Transformers for embedding, FAISS for retrieval, and Groq LLaMA 3.3-70B for synthesis), which are then rendered through Kroki D2 diagrams for visual architecture output. Finally, responses are delivered as structured multi-level reports with visual diagrams and cited sources.

---

## Core Technologies

- **RAG Pipeline (Primary Knowledge Engine)**
  Real-time web scraping via Playwright + Trafilatura, chunked and indexed with FAISS for precise semantic retrieval using Sentence-Transformers (all-MiniLM-L6-v2).

- **Groq LLaMA 3.3-70B (Synthesis Engine)**
  High-speed cloud inference using LLaMA 3.3-70B to merge RAG context into structured, multi-level explanations with LaTeX math, code examples, and D2 diagram code.

- **Hybrid Heuristic-ML Scoring Engine**
  Custom-built explanation engine that generates Beginner, Intermediate, and Advanced content layers with dynamic depth based on selected knowledge level.

- **FastAPI (Backend API Layer)**
  High-performance REST API supporting `/explain`, `/quiz`, `/socratic-tutor`, `/teach-ai`, and `/generate-pdf` endpoints with full CORS support.

- **Kroki D2 Visualization Engine**
  Renders AI-generated D2 architecture diagrams into interactive SVGs via Kroki.io for visual system understanding.

- **Live Web Search Integration**
  DuckDuckGo DDGS multi-query search targeting both general content and academic papers (arXiv, ResearchGate), enabling "Research-Aware" AI responses grounded in current sources.

- **Wikipedia + YouTube Media Engine**
  Automatically fetches relevant technical reference images from Wikipedia API and tutorial videos from YouTube for every explanation.

- **Interactive Quiz & Socratic Learning Engine**
  Adaptive MCQ quiz generation with AI intervention, Socratic tutoring mode with guided questioning, and "Teach the AI" role-reversal evaluation.

- **Persistent Advisory History & Export Architecture**
  One-click PDF report generation via ReportLab with embedded diagrams, equations, code examples, and cited sources for longitudinal record-keeping.

---

## Component-Wise Architecture

| Component | Description |
|---|---|
| FastAPI Backend | Orchestrates the full 7-stage pipeline: search → scrape → RAG → LLM → image → video → response. |
| RAG Service | Playwright-based scraper + Trafilatura extractor + FAISS vector index for semantic chunk retrieval. |
| Heuristic Scoring Engine | Applies knowledge-level rules (Beginner/Intermediate/Advanced) to dynamically adjust explanation depth, math rigor, and code complexity. |
| Search & Intent Router | DuckDuckGo DDGS multi-query search targeting both general content and academic papers (arXiv, ResearchGate). |
| Groq Synthesis Engine | Orchestrates the full explanation report, merging RAG context into structured JSON with title, summary, beginner/mechanics/advanced sections, D2 code, and media queries. |
| Local Knowledge Base | FAISS-indexed local advisory store (rag.py) that boosts context with pre-loaded domain knowledge before LLM synthesis. |
| Kroki D2 Renderer | Sanitizes and renders AI-generated D2 architecture diagrams into SVG via Kroki.io API. |
| Wikipedia Service | Multi-strategy image crawler (REST summary → PageImages → file inspection) with Pexels fallback. |
| YouTube/Pexels Service | Direct YouTube scrape + DDGS video search fallback to return relevant tutorial embed URLs. |
| Quiz Engine | Groq-powered adaptive MCQ generator with Scenario, Code, Boolean, and Match question modes. |
| Socratic Tutor | Guided questioning engine with hint injection, progress tracking, and session history. |
| Teach AI Engine | Role-reversal evaluator that scores user explanations on accuracy, clarity, and conceptual coverage. |
| PDF Generator | ReportLab-based report builder with embedded diagrams (Kroki PNG), equations, code blocks, and source citations. |
| Frontend (HTML/CSS/JS) | Vanilla JS single-page app with tabbed results, MathJax rendering, D2 diagram display, quiz UI, and Socratic chat interface. |

---

## Prerequisites

**1. Python Environment Setup**
Install Python 3.9+ and create a dedicated virtual environment for clean dependency management.
Official Download: https://www.python.org/downloads/

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

**2. Install Required Libraries**
All dependencies used in RAG processing, vector search, web scraping, and the FastAPI backend must be installed from `requirements.txt`.

```bash
pip install -r requirements.txt
```

Key libraries include:
- **FastAPI & Uvicorn**: Core backend API framework
- **Transformers & PEFT**: Sentence-Transformer embedding model
- **Groq**: Cloud-based LLM synthesis and translation engine
- **FAISS-CPU**: Vector similarity search for RAG retrieval
- **Playwright**: Headless browser for web scraping
- **Trafilatura**: Clean text extraction from scraped HTML
- **ReportLab**: PDF report generation with diagrams and equations
- **Pandas/NumPy**: Dataset processing and heuristic math

**3. Playwright Browser Setup**
Required for headless web scraping.

```bash
playwright install chromium
```

**4. Project Structure & Data Assets**
Ensure the local project structure contains the necessary data and model directories:

```
AI Research Explainer Engine/
├── backend/
│   ├── main.py              # FastAPI app & all API routes
│   ├── rag_service.py       # Playwright scraper + FAISS RAG
│   ├── rag.py               # Local knowledge base search
│   ├── teacher_service.py   # Groq explanation + PDF notes
│   ├── pdf_generator.py     # ReportLab PDF report builder
│   ├── wikipedia_service.py # Wikipedia image crawler
│   └── pexels_service.py    # YouTube/Pexels video fetcher
├── frontend/
│   ├── index.html           # Single-page UI
│   ├── app.js               # All frontend logic
│   └── style.css            # Styling
├── .env                     # API keys
└── requirements.txt
```

**5. Ollama Setup (Optional — Local LLM)**
Required only if using local LLM inference as a fallback. Install Ollama and pull the gemma3 model for secure on-premises inference.

Ollama Docs: https://ollama.ai/

```bash
ollama pull gemma3:latest
ollama serve
```

**6. Optional Tools for Development**
Recommended IDEs for development and debugging:
- Visual Studio Code: https://code.visualstudio.com/
- PyCharm Community: https://www.jetbrains.com/pycharm/

These tools support linting, Python virtual environments, and structured project navigation.

**7. API Credentials**
Create a `.env` file in the project root with the following keys:

```env
GROQ_API_KEY=<your_groq_api_key>
PEXELS_API_KEY=<your_pexels_api_key>
```

- **Groq API**: Required for high-speed LLM synthesis. Get your key at https://console.groq.com/
- **Pexels API**: Required for fallback image fetching. Get your key at https://www.pexels.com/api/

---

## Running the Application

```bash
cd backend
uvicorn main:app --reload --port 8000
```

Then open your browser at: **http://localhost:8000**

API documentation available at: **http://localhost:8000/docs**

---

## Project Flow

### 1. Environment Setup and Dependency Configuration
- **Activity 1.1:** Configure the Python 3.9+ environment and install the core AI stack (FastAPI, Sentence-Transformers, Groq, FAISS-CPU, Playwright).
- **Activity 1.2:** Set the Groq API key and Pexels API key in the `.env` file for LLM synthesis and media fetching.
- **Activity 1.3:** Install and configure Playwright's Chromium browser for headless web scraping.
- **Activity 1.4:** Validate the hierarchical folder structure: `backend/`, `frontend/` for clean module separation.
- **Activity 1.5:** (Optional) Initialize the Ollama local host and verify connectivity for the gemma3 fallback engine.

### 2. RAG Pipeline Development and Knowledge Indexing
- **Activity 2.1:** Implement the DuckDuckGo DDGS multi-query search router targeting general content and academic papers (arXiv, ResearchGate).
- **Activity 2.2:** Build the Playwright + Trafilatura scraping pipeline to extract clean text from 5+ live web sources per query.
- **Activity 2.3:** Chunk scraped text and encode with Sentence-Transformers (all-MiniLM-L6-v2) into FAISS vector index for semantic retrieval.
- **Activity 2.4:** Develop the Local Knowledge Base (`rag.py`) with a pre-loaded FAISS index to boost context before LLM synthesis.
- **Activity 2.5:** Validate end-to-end RAG retrieval accuracy across diverse technical topics.

### 3. Hybrid Intelligence & Explanation Pipeline
- **Activity 3.1:** Implement the Heuristic Scoring Engine applying knowledge-level rules (Beginner / Intermediate / Advanced) to dynamically adjust explanation depth, math rigor, and code complexity.
- **Activity 3.2:** Build the LLM prompt architecture with level-specific persona, LaTeX math constraints, and D2 diagram generation instructions.
- **Activity 3.3:** Integrate the Groq LLaMA 3.3-70B synthesis engine to merge RAG context into structured JSON explanations.
- **Activity 3.4:** Implement the D2 diagram sanitizer to clean and validate AI-generated architecture diagrams before Kroki rendering.

### 4. Ensemble AI & Synthesis Architecture
- **Activity 4.1:** Configure the FastAPI backend with all endpoints: `/explain`, `/quiz`, `/socratic-tutor`, `/teach-ai`, and `/generate-pdf`.
- **Activity 4.2:** Implement the Groq Factual Synthesis Engine to merge RAG context, local KB hits, and LLM output into a single cohesive report.
### 5. Frontend UI Implementation and User Interaction
- **Activity 5.1:** Design the vanilla HTML/CSS/JS single-page app with a 9-tab responsive layout (Beginner, Mechanics, Advanced, Diagram, Code, Quiz, Socratic, Teach AI, Sources).
- **Activity 5.2:** Implement MathJax rendering for LaTeX equations and Kroki.io SVG rendering for D2 architecture diagrams.
- **Activity 5.3:** Build the Interactive Quiz Engine with Scenario, Code, Boolean, and Match question modes with AI intervention on wrong answers.
- **Activity 5.4:** Implement the Socratic Tutor and Teach AI modules with session history, progress tracking, and role-reversal evaluation.
- **Activity 5.5:** Integrate the Wikipedia image crawler and YouTube video fetcher for automatic media enrichment per explanation.
- **Activity 5.6:** Build the PDF Report Generator using ReportLab with embedded Kroki diagrams, equations, code blocks, and cited sources.

### 6. Testing and Validation
- **Activity 6.1:** Validate the end-to-end 7-stage pipeline (search → scrape → RAG → LLM → image → video → response) across diverse technical topics.
- **Activity 6.2:** Cross-browser testing; optimize API response times, verify Kroki diagram rendering, and finalize deployment package.


---

## MILESTONE 1: Environment Setup and Dependency Configuration

This foundational milestone prepares the technical environment required for building and running the AI Research Explainer Engine. It ensures that all dependencies, backend modules, Groq API credentials, and project structure are properly installed and aligned for seamless execution of RAG retrieval, LLM synthesis, and explanation workflows.

### Activity 1.1: Setup Ollama and Local LLM (Optional Fallback)

- Visit the official Ollama site: https://ollama.ai/
- Download and install Ollama for your operating system (Windows, macOS, Linux).
- Open terminal and pull the gemma3 model:

```bash
ollama pull gemma3:latest
```

*Figure 2: Ollama Installation Page*

- Start the Ollama service:

```bash
ollama serve
```

*Figure 3: Ollama Model Download*

- Verify the installation by testing model availability:

```bash
ollama list
```

*Figure 4: Ollama Model List Verification*

---

### Activity 1.2: Install Python & Create Virtual Environment

- Install Python 3.9+ from the official website: https://www.python.org/downloads/
- Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

*Figure 5: Creating and Activating Python Virtual Environment in Terminal*

---

### Activity 1.3: Install Project Dependencies

Use the existing `requirements.txt` file in the project root to install all required libraries for:
- Model Inference: `sentence-transformers`, `faiss-cpu`
- API & Synthesis: `groq`, `requests`, `fastapi`, `uvicorn`
- Data Analysis: `pandas`, `numpy`
- Web Scraping: `playwright`, `trafilatura`, `duckduckgo-search`
```bash
pip install -r requirements.txt
```

```
fastapi>=0.110.0
uvicorn[standard]>=0.29.0
python-dotenv>=1.0.0
groq>=0.9.0
requests>=2.31.0
faiss-cpu>=1.8.0
sentence-transformers>=2.7.0
trafilatura>=1.9.0
duckduckgo-search>=6.1.0
numpy>=1.26.0
playwright>=1.44.0
```

*Figure 7: Installing Requirements*

---

### Activity 1.4: Create the .env Configuration File

Add the required environment variables:

```env
GROQ_API_KEY=<your_groq_api_key>
PEXELS_API_KEY=<your_pexels_api_key>
```

The backend loads these at startup from `main.py`:

```python
from dotenv import load_dotenv
load_dotenv(os.path.join(_BACKEND_DIR, '..', '.env'))

GROQ_API_KEY   = os.getenv("GROQ_API_KEY", "")
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY", "")

from groq import Groq
groq_client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None
```

*Figure 8: Setting .env File*

---

### Activity 1.5: Verify Model and Data Directories

Ensure that the backend service files are present in the `backend/` directory:
- `rag_service.py` — Playwright scraper + FAISS RAG
- `rag.py` — Local FAISS knowledge base
- `wikipedia_service.py` — Wikipedia image crawler
- `pexels_service.py` — YouTube/Pexels video fetcher
- `pdf_generator.py` — ReportLab PDF builder

The local knowledge base initializes automatically on startup from `rag.py`:

```python
def initialize_knowledge_base():
    global INDEX, DOC_STORE
    sample_data = [
        {"text": "B-Trees are self-balancing search trees commonly used in databases.", "source": "Lesson: Data Structures"},
        {"text": "A Dockerfile contains all commands to assemble an image.", "source": "Lesson: DevOps"},
        {"text": "RESTful APIs use HTTP requests to GET, PUT, POST and DELETE data.", "source": "Lesson: Backend"},
    ]
    DOC_STORE = sample_data
    texts = [d['text'] for d in sample_data]
    if model:
        embeddings = model.encode(texts)
        INDEX = faiss.IndexFlatL2(DIMENSION)
        INDEX.add(np.array(embeddings).astype('float32'))

initialize_knowledge_base()
```

---

### Activity 1.6: Prepare Project Folder Structure

Verify that the full project structure is organized as follows:

```
AI Research Explainer Engine/
├── backend/
│   ├── main.py              # FastAPI app & all API routes
│   ├── rag_service.py       # Playwright scraper + FAISS RAG
│   ├── rag.py               # Local knowledge base search
│   ├── teacher_service.py   # Groq explanation + PDF notes
│   ├── pdf_generator.py     # ReportLab PDF report builder
│   ├── wikipedia_service.py # Wikipedia image crawler
│   └── pexels_service.py    # YouTube/Pexels video fetcher
├── frontend/
│   ├── index.html           # Single-page UI
│   ├── app.js               # All frontend logic
│   └── style.css            # Styling
├── .env                     # API keys
└── requirements.txt
```

*Figure 9: Folder Structure*

---

## MILESTONE 2: RAG Pipeline Development and Knowledge Indexing

Sets up the RAG environment with Sentence-Transformers and FAISS, installs required libraries, and processes live web-scraped content. Ensures all dependencies are compatible and the embedding model is available for semantic retrieval, FAISS indexing, and context-aware LLM synthesis.

### Activity 2.1: Sentence-Transformer Embedding Model Setup

The system loads the `all-MiniLM-L6-v2` embedding model at startup for real-time semantic encoding of scraped web content.

- **Environment Configuration:** Uses `sentence-transformers` library with the lightweight `all-MiniLM-L6-v2` model (384-dim embeddings).
- **Dependency Management:** Installed via `requirements.txt` with `faiss-cpu`, `numpy`, and `sentence-transformers`.
- **Model Verification:** Confirms embedding model loaded successfully before serving requests.

```python
# rag_service.py
from sentence_transformers import SentenceTransformer

try:
    embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
except Exception as e:
    print(f"Failed to load sentence transformer: {e}")
    embedding_model = None
```

*Figure 10: Embedding Model Setup and Library Installation*

---

### Activity 2.2: Web Scraping Pipeline & Content Extraction

The Playwright + Trafilatura pipeline extracts clean text from 5+ live web sources per query, forming the raw corpus for FAISS indexing.

- **Multi-Source Scraping:** Playwright headless Chromium visits each URL and extracts full page HTML.
- **Clean Text Extraction:** Trafilatura strips boilerplate, ads, and navigation — returning only article body text.
- **Source Attribution:** Each chunk is prefixed with its source URL for citation in the final report.

```python
# rag_service.py
def scrape_pages(urls: list[str]) -> str:
    combined_text = ""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(user_agent="Mozilla/5.0 ...")
        page = context.new_page()
        page.set_default_timeout(10000)
        for url in urls:
            try:
                page.goto(url)
                html = page.content()
                text = trafilatura.extract(html)
                if text:
                    combined_text += f"\n\nSource: {url}\n{text}"
            except Exception as e:
                print(f"Error scraping {url}: {e}")
        browser.close()
    return combined_text
```

*Figure 11: Playwright Scraping Pipeline and Corpus Stats*

---

### Activity 2.3: FAISS Vector Indexing & Semantic Retrieval

The scraped text is chunked, encoded with Sentence-Transformers, and indexed into FAISS for top-k semantic retrieval.

- **Chunking Strategy:** Text split into 500-word chunks for granular retrieval.
- **FAISS IndexFlatL2:** Exact L2 distance search across all chunk embeddings.
- **Top-K Retrieval:** Returns the 4-5 most semantically relevant chunks for the query.

```python
# rag_service.py
def retrieve_context(query: str, combined_text: str, top_k: int = 4) -> str:
    chunks = chunk_text(combined_text)
    chunk_embeddings = embedding_model.encode(chunks)

    dimension = chunk_embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(chunk_embeddings).astype('float32'))

    query_embedding = embedding_model.encode([query])
    distances, indices = index.search(np.array(query_embedding).astype('float32'), top_k)

    relevant_chunks = [chunks[idx] for idx in indices[0] if idx != -1 and idx < len(chunks)]
    return "\n\n... ".join(relevant_chunks)
```

*Figure 12: FAISS Indexing & Semantic Retrieval*

---

### Activity 2.4: Local Knowledge Base Boost

A pre-loaded FAISS index (`rag.py`) injects domain knowledge before LLM synthesis, boosting context quality beyond live web results.

- **Static Knowledge Store:** Pre-seeded with curated technical facts across CS, DevOps, and Backend domains.
- **FAISS Search:** Same L2 similarity search as the live RAG pipeline.
- **Context Injection:** Local KB hits are prepended to the web RAG context before the Groq prompt.

```python
# rag.py
def search_knowledge(query, top_k=3):
    if not model or not INDEX or not DOC_STORE:
        return []
    query_vec = model.encode([query])
    D, I = INDEX.search(np.array(query_vec).astype('float32'), top_k)
    results = [DOC_STORE[idx] for idx in I[0] if idx != -1 and idx < len(DOC_STORE)]
    return results
```

*Figure 13: Local Knowledge Base Search and Context Injection*

---

### Activity 2.5: End-to-End RAG Validation

The full 7-stage pipeline is validated across diverse technical topics to confirm retrieval accuracy and context quality before LLM synthesis.

- **Pipeline Stages:** search → scrape → chunk → embed → FAISS index → retrieve → inject.
- **Fallback Handling:** If scraping yields nothing, search snippets are used as context.
- **Local KB Merge:** Local hits are prepended with clear section headers for LLM clarity.

```python
# main.py — /explain endpoint
search_results = _search_with_meta(req.query, max_results=req.max_sources)
urls = [r["url"] for r in search_results if r.get("url")]

raw_text = scrape_pages(urls) if urls else ""
if not raw_text.strip():
    raw_text = "\n\n".join(
        f"Source: {r['url']}\nTitle: {r['title']}\n{r['snippet']}"
        for r in search_results
    )

context = retrieve_context(req.query, raw_text, top_k=5)

local_hits = search_knowledge(req.query, top_k=3)
if local_hits:
    kb_lines = "\n".join(f"- {h['text']}  (Source: {h['source']})" for h in local_hits)
    context = f"LOCAL KNOWLEDGE BASE CONTEXT:\n{kb_lines}\n\nWEB RESEARCH CONTEXT:\n{context}"
```

*Figure 15: End-to-End RAG Pipeline Validation*

---

## MILESTONE 3: Hybrid Intelligence & Explanation Pipeline

This milestone implements the hybrid intelligence system combining heuristic knowledge-level scoring with LLM-powered explanation synthesis. Processes user queries through level-specific prompt engineering, D2 diagram generation, and Groq synthesis to deliver structured, multi-depth research explanations.

### Activity 3.1: Heuristic Scoring Engine — Knowledge-Level Rules

The system dynamically adjusts explanation depth, math rigor, and code complexity based on the selected knowledge level (Beginner / Intermediate / Advanced).

- Beginner: 600+ word analogies, no LaTeX, simplified code
- Intermediate: Engineering trade-offs, key formulas, production code
- Advanced: 800+ word research synthesis, full LaTeX derivations, PhD-level depth

```python
# main.py — _build_prompt()
if level == "beginner":
    persona = "You are a friendly, elite educator explaining to someone with NO technical background."
    advanced_req = "ABSOLUTELY NO math formulas or LaTeX equations."
elif level == "advanced":
    persona = "You are a Research Lead at a major AI Lab explaining to a PhD student."
    advanced_req = "800+ words. Extensive Mathematical Foundations in LaTeX. Derivations and loss functions."
elif level == "intermediate":
    persona = "You are a Senior Software Architect. Focus on industry implementation."
    mechanics_req = "Exhaustive Implementation & Component Logic. 600+ words."
```

*Figure 17: Knowledge-Level Heuristic Scoring Engine*

Key Features:
- Dynamic persona assignment per level
- LaTeX math toggled on/off based on level (`math_rigor` variable)
- Word count minimums enforced per section in the prompt

---

### Activity 3.2: LLM Prompt Architecture with D2 Diagram Instructions

The prompt enforces structured JSON output with level-specific content depth and D2 architecture diagram generation rules.

```python
# main.py — _build_prompt()
return f"""{persona}
Query: "{query}"

Real-time Scraped Research Context:
---
{context[:7500]}
---

Return ONLY a valid JSON object:
{{
  "title": "Professional Tech Title",
  "summary": "Academic executive summary",
  "beginner_explanation": "...",
  "core_mechanics": "...",
  "advanced_concepts": "...",
  "code_example": "Python code string",
  "key_takeaways": ["point 1", "point 2", "point 3"],
  "real_world_applications": ["App 1", "App 2"],
  "d2_code": "direction: down\nModule.A -> Module.B: \"Data Flow\"",
  "visual_query": "Tech Stock Photo keyword",
  "video_query": "YouTube Search Query"
}}"""
```

*Figure 18: LLM Prompt Architecture and D2 Diagram Instructions*

---

### Activity 3.3: Groq LLaMA 3.3-70B Synthesis Engine

Integrates Groq's high-speed cloud inference to merge RAG context into structured JSON explanations.

```python
# main.py — _llm_explain()
resp = groq_client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": _build_prompt(query, context, level, include_code)}],
    temperature=0.4,
    max_tokens=4000,
    response_format={"type": "json_object"},
)
raw_content = resp.choices[0].message.content.strip()
data = _parse_groq_json(raw_content)
```

*Figure 19: Groq LLaMA 3.3-70B Synthesis Integration*

---

### Activity 3.4: D2 Diagram Sanitizer

Cleans and validates AI-generated D2 architecture diagrams before sending to Kroki.io for SVG rendering.

```python
# main.py — _sanitize_d2()
def _sanitize_d2(d2: str) -> str:
    d2 = re.sub(r'^```(?:d2)?\s*', '', d2.strip(), flags=re.I)
    d2 = re.sub(r'\s*```\s*$', '', d2)

    for line in d2.splitlines():
        if '->' in line:
            conn_match = re.match(r'^([^:]+\->\s*[^:{]+)(?::\s*(.*))?$', line.strip())
            if conn_match:
                label = ' '.join((conn_match.group(2) or '').split()[:4])
                clean_lines.append(f"{conn_match.group(1).rstrip()}: \"{label}\"")
    return '\n'.join(clean_lines)
```

*Figure 20: D2 Diagram Sanitizer and Kroki Rendering Pipeline*

---

## MILESTONE 4: Ensemble AI & Synthesis Architecture

This milestone implements the multi-model synthesis system that routes queries through DuckDuckGo search, merges RAG context with local KB hits, synthesizes via Groq LLaMA 3.3-70B, and delivers structured explanations with Wikipedia images and YouTube video embeds.

### Activity 4.1: Multi-Query Search Router

Executes dual DuckDuckGo queries — one for general content and one targeting academic papers (arXiv, ResearchGate) — to maximize context coverage.

```python
# main.py — _search_with_meta()
search_variants = [query, f"{query} research papers arxiv paperwithcode"]

ddgs = DDGS()
for q in search_variants:
    raw = ddgs.text(q, max_results=max_results)
    for r in raw:
        url = r.get('href') or r.get('link') or r.get('url', '')
        if url:
            all_results.append({
                'title':   r.get('title', '') or url,
                'url':     url,
                'snippet': r.get('body') or r.get('snippet', ''),
            })
```

*Figure 27: Multi-Query Search Router with Academic Paper Targeting*

---

### Activity 4.2: Groq Factual Synthesis with Structured JSON Output

Aggregates RAG context and local KB hits, then synthesizes a unified structured report via Groq's Llama-3.3-70B.

```python
# main.py — _llm_explain()
resp = groq_client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": _build_prompt(query, context, level, include_code)}],
    temperature=0.4,
    max_tokens=4000,
    response_format={"type": "json_object"},
)
data = _parse_groq_json(resp.choices[0].message.content.strip())
d2 = _sanitize_d2((data.get("d2_code") or "").strip())
data["d2_code"] = d2
```

*Figure 29: Groq Factual Synthesis with JSON Schema Enforcement*

---

### Activity 4.3: Wikipedia Image + YouTube Video Fetcher

Automatically enriches every explanation with a relevant technical reference image and tutorial video embed.

```python
# wikipedia_service.py — get_wikipedia_image()
summary_resp = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{safe_title}", headers=headers, timeout=5)
if summary_resp.status_code == 200:
    sum_data = summary_resp.json()
    if "originalimage" in sum_data:
        return sum_data["originalimage"].get("source")

# pexels_service.py — get_youtube_video()
search_query = urllib.parse.quote(f"{query} tutorial")
url = f"https://www.youtube.com/results?search_query={search_query}"
html = urllib.request.urlopen(req, timeout=5).read().decode()
video_ids = re.findall(r'"videoId":"([a-zA-Z0-9_-]{11})"', html)
return f"https://www.youtube.com/embed/{video_ids[0]}?rel=0"
```

*Figure 31: Wikipedia Image Crawler and YouTube Video Fetcher*

---

## MILESTONE 5: Frontend UI Implementation and User Interaction

This milestone implements the vanilla HTML/CSS/JS single-page application with a 9-tab responsive layout, MathJax rendering, Kroki D2 diagram display, interactive quiz, Socratic tutor, Teach AI module, and PDF export.

### Activity 5.1: 9-Tab Responsive Layout Design

Implements modular tab navigation across all explanation layers and interactive learning modes.

```html
<!-- index.html — Tab Navigation -->
<div class="tab-nav glass">
  <button class="tab-btn active" onclick="showTab('beginner')">🌱 Beginner</button>
  <button class="tab-btn" onclick="showTab('mechanics')">⚙️ Mechanics</button>
  <button class="tab-btn" onclick="showTab('advanced')">🚀 Advanced</button>
  <button class="tab-btn" onclick="showTab('diagram')">📊 Diagram</button>
  <button class="tab-btn" onclick="showTab('code')">💻 Code</button>
  <button class="tab-btn" onclick="showTab('quiz')">🧠 Quiz</button>
  <button class="tab-btn" onclick="showTab('socratic')">🤔 Socratic</button>
  <button class="tab-btn" onclick="showTab('teach')">👨🏫 Teach AI</button>
  <button class="tab-btn" onclick="showTab('sources')">🔗 Sources</button>
</div>
```

*Figure 34: 9-Tab Responsive Layout Architecture*

Tab Functionalities:
1. Beginner: Intuitive explanation with key takeaways
2. Mechanics: Core architecture and implementation depth
3. Advanced: Research-level content with LaTeX math
4. Diagram: Kroki-rendered D2 SVG architecture diagram
5. Code: Python implementation with copy button
6. Quiz: Adaptive MCQ challenge with AI intervention
7. Socratic: Guided questioning tutor with progress tracking
8. Teach AI: Role-reversal evaluation with scoring
9. Sources: Cited web sources with links

---

### Activity 5.2: Dynamic Search with Level & Source Selectors

Cascading input controls that adjust explanation depth and number of sources scraped per query.

```html
<!-- index.html — Options Row -->
<select id="level-select" class="opt-select">
  <option value="all">All Levels</option>
  <option value="beginner">Beginner</option>
  <option value="intermediate">Intermediate</option>
  <option value="advanced">Advanced</option>
</select>

<select id="sources-select" class="opt-select">
  <option value="4">4 Sources</option>
  <option value="6">6 Sources</option>
  <option value="8">8 Sources</option>
</select>
```

*Figure 35: Dynamic Level and Source Selector UI*

---

### Activity 5.3: Kroki D2 Diagram Rendering + MathJax Integration

Renders AI-generated D2 architecture diagrams as interactive SVGs via Kroki.io, and renders LaTeX equations via MathJax.

```html
<!-- index.html — MathJax Config -->
<script>
  window.MathJax = {
    tex: {
      inlineMath: [['$', '$'], ['\\(', '\\)']],
      displayMath: [['$$', '$$'], ['\\[', '\\]']],
      processEscapes: true
    }
  };
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
```

```python
# pdf_generator.py — fetch_diagram_image() via Kroki
response = requests.post(
    'https://kroki.io/d2/png',
    data=d2_code.encode('utf-8'),
    headers={'Content-Type': 'text/plain'},
    timeout=30
)
if response.status_code == 200:
    img_buffer = BytesIO(response.content)
    img = Image(img_buffer, width=6*inch, height=4*inch, kind='proportional')
    return img
```

*Figure 36: Kroki D2 SVG Rendering and MathJax LaTeX Display*

---

### Activity 5.4: PDF Report Generator with Embedded Diagrams

One-click PDF export via ReportLab with embedded Kroki diagrams, equations, code blocks, and cited sources.

```python
# pdf_generator.py — generate_topic_pdf()
def generate_topic_pdf(topic_data):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4,
        topMargin=0.5*inch, bottomMargin=0.5*inch)
    elements = []

    elements.append(Paragraph(topic_data.get('title', 'Topic'), title_style))
    elements.append(Paragraph(topic_data['summary'], body_style))
    elements.append(PageBreak())

    # Embed Kroki diagram as PNG
    if topic_data.get('d2_code'):
        diagram_img = fetch_diagram_image(topic_data['d2_code'])
        if diagram_img:
            elements.append(diagram_img)

    # Sources
    for i, src in enumerate(topic_data.get('sources', [])[:10], 1):
        elements.append(Paragraph(f"{i}. {src.get('title', '')}", body_style))

    doc.build(elements)
    buffer.seek(0)
    return buffer
```

*Figure 38: PDF Report Generator with Kroki Diagram and Source Citations*

---

## MILESTONE 6: Testing and Validation

### Activity 6.1: End-to-End Pipeline Validation

Validates the complete 7-stage pipeline (search → scrape → RAG → LLM → image → video → response) across diverse technical topics.

```python
# main.py — /explain endpoint — Full 7-stage pipeline
print("  [1/7] Web search…")
search_results = _search_with_meta(req.query, max_results=req.max_sources)

print("  [2/7] Scraping pages…")
raw_text = scrape_pages(urls) if urls else ""

print("  [3/7] RAG vector retrieval…")
context = retrieve_context(req.query, raw_text, top_k=5)

print("  [4/7] Local KB search…")
local_hits = search_knowledge(req.query, top_k=3)

print("  [5/7] Generating explanation via Groq…")
data = _llm_explain(req.query, context, req.level, req.include_code)

print("  [6/7] Fetching image…")
data["image_url"] = get_wikipedia_image(data.get("visual_query") or req.query)

print("  [7/7] Fetching video…")
data["video_url"] = get_pexels_video(data.get("video_query") or req.query)

print("  ✅  Pipeline complete.")
return JSONResponse(content=data)
```

*Figure 39: End-to-End 7-Stage Pipeline Execution Log*

---

### Activity 6.2: API Health Check & Deployment Validation

Confirms all modules loaded, API keys set, and services available before deployment.

```python
# main.py — /health endpoint
@app.get("/health")
def health():
    return {
        "status":          "ok",
        "groq_key_set":    bool(GROQ_API_KEY),
        "pexels_key_set":  bool(PEXELS_API_KEY),
        "embedding_model": "loaded" if EMBEDDING_AVAILABLE else "unavailable",
        "playwright":      PLAYWRIGHT_AVAILABLE,
        "ddgs":            DDGS_AVAILABLE,
        "modules": {
            "rag_service":       True,
            "pexels_service":    True,
            "wikipedia_service": True,
            "rag":               True,
            "pdf_generator":     True,
        },
    }
```

*Figure 40: Health Check Endpoint and Deployment Validation*


---

## Conclusion

The AI Research Explainer Engine represents a significant advancement in how students, researchers, and educators access actionable, structured technical knowledge across any domain. By combining ensemble AI reasoning, domain-specific RAG retrieval from live web sources and a local knowledge base, and real-time search integration, the system delivers multi-level explanations across diverse technical topics with high contextual accuracy and research-backed depth.

Built on a modular architecture featuring Sentence-Transformer semantic embeddings, FAISS vector retrieval, Groq LLaMA 3.3-70B cloud synthesis, and a hybrid heuristic-ML scoring engine, the platform offers both technical resilience and exceptional accessibility. Interactive D2 architecture diagrams via Kroki.io, Wikipedia + YouTube media enrichment, and one-click PDF export enable users to receive precise, evidence-based explanations tailored to their knowledge level — making it invaluable for self-learners, academic researchers, and educators alike.

Looking forward, the engine provides a robust foundation for extensions such as personalized learning path generation, integration with academic paper databases (arXiv, Semantic Scholar), mobile app deployment for offline access, real-time collaborative annotation, and adaptive difficulty tracking across sessions. With its blend of semantic search, RAG-powered context retrieval, multi-level explanation synthesis, and interactive quiz and Socratic learning modes, the AI Research Explainer Engine sets a practical benchmark for next-generation AI-powered research intelligence platforms serving the global learning community.
