# Offline Customer Support Chatbot Report

## 1. Introduction

This project evaluates the feasibility of using a locally hosted Large Language Model (LLM) for customer support automation. The primary goal was to build a proof-of-concept chatbot that operates entirely offline, ensuring data privacy and compliance with regulations like GDPR, CCPA, and India's DPDP Act 2023.

The system uses **Ollama** to run Meta's **Llama 3.2 (3B)** model locally on consumer hardware. A key objective was to compare the effectiveness of two fundamental prompt engineering strategies:
- **Zero-Shot prompting:** Providing only an instruction with no examples
- **One-Shot prompting:** Providing a single high-quality example within the prompt

The experiment uses 20 e-commerce customer support queries adapted from the Ubuntu Dialogue Corpus, a dataset of real technical support conversations.

---

## 2. Methodology

### 2.1 Data Preparation
20 customer support queries were sourced from the Ubuntu Dialogue Corpus and manually adapted to fit an e-commerce context. For example:
- **Original (Technical):** "My wifi driver is not working after the latest update."
- **Adapted (E-commerce):** "My discount code isn't working at checkout."

### 2.2 Prompt Template Design
Two distinct prompt templates were created in the `prompts/` directory:

**Zero-Shot Template:**