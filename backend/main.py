#Fastapi enntry points 

from fastapi import FastAPI , Body
from pydantic import BaseModel #used for validation(datatype) we overwrite over basemodel
from backend.agents.coordinator import run_crew 
app = FastAPI(title = "Multi-agent Assistent")

#Model for validating incoming request
class AssistantRequest(BaseModel): #extemding BaseModel
    command: str
   

@app.post("/query")
def query(request: AssistantRequest= Body(...)): #ensures request body maps to the Pydantic model.
   """
    User sends any natural language command.
    Coordinator decides which agent to call.
    """
   response = run_crew(request.command)
   return {"response": response}