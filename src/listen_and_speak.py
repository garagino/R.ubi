from pyttsx3 import init
import speech_recognition as sr

class ListenAndSpeak:
    def __init__(self) -> None:
        self.__engine = init()
        self.__voice = self.__engine.getProperty('voices')[0]
        self.__speed_voice = 250
        self.__volume_voice = 1

        self.__microfone = sr.Recognizer()

    def speak(self, texto:str):
        self.__engine.setProperty('rate', self.__speed_voice)
        self.__engine.setProperty('volume', self.__volume_voice)
        self.__engine.setProperty('voice', self.__voice)
        self.__engine.say(texto)
        self.__engine.runAndWait()
    
    def listen(self):
        with sr.Microphone() as source:
            self.__microfone.adjust_for_ambient_noise(source, duration=0.8)
            print('Ouvindo')
            audio = self.__microfone.listen(source)
        
        try:
            phrase = self.__microfone.recognize_google(audio, language='pt-BR')
            print(f'Você disse: {phrase}')
            return f'Você disse: {phrase}'
        except sr.UnknownValueError:
            phrase = ''
            print('Não entendi o que você disse')
            return 'Não entendi o que você disse'



