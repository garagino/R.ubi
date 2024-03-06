from listen_and_speak import ListenAndSpeak
from geminiApi import GeminiApi

class Rubi(ListenAndSpeak, GeminiApi):
    def __init__(self) -> None:
        ListenAndSpeak.__init__(self)
        GeminiApi.__init__(self)
    
    def conversation(self):
        while True:
            pergunta = self.listen()
            print(pergunta)

            if 'até mais' in pergunta.lower() or 'tchau' in pergunta.lower() or 'adeus' in pergunta.lower():
                print('Até mais! Foi um prazer conversar com você!')
                self.text_to_speech('Até mais! Foi um prazer conversar com você!')
                self.play_audio()
                break

            resposta = self.generate_content(pergunta)
            print(resposta)
            self.text_to_speech(resposta)
            self.play_audio()


rubi = Rubi()
rubi.conversation()

