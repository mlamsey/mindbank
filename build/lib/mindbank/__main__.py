import argparse
import sys

from mindbank.mindbank import MindBank
from mindbank.transcriber import Transcriber
from mindbank.recorder import AudioRecorder
from mindbank.summarizer import Summarizer

def main():
    # parse arguments
    parser = argparse.ArgumentParser(description="M I N D B A N K")
    parser.add_argument("--token", help="path to Chat GPT token")

    args = parser.parse_args()
    if not args.token:
        print("mindbank::__main__: Please specify a token using --token")
        sys.exit()

    # main
    mindbank = MindBank()
    summarizer = Summarizer(args.token)
    try:
        while True:
            if not input("Press enter to record a conversation..."):
                mindbank.record_conversation()
            if not input("Press enter to transcribe the recording..."):
                conversation_filename = mindbank.recorder.filename
                transcription = mindbank.transcribe_conversation(conversation_filename)
                text = transcription["text"]
                summary = summarizer.summarize_text(text)
                print(summary)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()