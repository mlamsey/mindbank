from datetime import datetime

from transcriber import Transcriber
from recorder import AudioRecorder

class MindBank:
    def __init__(self):
        print("INITIALIZING MIND BANK")
        self.transcriber = Transcriber()
        self.recorder = AudioRecorder()
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
        """
        print(f"Transcribing {conversation_filename}...")
        return self.transcriber.transcribe_audio_file(conversation_filename)
    
if __name__ == '__main__':
    mindbank = MindBank()
    try:
        while True:
            if not input("Press enter to record a conversation..."):
                mindbank.record_conversation()
            if not input("Press enter to transcribe the recording..."):
                conversation_filename = mindbank.recorder.filename
                transcription = mindbank.transcribe_conversation(conversation_filename)
                print(transcription["text"])
    except KeyboardInterrupt:
        pass
