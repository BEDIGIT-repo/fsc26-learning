# Exercises

1. **Zero-shot Prompting:**  
   Implement a function that uses a zero-shot prompt to classify a customer support ticket as "URGENT", "NORMAL", or "LOW" priority. The function should use an LLM (via LangChain) and take the ticket text as input, returning the predicted priority as a string. Do not provide any examples in the prompt.

2. **Few-shot Prompting:**  
   Implement a function that uses few-shot prompting to classify a customer support ticket as "URGENT", "NORMAL", or "LOW" priority. The function should use an LLM (via LangChain), include at least two example tickets and their priorities in the prompt, and return the predicted priority as a string.

3. **Structured Output with LLMs:**  
   Implement a function that uses an LLM with structured output (e.g., via Pydantic and LangChain) to classify a support ticket and extract structured information such as priority, title, and theme. The function should return the LLM's structured response as a Python object or dictionary.

4. **Chain of Thought Prompting:**  
   Implement a function that solves a riddle using an LLM, both with and without Chain of Thought (CoT) prompting. The function should craft two prompts: one that asks for a direct answer, and one that encourages step-by-step reasoning. Return both responses as integers.