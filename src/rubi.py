'''Modulo principal do Rubi'''
from listen_and_speak import ListenAndSpeak
from geminiApi import GeminiApi

class Rubi(ListenAndSpeak, GeminiApi):
    '''Classe que representa o Rubi'''
    def __init__(self) -> None:
        ListenAndSpeak.__init__(self)
        GeminiApi.__init__(self)

    def conversation(self):
        '''Método para conversar com o usuário.
        funcionamento:
            - Ouve a pergunta do usuário;
            - Gera a resposta baseada na pergunta;
            - Fala a resposta.
            - Repete o processo até o usuário encerrar a conversa.
        '''
        voz = ['Masculina', 'Chris']
        while True:
            pergunta = self.listen()
            print(pergunta)

            if 'até mais' in pergunta.lower() or\
                  'tchau' in pergunta.lower() or\
                  'adeus' in pergunta.lower():

                print('Até mais! Foi um prazer conversar com você!')
                self.text_to_speech('Até mais! Foi um prazer conversar com você!', voz[0], voz[1])
                break

            if 'mude a voz' in pergunta.lower() or\
                    'troque de voz' in pergunta.lower() or\
                    'troque a voz' in pergunta.lower():
                
                if voz == ['Feminina', 'Serena']:
                    voz = ['Masculina', 'Chris']
                else:
                    voz = ['Feminina', 'Serena']

            resposta = self.generate_content(pergunta)
            print(resposta)
            self.text_to_speech(resposta, voz[0], voz[1])


rubi = Rubi()
rubi.conversation()

