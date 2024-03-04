from listen_and_speak import ListenAndSpeak
from geminiApi import GeminiApi

class Rubi(ListenAndSpeak, GeminiApi):
    def __init__(self) -> None:
        ListenAndSpeak.__init__(self)
        GeminiApi.__init__(self)

rubi = Rubi()

rubi.speak('Olá pessoa! Meu nome é Rubi! E estou aqui para te ajudar!')
pergunta = rubi.listen()
print(pergunta)

resposta = rubi.generate_content(pergunta)
print(resposta)
rubi.speak(resposta)
