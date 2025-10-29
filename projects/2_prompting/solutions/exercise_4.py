"""
Solution for Exercise 4: Use Chain of Thought prompting and LLMs with structured 
    outputs to solve riddles asking for a number.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field


load_dotenv()


def exercise_4(riddle: str) -> str:
    """
    Solves a riddle with and without Chain of Thought prompting.
    Args:
        riddle (str): Riddle for the llm to solve
    Returns:
        int: LLM's structured response.
    """


    class RiddleResponse(BaseModel):
        """Response of the riddle"""
        number: int = Field(description="Response of the riddle")

    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash").with_structured_output(RiddleResponse)

    prompt_without_cot = f"{riddle} Return the answer directly without thinking."
    prompt_with_cot = f"{riddle} Let's think step by step."

    result_without_cot = llm.invoke(prompt_without_cot)
    result_with_cot = llm.invoke(prompt_with_cot)

    return result_without_cot, result_with_cot


if __name__ == "__main__":
    riddle = "When I was 4 years old, my partner was 3 times my age. Now, I am 20 years old. How old is my partner?"
    llm_response_without_cot, llm_response_with_cot = exercise_4(riddle)

    print(f"Without Chain of Thought: {llm_response_without_cot}\n")
    print(f"With Chain of Thought: {llm_response_with_cot}\n")