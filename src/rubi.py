from listen_and_speak import ListenAndSpeak
from geminiApi import GeminiApi

class Rubi(ListenAndSpeak, GeminiApi):
    def __init__(self) -> None:
        ListenAndSpeak.__init__(self)
        GeminiApi.__init__(self)

rubi = Rubi()

while True:
    pergunta = rubi.listen()
    print(pergunta)

    if 'até mais' in pergunta.lower():
        rubi.speak('Até mais!')
        break

    resposta = rubi.generate_content(pergunta)
    print(resposta)
    rubi.speak(resposta)
