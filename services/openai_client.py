from openai import OpenAI

class OpenAIClient:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def query_llm(self, user_query, model="gpt-4o-2024-08-06"):
        return self.client.beta.chat.completions.parse(
            model=model,
            messages=[
                {"role": "system", "content": "You are a data assistant."},
                {"role": "user", "content": user_query},
            ]
        )
