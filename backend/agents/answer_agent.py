from crewai import Agent, Task

class AnswerAgent(Agent):
    def __init__(self,llm):      #constructor method
        #So super().__init__(...) calls the constructor (__init__) of the parent class Agent.
        super().__init__(     #super() is a built-in Python function that lets you call a method from the parent class i.e Agent class here.
            role="AI Answerer",
            goal="Answer ML/AI questions in detail",
            backstory="Expert ML tutor who explains in simple terms",
            verbose=True,   #Makes it return detailed answers.
        )
        self.llm = llm   #llm is an instance variable of the AnswerAgent class. It stores the LLM object passed during initialization.
    #Task is a class provided by crewAI
    #Creating a new Task object
    # Passing values (name, description, agent, max_iterations) into the Task constructor
    # Returning that Task object
    def explain_concept(self, command: str) -> Task:    #-->Task means this function returns a Task object.
        return Task(
            name="Explain Concept",
            description=f"Explain the concept in detail: {command}",
            agent=self,       #Means this AnswerAgent will execute it.
            max_iterations=3,  #The agent can refine its reasoning up to 3 times before finalizing.
            expected_output="A detailed textual explanation of the concept" , # <-- tell CrewAI we expect a string
            llm=self.llm  ,          # <-- attach LLM to the task
            prompt=f"You are an expert ML/AI tutor. Explain the following concept in detail: {command}",
            sync=True  # make sure CrewAI waits for the LLM output
        )