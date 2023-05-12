from datetime import datetime

from transcriber import Transcriber
from recorder import AudioRecorder
from summarizer import Summarizer

class MindBank:
    def __init__(self, api_key_file=None):
        print("INITIALIZING MIND BANK")
        self.transcriber = Transcriber()
        self.recorder = AudioRecorder()
        self.summarizer = Summarizer(api_key_file=api_key_file)
        print("MIND BANK INITIALIZED")

    def record_conversation(self):
        """
        Records a conversation and returns the transcription
        """
        # set filename as "conversation" + timestamp
        datetime_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = "conversation_" + datetime_str + ".wav"
        self.recorder.set_filename(filename)
        self.recorder.start_recording()
        input("Press enter to stop recording...")
        self.recorder.stop_recording()

    def transcribe_conversation(self, conversation_filename):
        """
        Transcribes a conversation and returns the transcription
        Output: transcription (dict): ["text"] contains the transcription
        """
        print(" ")
        print(f"Transcribing {conversation_filename}...")
        transcription = self.transcriber.transcribe_audio_file(conversation_filename)
        print("Transcription complete!")
        print(" ")
        return transcription
    
    def summarize_text(self, text):
        """
        Summarizes text and returns the summary
        Input: text (str): text to summarize
        Output: response (dict): response from the OpenAI API
        ["choices"][0]["text"] contains the summary
        """
        print(" ")
        print("Summarizing text...")
        summary = self.summarizer.summarize_text(text)
        print("Summary complete!")
        print(" ")
        return summary
    
    def print_response(self, response):
        """
        Prints the summary from the response
        Input: response (dict): response from the OpenAI API
        """
        self.summarizer.print_response(response)

    def write_response_to_file(self, response, filename):
        """
        Writes the summary from the response to a file
        Input: response (dict): response from the OpenAI API
        Input: filename (str): name of the file to write to
        """
        self.summarizer.write_response_to_file(response, filename)
    
if __name__ == '__main__':
    print("M I N D B A N K")
    print("Don't run me like this! Run me from main.py instead!")
    # import argparse
    # import sys
    # # parse arguments
    # parser = argparse.ArgumentParser(description="MindBank")
    # parser.add_argument("--token", help="path to Chat GPT token")

    # args = parser.parse_args()
    # if not args.token:
    #     print("mindbank::__main__: Please specify a token using --token")
    #     sys.exit()

    # # main
    # mindbank = MindBank()
    # summarizer = Summarizer(args.token)
    # try:
    #     while True:
    #         if not input("Press enter to record a conversation..."):
    #             mindbank.record_conversation()
    #         if not input("Press enter to transcribe the recording..."):
    #             conversation_filename = mindbank.recorder.filename
    #             transcription = mindbank.transcribe_conversation(conversation_filename)
    #             text = transcription["text"]
    #             summary = summarizer.summarize_text(text)
    # except KeyboardInterrupt:
    #     pass
