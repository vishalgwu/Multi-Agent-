# Project Proposal: Multi-Agent AI System for Short News Summarization

## Project Title
**"Smart News Digest System using Multi-Agent AI Architecture"**

##  Project Overview

This project aims to develop a **multi-agent AI system** that will automate fetching, summarization, analysis, and delivery of short-form news articles to users. The system leverages state-of-the-art language models (LLMs), smart task delegation, and role-based agents to offer users **brief**, **personalized**, and **bias-aware** news updates.

Our system will include both **web-based** and **chatbot** interfaces for everyday digests.

---

## Project Objectives

- ✅ Summarize long news articles into 2–3 bullet points using LLMs
- ✅ Display user-selected subject-area-specific news (e.g., Tech, Politics)
- ✅ Detect political or emotive bias in news with sentiment classifiers
- ✅ Provide optional **voice summaries** via TTS (Text-to-Speech)
- ✅ Produce a modular agent architecture (fetcher, summarizer, filter, etc.)
- ✅ Deploy a working prototype with simple and clean interface

---

##  Multi-Agent Roles

| Agent | Function |
|-------|----------|
|  News Fetcher Agent | Fetches latest news articles from RSS feeds, APIs |
| ✂️ Summarizer Agent | Summarizes news in brief summaries using GPT-4o or BART |
| ⚖️ Bias Detector Agent | Scales news tone/perspective (neutral or biased) |
|  Personalization Agent | Filters and ranks news according to user interest profile
| Voice Reader Agent (Optional) | Converts summaries to speech for listening output |
|  Newsletter Agent | Composes daily digests in structured mode for email or chat

---

##  Technologies to Use

| Layer | Tools / Libraries |
|-------|--------------------|
| LLM / NLP | OpenAI GPT-4o, Hugging Face (BART, T5) |
| Agent Orchestration | CrewAI or LangGraph |
| News Source APIs | NewsAPI, RSS feeds (using `feedparser`) |
| Backend | FastAPI (Python) |
| Frontend | Streamlit (Web App) or Telegram Bot |
| TTS | gTTS (Google Text-to-Speech), ElevenLabs (optional) |
| Storage | SQLite / PostgreSQL (user preferences), Redis (caching) |
| Deployment | Streamlit Cloud + Render/Railway for backend services

---

## Workflow Summary

1. User selects news categories of choice (Tech, World, Sports, etc.)
2. News Fetcher Agent retrieves related articles
3. Summarizer Agent summarizes each article into a 2–3 sentence summary
4. Bias Detector Agent detects any emotionally charged or politically biased content
5. Personalization Agent filters the top 3–5 stories based on user profile
6. Voice Agent optionally converts summaries to audio
7. Final output is presented through a web dashboard or sent through a chatbot interface

---


##  Timeline (Estimated)

| Phase | Timeframe |
|-------|-----------|
| Requirement Gathering & Setup | 1 week |
| Agent Design & Integration | 3 weeks |
| Summarizer + Fetcher Agent MVP | 2 weeks |
| UI Development (Streamlit / Bot) | 1–2 week |
| Personalization + Bias Detection | 2 weeks |
| Final Integration & Testing | 2 weeks |
| Deployment & Presentation Prep | 1 week |

**Total: 10–12 weeks (single-person build) **

---

## ✅ Expected Outcomes

- Fully functional, multi-agent-based news summarizer system
- Intelligently processing news by collaborative role-based agents
- Streamlit web app and/or Telegram bot daily summaries
- Practical application as a personal news digest assistant

---

##  Future Scope

- Cross-source comparison for bias analysis (e.g., Fox vs CNN)
- Voice assistant integrations (Alexa, Google Assistant)
- Clustering topics and news trend analysis
- Real-time fact-checking agent

---

## Submitted By

- **Student Name**: Fulsundar Vishal
- - **Email-id**: vishal.fulsundar@gwu.edu
- **Course**: Data science- Deep learning
- **Institution**: GWU
- **Submitted To**: Amir jafari
- 
- 

---

## Repository 
**GitHub**: https://github.com/vishalgwu/Multi-Agent-/tree/main

