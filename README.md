# High-Performance Asynchronous Task Queue Engine

A lightweight, production-grade asynchronous backend service built using Python and FastAPI. The engine splits the system architecture into an API routing tier and a concurrent worker thread execution tier. 

## Key Architectural Highlights
- **Decoupled System Layout:** Separates incoming network requests from resource-heavy processes.
- **Immediate API Response:** Instantly issues tracking IDs (UUIDv4) to users while queuing background logic.
- **Multithreaded Background Execution:** Leverages non-blocking concurrent queues to execute heavy tasks sequentially without degrading API throughput.

## Technologies Utilized
- **Language:** Python
- **Framework:** FastAPI
- **Web Server Engine:** Uvicorn
- **Concurrency Management:** Built-in Python queue & threading

## Quick Setup Guide
1. Launch the application:
   python3 -m uvicorn main:app --reload
2. Interact with the engine via the UI dashboard at: http://localhost:8000/docs
