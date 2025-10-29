from dotenv import load_dotenv
from typing import Tuple

load_dotenv()


def exercise_4(riddle: str) -> Tuple[int, int]:
    """
    Solves a riddle with and without Chain of Thought prompting.
    Args:
        riddle (str): Riddle for the llm to solve
    Returns:
        Tuple[int, int]: A tuple containing the responses with and without CoT
    """

    ##################
    # YOUR CODE HERE #
    ##################
    # You should craft 2 prompts that send the riddle to the llm:
    #   1. First one forces the llm to not think and answer directly
    #   2. Second one forces the llm to think step by step
    # You should make 2 calls to the llm api and have to results to
    # send as a tuple of int ("return resultA, resultB")
    # Tip: Use .with_structured_output

    pass


if __name__ == "__main__":
    riddle = "When I was 4 years old, my partner was 3 times my age. Now, I am 20 years old. How old is my partner?"
    llm_response_without_cot, llm_response_with_cot = exercise_4(riddle)

    print(f"Without Chain of Thought: {llm_response_without_cot}\n")
    print(f"With Chain of Thought: {llm_response_with_cot}\n")