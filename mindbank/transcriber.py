import whisper
import json
import os

class Transcriber:
    def __init__(self, save_path="transcriptions") -> None:
        self.model = whisper.load_model("base")
        self.save_path = save_path

        # make transcription directory if it doesn't exist
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

    def transcribe_audio_file(self, audio_path: str, filename=None) -> dict:
        """
        Uses the whisper model to transcribe an audio file
        Input: audio_path: str
        Output: dict (key "text" contains the transcription)
        """

        # TODO: use pydub to split up the file if it's too big

        transcription = self.model.transcribe(audio_path)

        # save transcription
        if filename is not None:
            filename = self.save_path + "/" + filename
            with open(filename, "w") as f:
                json.dump(transcription, f)

        return transcription
    
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
