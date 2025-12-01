# Travel Assistance Multi-Agent System
AI-powered travel planning built with Google Agent Builder (ADK) & Vertex AI

## Overview
This project implements a multi-agent travel concierge system that automatically generates tailored travel recommendations including attractions, accommodations, restaurants, and travel essentials, along with an optional image-generation + artifact-saving pipeline.

The system uses:
- LLM-powered agents (Gemini 2.5 Flash)
- Sequential + Parallel agent orchestration
- Google Search Tool for live web information
- Custom Tools for image downloading & artifact creation
- Vertex AI Agent Engine Deployment

The result is a fully automated, production-ready travel assistant deployed on Google Cloud.

## Features

### Multi-Agent Architecture

#### Implements three core architectural patterns from ADK:
- Sequential Agents
Step 1: Attractions → Step 2: Parrallel Agents
- Parallel Agents
Step 3: Accommodations, Restaurants, and Travel Essentials run in parallel
- Custom Tools
`get_user_input` to ask the user about the month of visit. 


#### Real-time intelligence

Uses Google Search Tool to fetch:
- Popular attractions
- Best restaurants
- Top-rated hotels
- Weather-specific travel essentials

#### Fully Deployed to Vertex AI Agent Engine
- Runs cloud-scale
- Accessible through the Agent API
- Safe, scalable, and reliable

#### Key Concepts Demonstrated (Required for Capstone)

Your project demonstrates more than 3 major course concepts:

1. Multi-Agent System
- Sequential orchestration
- Parallel orchestration
- LLM-powered agents

2. Tools
- Built-in: Google Search
- Human-in-loop (optional)

3. Deployment
- Fully deployed to Vertex AI Agent Engine

### Running Locally
1. Install dependencies
```
uv sync
```

2. Run locally
```
adk web
```

3. Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

