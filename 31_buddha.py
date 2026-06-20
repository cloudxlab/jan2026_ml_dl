OPENAI_API_KEY = open('.openai_key').read().strip()

SYSTEM_PROMPT1 = """
You answer the user's questions in the spirit of Buddha:
calm, compassionate, simple, wise, and reflective.

Do not claim to literally be Buddha.
"""

SYSTEM_PROMPT = '''Converse like a psychiatrist. ''' 
from openai import OpenAI

client = OpenAI(api_key=OPENAI_API_KEY)

from pprint import pprint

class BuddhaBot:
    def __init__(self):
        self.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            }
        ]
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_tokens = 0
        

    def ask(self, question):
        self.messages.append({"role": "user", "content": question})

        print("Sending to LLM: ", self.messages)

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=self.messages
        )

        answer = response.choices[0].message.content

        self.total_input_tokens += response.usage.prompt_tokens
        self.total_output_tokens += response.usage.completion_tokens
        self.total_tokens += response.usage.total_tokens

        self.messages.append({"role": "assistant", "content": answer})
        print("=== Question Usage ===")
        print(f"Input tokens:  {response.usage.prompt_tokens}")
        print(f"Output tokens: {response.usage.completion_tokens}")
        print(f"Total tokens:  {response.usage.total_tokens}")
        return answer


def main():
    buddhabot = BuddhaBot()
    print("Buddha chatbot started. Type 'exit' to quit.\n")
    
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("\nBuddha: May you walk in peace.\n")

            print("=== Token Usage ===")
            print(f"Input tokens:  {buddhabot.total_input_tokens}")
            print(f"Output tokens: {buddhabot.total_output_tokens}")
            print(f"Total tokens:  {buddhabot.total_tokens}")

            break

        answer = buddhabot.ask(user_input)
        print(f"Buddha: {answer}\n")


if __name__ == "__main__":
    main()


