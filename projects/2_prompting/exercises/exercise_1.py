from dotenv import load_dotenv

load_dotenv()

def exercise_1(ticket_text: str) -> str:
    """
    Classify a customer support ticket as 'URGENT', 'NORMAL', or 'LOW' priority using zero-shot prompting.
    Args:
        ticket_text (str): The text of the customer support ticket.
    Returns:
        str: LLM's response.
    """

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
        llm_response = exercise_1(ticket)
        print(f"Example {i}: {ticket}\nLLM's Response: {llm_response}\n")