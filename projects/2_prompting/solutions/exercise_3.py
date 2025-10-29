"""
Solution for Exercise 3: Use LLMs with structured outputs
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from enum import Enum


load_dotenv()

def exercise_3(ticket_text: str) -> str:
    """
    Use LLMs with structured outputs to classify a support ticket and extract structured information.
    Args:
        ticket_text (str): The text of the customer support ticket.
    Returns:
        str: LLM's structured response.
    """

    # Enums in Python are used to define a set of fixed values.
    class PriorityEnum(str, Enum):
        URGENT = "URGENT"
        NORMAL = "NORMAL"
        LOW = "LOW"


    class SupportTicket(BaseModel):
        """Support ticket request"""

        priority: PriorityEnum = Field(description="The priority of the ticket. One of [URGENT, NORMAL, LOW]")
        # You can add many more fields (e.g. number of words, difficulty to solve, estimated time, ...)
        # as long as you define them well. For example here i add a title and a theme for each ticket.
        title: str = Field(description="Title of the ticket")
        theme: str = Field(description="General theme of the request")
    

    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash").with_structured_output(SupportTicket)
    result = llm.invoke(ticket_text)
    return result


if __name__ == "__main__":
    tickets = [
        "My internet connection has been down for hours and I need it for work. Please help!",
        "I would like to change my billing address for future invoices.",
        "The printer in the office is making a strange noise, but it still works."
    ]
    for i, ticket in enumerate(tickets, 1):
        llm_response = exercise_3(ticket)
        print(f"Example {i}: {ticket}\nLLM's Response: {llm_response}\n")