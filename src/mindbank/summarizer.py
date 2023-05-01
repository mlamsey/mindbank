import openai
import json

def setup_api_key():
    # read api key from file
    with open("/Users/mlamsey/Documents/GT/HRL/mindbank/api-key.txt", "r") as f:
        api_key = f.read()

    openai.api_key = api_key

class Summarizer:
    def __init__(self):
        setup_api_key()
        # self.gpt_model = "gpt-3.5-turbo"
        self.gpt_model = "text-davinci-003"

    def generate_prompt(self, text=""):
        return """
        I transcribed human speech. The transcription is below. Summarize it.

        {}
        """.format(text)

    def summarize_text(self, text):
        response = openai.Completion.create(
                model=self.gpt_model,
                prompt=self.generate_prompt(),
                temperature=1,
            )

        return response
    
    def write_response_to_file(self, response_json, filename):
        json.dump(response_json, filename)

if __name__ == '__main__':
    text = """
    asdf
    """
    summarizer = Summarizer()
    summary = summarizer.summarize_text(text)
    filename = "test.json"
    summarizer.write_response_to_file(summary)