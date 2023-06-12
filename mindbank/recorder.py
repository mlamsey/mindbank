import pyaudio
import wave
import os
import threading

class AudioRecorder:
    def __init__(self, filename="output.wav", prompt_for_input_device=True):
        self.filename = filename
        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 44100
        self.p = pyaudio.PyAudio()
        self.frames = []
        self.stream = None
        self.is_recording = False
        self.input_device_index = None

        # make recording directory if it doesn't exist
        if not os.path.exists("recordings"):
            os.makedirs("recordings")

        if prompt_for_input_device:
            self.prompt_for_input_device()

    def prompt_for_input_device(self):
        """
        Prompts the user to select an input device
        """
        while True:
            print("Input devices:")
            for i in range(self.p.get_device_count()):
                print(f"{i}: {self.p.get_device_info_by_index(i)['name']}")
            index = int(input("Select an input device, or enter Q to cancel: "))
            if index == "Q":
                return
            elif index >= 0 and index < self.p.get_device_count():
                self.set_input_device_index(index)
                break

    def set_input_device_index(self, index):
        """
        Sets the input device index
        Input: index (int)
        """
        self.input_device_index = index

    def set_filename(self, filename):
        """
        Sets the filename of the recording
        Input: filename (str)
        """
        self.filename = "recordings/" + filename

    def start_recording(self):
        """
        Starts recording audio
        """
        # record
        if self.input_device_index is not None:
            if not self.is_recording:
                self.is_recording = True
                self.frames = []
                self.stream = self.p.open(format=self.format,
                                        channels=self.channels,
                                        rate=self.rate,
                                        input=True,
                                        frames_per_buffer=self.chunk,
                                        input_device_index=self.input_device_index)

                print("Recording started...")
                threading.Thread(target=self.record).start()
        else:
            print("recorder::start_recording: No input device selected. Run prompt_for_input_device() to select an input device.")

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

            save_path = self.filename
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
    import keyboard

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
