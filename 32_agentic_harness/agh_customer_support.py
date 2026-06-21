OPENAI_API_KEY = open('../.openai_key').read().strip()

import os
from openai import OpenAI

client = OpenAI(api_key=OPENAI_API_KEY)


BASE_PROMPT_TEMPLATE = """
Answer the user's question.

User's Question: {user_question}

Here is the list of documents:
{document_list}

You can do one of the following things only:

1. Answer the user's question:
ANSWER: <answer>

2. Ask user a clarification question:
ASKUSER: <question>

3. Read a file:
READFILE: <filename.txt>

Important:
- Output only one line.
- Do not explain.
- Do not use any format other than ANSWER, ASKUSER, or READFILE.
"""


def build_document_list(documents: dict[str, str]) -> str:
    lines = []

    for filename, description in documents.items():
        lines.append(f"{filename}: {description}")

    return "\n".join(lines)


def call_llm(prompt: str, model: str = "gpt-5.5") -> str:
    response = client.responses.create(
        model=model,
        input=prompt,
    )
    return response.output_text.strip()


def parse_action(response: str):
    response = response.strip()

    if response.startswith("ANSWER:"):
        return "ANSWER", response[len("ANSWER:"):].strip()

    if response.startswith("ASKUSER:"):
        return "ASKUSER", response[len("ASKUSER:"):].strip()

    if response.startswith("READFILE:"):
        return "READFILE", response[len("READFILE:"):].strip()

    return "INVALID", response


def read_file(file_name):
    return open(file_name).read()


def agentic_harness(
    user_question: str,
    document_descriptions: dict[str, str],
    max_steps: int = 20,
):
    context = ""

    document_list = build_document_list(document_descriptions)

    for step in range(max_steps):
        print(f"Step {step}")
        prompt = BASE_PROMPT_TEMPLATE.format(
            user_question=user_question,
            document_list=document_list,
        )

        if context:
            prompt += "\n\nContext so far:\n" + context
        
        print(f"Prompt: {prompt}")
        llm_output = call_llm(prompt)
        print(f"\nLLM: {llm_output}")

        action, value = parse_action(llm_output)
        
        if action == "ANSWER":
            return value

        elif action == "ASKUSER":
            user_reply = input(f"{value}\nUser: ")
            context += f"\nThe agent asked: {value}"
            context += f"\nThe user replied: {user_reply}"

        elif action == "READFILE":
            filename = value.strip()

            try:
                content_file = read_file(file_name=filename)
                context += f"\nContent of {filename}:\n{content_file}"
            except:                
                context += f"\nError: {filename} does not exist."

        else:
            context += f"""
The previous LLM output was invalid:
{value}

Please respond with exactly one of:
ANSWER: ...
ASKUSER: ...
READFILE: filename.txt
"""
    return "Failed: agent did not finish within max_steps."

if __name__ == "__main__":
    document_descriptions = {
        "file1.txt": "Contains the credit card limit details of the corporate users.",
        "file2.txt": "Contains the credit card limits and conditions of the individual users.",
        "file3.txt": "Contains the terms and conditions for approval of credit card.",
        "file4.txt": "reference credit limits"
    }
    while True:
        print(" I am credit card customer service agent! You can ask any questions.")
        question = input("Question: ")

        answer = agentic_harness(
            user_question=question,
            document_descriptions=document_descriptions,
        )
        print("\nFINAL ANSWER:")
        print(answer)
