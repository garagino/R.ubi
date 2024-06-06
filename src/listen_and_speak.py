'''Módulo que contém a classe ListenAndSpeak, responsável por ouvir e falar com o usuário. V1.0.0'''
import speech_recognition as sr
from decouple import config
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from io import BytesIO
from pydub import AudioSegment, playback
import requests

class ListenAndSpeak:
    '''Classe responsável por transformar texto em voz e voz em texto.'''
    def __init__(self):
        self.__microfone = sr.Recognizer()

        # Configuração do cliente ElevenLabs
        self.eleven_client = ElevenLabs(api_key=config('ELEVENLABS_API_KEY'))

        # Dicionário com as vozes disponíveis (Acesso: self.vozes['Masculina']['Chris'])
        self.vozes = {
            'Masculina': {
                'Chris': 'iP95p4xoKVk53GoZ742B', #  Muito bom, parece uma pessoa mesmo
                'Josh': 'TxGEqnHWrfWFTfGW9XjX', # Bom, porém bem sério             
                'JoãoPedro': '7u8qsX4HQsSHJ0f8xsQZ' #  Muito bom, parece uma pessoa mesmo
            },
            'Feminina': {
                'Matilda': 'XrExE9yKIg1WjnnlVkGX', # Bom, bem animada, mas um pouco robótica
                'Serena': 'pMsXgVXv3BLzUgSXRplE', #  Bom, porem meio robótico
            }
        }
    
    def get_voices(self):
        '''Método que exibe todas as vozes disponíveis.'''
        url = "https://api.elevenlabs.io/v1/voices"
        headers = {
            "Accept": "application/json",
            "xi-api-key": config('ELEVENLABS_API_KEY'),
            "Content-Type": "application/json"
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        for voice in data['voices']:
            print(f"{voice['name']}; {voice['voice_id']}")


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

    def text_to_speech(self, text:str, voice_gender:str ='Masculina', voice_id:str='Chris'):
        '''Método que transforma texto em voz.
        Funcionamento:
            - Sintetiza o texto em fala;
            - Salva o áudio sintetizado em um arquivo;
        Args:
            text (str): Texto a ser transformado em voz.
            voice_id (str, optional): Voz a ser utilizada. Defaults to 'Chris'.
        
        Modelo de vozes disponíveis:
            Chris,Josh, Matilda, Serena, JoãoPedro
        '''
        # Sintetiza o texto em fala
        response = self.eleven_client.text_to_speech.convert(
            voice_id=self.vozes[voice_gender][voice_id],
            optimize_streaming_latency="0",
            output_format="mp3_22050_32",
            text=text,
            model_id="eleven_multilingual_v2",
            voice_settings=VoiceSettings(
                stability=0.0,
                similarity_boost=0.5,
                style=0.0,
                use_speaker_boost=True,
            ),
        )

        # Salva o áudio sintetizado em um array de bytes
        audio_bytes = BytesIO()
        for chunk in response:
            if chunk:
                audio_bytes.write(chunk)
        
        audio_bytes.seek(0)

        # Reproduz o áudio
        playback.play(AudioSegment.from_file(audio_bytes, format="mp3"))
