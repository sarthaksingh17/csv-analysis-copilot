# CSV Analysis Copilot


## Overview

-CSV Analysis Copilot is an AI-powered data analysis web application.
-It allows users to upload a CSV file and ask questions about the data in natural language.
-The application uses a Large Language Model (LLM) only for reasoning, while all computations are performed using Pandas.
-This design ensures accuracy, transparency, and prevents hallucinated results.

## Problem Statement

-Data analysis usually requires:
--Writing Python code
--Knowing SQL or Pandas
--Understanding data structures

-Non-technical users struggle to extract insights from CSV files.

## Solution

-Enable users to:
--Upload a CSV file
--Ask questions in plain English
--Receive computed, data-backed answers

-Use an LLM as a decision-maker, not a calculator.

## Key Features

-Upload and analyze CSV files
-Automatic data preview
-Dataset profiling:
--Row and column count
--Column names
--Data types
--Missing values

-Natural language Q&A over tabular data
-AI-powered Pandas agent for analysis
-Local LLM support using Ollama (no API cost)
-Structured logging for debugging and observability
-Clean, minimal Streamlit UI

## Tech Stack
-Python
-Streamlit – Web application framework
-Pandas – Data manipulation and computation
-LangChain – LLM orchestration and agent framework
-Ollama – Local LLM runtime
-Logging – Application observability

## System Architecture
-User uploads a CSV file via Streamlit UI
-CSV is loaded into a Pandas DataFrame
-User submits a natural language question
-LangChain agent:
--Interprets the question
--Decides the required Pandas operation

-Pandas executes the computation
-Results are returned and displayed in the UI

## Important Design Principle:
-The LLM never generates data
-All results come directly from Pandas computations

## Why Use a Local LLM

-No dependency on paid APIs
-No API key management
-Works offline
-Better understanding of agent behavior
-Ideal for learning and experimentation
The architecture is modular and can be easily adapted to use cloud-based 
LLM APIs for deployment.

## Learning Outcomes
-This project demonstrates:
-How LLMs are used in real applications
-Agent-based reasoning with LangChain
-Safe tool usage in AI systems
-Separation of reasoning and computation
-Data ingestion and profiling
-Debugging using logging
-Performance considerations for local LLMs

## Limitations
-Designed for local execution only
-Not deployed to Streamlit Cloud with a local LLM
-Performance depends on system hardware
-Best suited for small to medium-sized datasets

## Future Enhancements
-Data visualizations and charts
-Follow-up questions using conversational memory
-Cloud-based LLM integration
-Deployment-ready configuration
-Improved error explanations and user guidance

## Author
Created by Sarthak Singh
