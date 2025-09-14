from crewai import Crew , LLM
from .answer_agent import AnswerAgent
# from .scheduler_meeting_agent import SchedulerAgent
# from .slack_agent import SlackAgent
# from .notes_agent import NotesAgent




def run_crew(command: str):

     # Define LLM once
    llm = LLM(model="ollama/llama3", temperature=0.7, max_tokens=1000)

    # Initialize agents
    # scheduler = SchedulerAgent()
    # slack = SlackAgent()
    # notes = NotesAgent()
    answer = AnswerAgent(llm=llm)

    task = None
    response = None

    cmd = command.lower()

    # Decide routing
    # if "schedule" in cmd:
    #     task = scheduler.schedule_meeting(command)

    # elif "meeting" in cmd or "calendar" in cmd:
    #     # return meetings directly (no Crew needed for static response)
    #     response = scheduler.get_meetings("today")

    # elif "slack" in cmd:
    #     task = slack.show_messages(command)

    # elif "note" in cmd:
    #     task = notes.create_notes(command)

    if "explain" in cmd:
        task = answer.explain_concept(command)

    # else:
    #     task = answer.create_task(command)

    # If we already got a response (like listing meetings), return it directly
    # if response:
    #     return response

    # creating a crew object, which is basically a small team of AI agents + tasks that they will work on.
    crew = Crew(agents=[answer], tasks=[task])

    #tells the Crew to start working.
    # 1. Pick the right agent(s) for the task.

    # 2. Run their reasoning/LLM calls.

    # 3. Possibly pass results between agents.

    # 4. Finally return the output/result of the task.
    return crew.kickoff()
