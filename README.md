# VoiceAid AI – Voice Based Assistant for Rural Users

VoiceAid AI is a voice-first intelligent assistant designed to help rural and low-literacy users access essential information such as government schemes, weather updates, and advisories using simple voice commands in regional languages.

## Project ID
AID106 – Civora Nexus Pvt. Ltd.

## Key Features
- Voice-based interaction
- Speech-to-Text (STT)
- AI-based Natural Language Understanding (NLU)
- Multilingual support
- Simple and accessible design

## Tech Stack
- Python
- Speech-to-Text (STT)
- NLP
- Text-to-Speech (TTS)
- Git & GitHub

## Project Status
Phase 1 – Voice Input & Speech Recognition

Phase 2 – Natural Language Understanding (NLU)

In Phase 2, the project focuses on enabling the system to understand user intent and context from multilingual voice inputs, rather than only converting speech to text.

This phase forms the core intelligence layer of VoiceAid AI.

Key Capabilities Implemented

Intent Classification

The system analyzes transcribed user speech and classifies it into predefined intents such as:

  weather_query

  scheme_query

  unknown_intent

  Entity Extraction

Important contextual information is extracted from user queries, such as:

Date references (e.g., today, tomorrow)

Multilingual Understanding

Supports intent detection and entity extraction for:

  Hindi

  Telugu

Explainable AI Logic

Rule-based NLP logic is used for transparent and explainable intent detection, suitable for low-resource and rural use cases.

Example Workflow

    User Voice Input (Telugu/Hindi)
            ↓
    Speech-to-Text (STT)
            ↓
    Intent Detection (NLU)
            ↓
    Entity Extraction


Example:

Input (Telugu):

  “రేపు వాతావరణం ఎలా ఉంటుంది”

Output:

  Intent: weather_query
  Entity: date = tomorrow

Technologies Used

  Python

  Rule-based NLP logic

  Multilingual keyword matching

  Modular AI design (STT → NLU separation)

Outcome of Phase 2

  By the end of Phase 2, the system can intelligently interpret user queries, identify their purpose, and extract key contextual details, enabling accurate routing to knowledge retrieval and response generation modules in the next phase.
## Phase 3 – Knowledge Base & Response Generation

Phase 3 focuses on enabling the system to generate meaningful and citizen-friendly responses based on the detected intent and extracted entities.

### Key Features

- **Knowledge Base Integration**
  - Structured JSON-based knowledge base for weather updates and government scheme information
- **Intent-Based Response Generation**
  - User intent is mapped to relevant information from the knowledge base
- **Context-Aware Answers**
  - Responses adapt based on extracted entities such as date (today/tomorrow)
- **Explainable AI Flow**
  - Clear separation between NLU and response generation logic

### Example Flow

