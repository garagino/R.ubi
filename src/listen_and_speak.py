'''Módulo que contém a classe ListenAndSpeak, responsável por ouvir e falar com o usuário. V1.0.0'''
from pyttsx3 import init
import speech_recognition as sr

class ListenAndSpeak:
    '''Classe responsável por transformar texto em voz e voz em texto.'''
    def __init__(self) -> None:
        self.__engine = init()
        self.__voice = self.__engine.getProperty('voices')[0]
        self.__speed_voice = 250
        self.__volume_voice = 1

        self.__microfone = sr.Recognizer()

    def speak(self, texto:str):
        '''Método que transforma string em voz.
        Funcionamento:
            - Configura a velocidade da voz;
            - Configura o volume da voz;
            - Configura o tipo de voz;
            - Fala o texto.
            - Trava a excecução do código e aguarda a voz terminar de falar.
        Args:
            texto (str): Texto a ser transformado em voz.
        '''
        self.__engine.setProperty('rate', self.__speed_voice)
        self.__engine.setProperty('volume', self.__volume_voice)
        self.__engine.setProperty('voice', self.__voice)
        self.__engine.say(texto)
        self.__engine.runAndWait()

    def listen(self):
        '''Método que transforma voz em string.
        Funcionamento:
            - Configura o microfone;
            - Configura o tempo de duração do ajuste do microfone para se adequar ao ruído ambiente;
            - Aguarda a voz ser reconhecida.
        Returns:
            str: String com a voz reconhecida.
        '''
        with sr.Microphone() as source:
            self.__microfone.adjust_for_ambient_noise(source, duration=0.8)
            print('Ouvindo')
            audio = self.__microfone.listen(source)

        try:
            phrase = self.__microfone.recognize_google(audio, language='pt-BR')
            return phrase
        except sr.UnknownValueError:
            phrase = ''
            return 'Audio não reconhecido'
