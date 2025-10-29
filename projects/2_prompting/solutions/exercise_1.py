"""
Solution for Exercise 1: Zero-shot Prompting for Ticket Priority Classification using LangChain and Google LLM
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

def exercise_1(ticket_text: str) -> str:
    """
    Classify a customer support ticket as 'URGENT', 'NORMAL', or 'LOW' priority using zero-shot prompting and Google LLM via LangChain.
    Args:
        ticket_text (str): The text of the customer support ticket.
    Returns:
        str: LLM's response.
    """
    prompt_template = PromptTemplate(
        input_variables=["ticket_text"],
        template=(
            "Classify the following customer support ticket as 'URGENT', 'NORMAL', or 'LOW' priority.\n"
            "Ticket: {ticket_text}\n"
            "Priority:"
        )
    )
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")  
    # You can play with max_output_tokens  and temperature here
    # llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=1, max_output_tokens=3)
    result = llm.invoke(prompt_template.format_prompt(ticket_text=ticket_text))
    return result.content

if __name__ == "__main__":
    tickets = [
        "My internet connection has been down for hours and I need it for work. Please help!",
        "I would like to change my billing address for future invoices.",
        "The printer in the office is making a strange noise, but it still works."
    ]
    for i, ticket in enumerate(tickets, 1):
        llm_response = exercise_1(ticket)
        print(f"Example {i}: {ticket}\nLLM's Response: {llm_response}\n")