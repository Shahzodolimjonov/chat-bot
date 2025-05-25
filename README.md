# Cosmic Vibrations AI Test Task

A stateless chat graph using LangGraph with a single tool (`get_current_time`) that returns the current UTC time in ISO-8601 format when prompted (e.g., "What time is it?").

## Setup Instructions
1. **Install Ollama**:
   - Download and install Ollama: https://ollama.com/
   - Pull the model: `ollama pull llama3.2`
   - Start Ollama: `ollama serve` (ensure it runs on port 11434)

2. **Set up the project**:
   ```bash
   git clone <your_repo>
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   pip install -r requirements.txt  
   python main.py  # Run the Script
   
