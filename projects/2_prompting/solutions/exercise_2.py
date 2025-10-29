"""
Solution for Exercise 2: Few-shot Prompting for Ticket Priority Classification using LangChain and Google LLM
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

def exercise_2(ticket_text: str) -> str:
    """
    Classify a customer support ticket as 'URGENT', 'NORMAL', or 'LOW' priority using few-shot prompting and Google LLM via LangChain.
    Args:
        ticket_text (str): The text of the customer support ticket.
    Returns:
        str: LLM's response.
    """
    prompt_template = PromptTemplate(
        input_variables=["ticket_text"],
        template=(
            "Classify the following customer support ticket as 'URGENT', 'NORMAL', or 'LOW' priority.\n"
            "Example:\n"
            "Our website is completely inaccessible and customers are complaining.\n"
            "Priority: URGENT\n"
            "Example:\n"
            "Can you send me the user manual for the new software update?\n"
            "Priority: NORMAL\n"
            "Example:\n"
            "The air conditioning in the server room stopped working and it's getting very hot.\n"
            "Priority: URGENT\n"
            "Ticket: {ticket_text}\n"
            "Priority:"
        )
    )
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
    result = llm.invoke(prompt_template.format_prompt(ticket_text=ticket_text))
    return result.content

if __name__ == "__main__":
    tickets = [
        "My internet connection has been down for hours and I need it for work. Please help!",
        "I would like to change my billing address for future invoices.",
        "The printer in the office is making a strange noise, but it still works."
    ]
    for i, ticket in enumerate(tickets, 1):
        llm_response = exercise_2(ticket)
        print(f"Example {i}: {ticket}\nLLM's Response: {llm_response}\n")