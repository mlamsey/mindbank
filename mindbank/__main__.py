import argparse
import sys

from mindbank import MindBank

def main():
    # parse arguments
    parser = argparse.ArgumentParser(description="M I N D B A N K")
    parser.add_argument("--token", help="path to Chat GPT token")

    args = parser.parse_args()
    if not args.token:
        print("mindbank::__main__: Please specify a token using --token")
        sys.exit()

    # main
    mindbank = MindBank(args.token)

    try:
        while True:
            if not input("Press enter to record a conversation..."):
                mindbank.record_conversation()
            if not input("Press enter to transcribe the recording..."):
                conversation_filename = mindbank.recorder.filename
                transcription = mindbank.transcribe_conversation(conversation_filename)
                text = transcription["text"]
                summary = mindbank.summarize_text(text)
                mindbank.print_response(summary)
                
                # TODO: create dynamic filename
                mindbank.write_response_to_file(summary, "mindbank.txt")
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()