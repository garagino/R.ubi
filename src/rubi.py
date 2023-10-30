from listen_and_speak import ListenAndSpeak
from gptApi import GptApi

class Rubi(ListenAndSpeak, GptApi):
    def __init__(self) -> None:
        ListenAndSpeak.__init__(self)
        GptApi.__init__(self)
