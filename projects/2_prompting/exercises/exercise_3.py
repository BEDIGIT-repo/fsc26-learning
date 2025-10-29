from dotenv import load_dotenv

load_dotenv()

def exercise_3(ticket_text: str) -> str:
    """
    Use LLMs with structured outputs to classify a support ticket and extract structured information.
    Args:
        ticket_text (str): The text of the customer support ticket.
    Returns:
        str: LLM's structured response.
    """

    # Doc: https://python.langchain.com/docs/how_to/structured_output/#the-with_structured_output-method
    
    ##################
    # YOUR CODE HERE #
    ##################

    pass


if __name__ == "__main__":
    tickets = [
        "My internet connection has been down for hours and I need it for work. Please help!",
        "I would like to change my billing address for future invoices.",
        "The printer in the office is making a strange noise, but it still works."
    ]
    for i, ticket in enumerate(tickets, 1):
        llm_response = exercise_3(ticket)
        print(f"Example {i}: {ticket}\nLLM's Response: {llm_response}\n")