import openai
import os

class ChatGPT:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.completion = openai.Completion()

    def generate_response(self, input_text, context):
        prompt = f"{input_text}\nResponse:"
        response = self.completion.create(
            engine="davinci",
            prompt=prompt,
            temperature=0.5,
            max_tokens=1024,
            n=1,
            stop=None,
            frequency_penalty=0,
            presence_penalty=0,
            context=context,
        )
        message = response.choices[0].text.strip()
        return message