import openai
import json

def setup_api_key():
    # read api key from file
    with open("/nethome/mlamsey3/HRL/mindbank/api-key.txt", "r") as f:
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
        prompt = self.generate_prompt(text)
        response = openai.Completion.create(
                model=self.gpt_model,
                prompt=prompt,
                temperature=1,
                max_tokens=2048
            )

        return response
    
    def write_response_to_file(self, response_json, filename):
        with open(filename, "w") as f:
            json.dump(response_json, f)

    def print_response(self, response):
        text = response["choices"][0]["text"]
        print(text)

if __name__ == '__main__':
    text = """
    Unix is a family of multitasking, multiuser computer operating systems that derive from the original AT&T Unix, whose development started in 1969[1] at the Bell Labs research center by Ken Thompson, Dennis Ritchie, and others.[4]

    Initially intended for use inside the Bell System, AT&T licensed Unix to outside parties in the late 1970s, leading to a variety of both academic and commercial Unix variants from vendors including University of California, Berkeley (BSD), Microsoft (Xenix), Sun Microsystems (SunOS/Solaris), HP/HPE (HP-UX), and IBM (AIX). In the early 1990s, AT&T sold its rights in Unix to Novell, which then sold the UNIX trademark to The Open Group, an industry consortium founded in 1996. The Open Group allows the use of the mark for certified operating systems that comply with the Single UNIX Specification (SUS).

    Unix systems are characterized by a modular design that is sometimes called the "Unix philosophy". According to this philosophy, the operating system should provide a set of simple tools, each of which performs a limited, well-defined function.[5] A unified and inode-based filesystem (the Unix filesystem) and an inter-process communication mechanism known as "pipes" serve as the main means of communication,[4] and a shell scripting and command language (the Unix shell) is used to combine the tools to perform complex workflows.

    Unix distinguishes itself from its predecessors as the first portable operating system: almost the entire operating system is written in the C programming language, which allows Unix to operate on numerous platforms.[6] 
    """
    summarizer = Summarizer()
    summary = summarizer.summarize_text(text)
    summarizer.print_response(summary)
    filename = "test.json"
    summarizer.write_response_to_file(summary, filename)