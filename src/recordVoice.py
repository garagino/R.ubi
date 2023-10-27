import wave
from pyaudio import PyAudio, paInt16

class RecordVoice:
    def __init__(self):
        self.__input = True
        self.__format = paInt16
        self.__channel = 1
        self.__rate = 44000
        self.__frames_buffer = 1024
        self.__frames = []
        self.__audio = PyAudio()
    
    def __recording(self):
        stream = self.__audio.open(
            input=self.__input,
            format=self.__format,
            channels=self.__channel,
            rate=self.__rate,
            frames_per_buffer=self.__frames_buffer
        )

        # Bolar outra forma de interromper a captura
        try:
            while True:
                bloco = stream.read(self.__frames_buffer)
                self.__frames.append(bloco)
        except KeyboardInterrupt:
            pass
            
        return stream
    
    def create_record(self):
        stream = self.__recording()

        stream.start_stream()
        stream.close()
        self.__audio.terminate()

        with wave.open('recording.wav', 'wb') as rec:
            rec.setnchannels(self.__channel)
            rec.setframerate(self.__rate)
            rec.setsampwidth(self.__audio.get_sample_size(self.__format))
            rec.writeframes(b''.join(self.__frames))
    
