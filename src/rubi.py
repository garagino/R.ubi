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
                self.speak('Até mais!')
                break

            resposta = self.generate_content(pergunta)
            print(resposta)
            self.speak(resposta)


rubi = Rubi()
rubi.conversation()
