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
    f = "/Users/mlamsey/Documents/GT/HRL/mindbank/src/mindbank/conversation_20230501_145504.wav"
    transcriber = Transcriber()
    print(transcriber.transcribe_audio_file(f)["text"])
