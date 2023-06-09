import openai
import json
import os

def setup_api_key(api_key_file=None):
    """
    Sets up the OpenAI API key in the openai module
    Input: api_key_file (str)
    """
    if api_key_file is None:
        print("summarizer::setup_api_key: Please specify an API key file")
        return

    # read api key from file
    api_key = None
    with open(api_key_file, "r") as f:
        api_key = f.read()
    
    # set api key
    if api_key is None:
        print("summarizer::setup_api_key: API key file is empty")
        return

    openai.api_key = api_key

class Summarizer:
    def __init__(self, api_key_file=None):
        setup_api_key(api_key_file=api_key_file)
        # self.gpt_model = "gpt-3.5-turbo"
        self.gpt_model = "text-davinci-003"

    def generate_prompt(self, text=""):
        """
        Generates a prompt for the GPT model
        Input: text (str): text to summarize
        Output: prompt (str): prompt for the GPT model
        """
        return """
        Transcribed human speech is below. Summarize it.

        {}
        """.format(text)

    def summarize_text(self, text):
        """
        Uses the OpenAI API to summarize text
        Input: text (str): prompt for the GPT model
        Output: response (dict): response from the OpenAI API
        ["choices"][0]["text"] contains the summary
        """

        prompt = self.generate_prompt(text)
        response = openai.Completion.create(
                model=self.gpt_model,
                prompt=prompt,
                temperature=1,
                max_tokens=2048
            )

        return response
    
    def write_response_to_file(self, response_json, filename):
        """
        Writes the response to a file
        Inputs: response_json (dict): response from the OpenAI API
                filename (str): name of the file to write to
        """
        # check if summaries folder exists
        if not os.path.exists("summaries"):
            os.makedirs("summaries")

        # write response to file
        filename = "summaries/" + filename
        with open(filename, "w") as f:
            json.dump(response_json, f)

    def print_response(self, response):
        """
        Prints the API response text
        """
        text = response["choices"][0]["text"]
        print("""
        The summarized response is:
        
        {}
        """.format(text))

if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser()
    parser.add_argument("--token", type=str, default="api_key.txt", help="path to OpenAI API key")
    args = parser.parse_args()
    if not args.token:
        print("summarizer::__main__: Please specify an API key using --token")
        sys.exit()

    test_text = """
    Unix is a family of multitasking, multiuser computer operating systems that derive from the original AT&T Unix, whose development started in 1969[1] at the Bell Labs research center by Ken Thompson, Dennis Ritchie, and others.[4]

    Initially intended for use inside the Bell System, AT&T licensed Unix to outside parties in the late 1970s, leading to a variety of both academic and commercial Unix variants from vendors including University of California, Berkeley (BSD), Microsoft (Xenix), Sun Microsystems (SunOS/Solaris), HP/HPE (HP-UX), and IBM (AIX). In the early 1990s, AT&T sold its rights in Unix to Novell, which then sold the UNIX trademark to The Open Group, an industry consortium founded in 1996. The Open Group allows the use of the mark for certified operating systems that comply with the Single UNIX Specification (SUS).

    Unix systems are characterized by a modular design that is sometimes called the "Unix philosophy". According to this philosophy, the operating system should provide a set of simple tools, each of which performs a limited, well-defined function.[5] A unified and inode-based filesystem (the Unix filesystem) and an inter-process communication mechanism known as "pipes" serve as the main means of communication,[4] and a shell scripting and command language (the Unix shell) is used to combine the tools to perform complex workflows.

    Unix distinguishes itself from its predecessors as the first portable operating system: almost the entire operating system is written in the C programming language, which allows Unix to operate on numerous platforms.[6] 
    """

    summarizer = Summarizer(api_key_file=args.token)
    summary = summarizer.summarize_text(test_text)
    summarizer.print_response(summary)
    filename = "test.json"
    summarizer.write_response_to_file(summary, filename)