import pyaudio
import wave
import keyboard
import os
import threading

class AudioRecorder:
    def __init__(self, filename="output.wav"):
        self.filename = filename
        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 44100
        self.p = pyaudio.PyAudio()
        self.frames = []
        self.stream = None
        self.is_recording = False

    def set_filename(self, filename):
        """
        Sets the filename of the recording
        Input: filename (str)
        """
        self.filename = filename

    def start_recording(self):
        """
        Starts recording audio
        """
        # make recording directory if it doesn't exist
        if not os.path.exists("recordings"):
            os.makedirs("recordings")

        # record
        if not self.is_recording:
            self.is_recording = True
            self.frames = []
            self.stream = self.p.open(format=self.format,
                                      channels=self.channels,
                                      rate=self.rate,
                                      input=True,
                                      frames_per_buffer=self.chunk)

            print("Recording started...")
            threading.Thread(target=self.record).start()

    def record(self):
        """
        Records audio
        """
        while self.is_recording:
            data = self.stream.read(self.chunk)
            self.frames.append(data)

    def stop_recording(self):
        """
        Stops recording audio
        """
        if self.is_recording:
            self.is_recording = False
            self.stream.stop_stream()
            self.stream.close()

            save_path = os.path.join("recordings", self.filename)
            wf = wave.open(save_path, 'wb')
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.p.get_sample_size(self.format))
            wf.setframerate(self.rate)
            wf.writeframes(b''.join(self.frames))
            wf.close()

            print(f"Recording stopped. Audio saved as {self.filename}")

    def cleanup(self):
        self.p.terminate()

    @staticmethod
    def print_menu():
        """
        Prints the demo menu
        """
        print("Press 'a' to start recording")
        print("Press 's' to stop recording")

if __name__ == "__main__":
    recorder = AudioRecorder()

    try:
        recorder.print_menu()
        while True:
            if keyboard.is_pressed('a'):
                recorder.start_recording()
                keyboard.wait('s')
                recorder.stop_recording()
    except KeyboardInterrupt:
        recorder.cleanup()
        print("Exiting...")
