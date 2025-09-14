source crew_env/bin/activate
ollama run llama3
uvicorn backend.main:app --reload     #to run backend
swagger url : http://127.0.0.1:8000/docs
