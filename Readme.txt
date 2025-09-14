source crew_env/bin/activate
ollama run llama3
uvicorn backend.main:app --reload     #to run backend