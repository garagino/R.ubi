from elevenlabs import VoiceSettings, play
from elevenlabs.client import ElevenLabs
from decouple import config
import requests

ELEVENLABS_API_KEY = config('ELEVENLABS_API_KEY')

vozes = {
    'Chris': 'iP95p4xoKVk53GoZ742B', #  Muito bom, parece uma pessoa mesmo
    'Josh': 'TxGEqnHWrfWFTfGW9XjX', # Bom, porém bem sério 
    'Matilda': 'XrExE9yKIg1WjnnlVkGX', # Bom, bem animada, mas um pouco robótica
    'Serena': 'pMsXgVXv3BLzUgSXRplE', #  Bom, porem meio robótico
    'JoãoPedro': '7u8qsX4HQsSHJ0f8xsQZ' #  Muito bom, parece uma pessoa mesmo
}

client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

url = "https://api.elevenlabs.io/v1/voices"

headers = {
  "Accept": "application/json",
  "xi-api-key": ELEVENLABS_API_KEY,
  "Content-Type": "application/json"
}

def get_voices():
    response = requests.get(url, headers=headers)

    data = response.json()

    for voice in data['voices']:
        print(f"{voice['name']}; {voice['voice_id']}")

def text_to_speech_file(text: str) -> str:
    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id=vozes['Matilda'], # Adam pre-made voice
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_multilingual_v2", # use the turbo model for low latency, for other languages use the `eleven_multilingual_v2`
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )

    save_file_path = "output.mp3"

    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: A new audio file was saved successfully!")

    # Return the path of the saved audio file
    return save_file_path

text_to_speech_file(
    "Olá, sou o primeiro teste de voz para o novo Rubi. Sou super simples de ser utilizado e estou ansioso para ser integrado em novos projetos.\
        Será um prazer trabalhar com vocês: Iza, Lucas, Letícia e Mariá!"
    )
