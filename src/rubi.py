from listen_and_speak import ListenAndSpeak
from gptApi import GptApi

class Rubi(ListenAndSpeak):
    def __init__(self) -> None:
        super().__init__()
    
    def talk(self, inputs:list, outputs:list):
        speech = self.listen().lower()
        if speech == 'não entendi o que você disse':
            return self.speak('Desculpe, não entendi o que você disse')
        print(speech)
        for word in inputs:
            if speech in word:
                return self.speak(outputs[inputs.index(word)])
        
        return self.speak('Desculpe, ainda não sei responder isso')

rubi = Rubi()
