import whisper

class Transcriber:
    def __init__(self) -> None:
        self.model = whisper.load_model("base")

    def transcribe_audio_file(self, audio_path: str) -> dict:
        """
        Uses the whisper model to transcribe an audio file
        Input: audio_path: str
        Output: dict (key "text" contains the transcription)
        """
        return self.model.transcribe(audio_path)
    
if __name__ == '__main__':
    import argparse
    import sys
    
    # parse arguments
    parser = argparse.ArgumentParser(description="Transcriber")
    parser.add_argument("--audio", help="path to audio file")
    args = parser.parse_args()
    
    if not args.audio:
        print("transcriber::__main__: Please specify an audio file using --audio")
        sys.exit()

    transcriber = Transcriber()
    print(transcriber.transcribe_audio_file(args.audio)["text"])
