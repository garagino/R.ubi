'''Modulo responsavel pela integração com a API Gemini da Google.'''
from decouple import config
import google.generativeai as genai

class GeminiApi:
    '''Classe responsavel pela integração com a API Gemini da Google.'''
    def __init__(self):
        self.GOOGLE_API_KEY = config('TOKEN') # Definindo a chave de API
        genai.configure(api_key=self.GOOGLE_API_KEY) # Configurando a chave de API
        self.model = genai.GenerativeModel('gemini-pro') # Definindo o modelo de linguagem

        # Definindo o prompt base
        prompt_base = 'Considere que seu nome é Rubi e você é um assistente virtual.\
            Você está conversando com uma pessoa.\
            Ajude-a com o que ela precisar. Seja gentil e educado. Não compartilhe informações pessoais. Responda como se fosse uma conversa fluída\
            responda com no maximo 100 caracteres. Seja claro e objetivo. Não use palavras de baixo calão. Não seja ofensivo. Não seja preconceituoso.\
            Tente ser o mais humano possível. Não use pronomes pessoais.\
            Esta pessoa disse o seguinte: '

        self.message = [{'parts':[prompt_base], 'role': 'user'}] # Define o primeiro prompt de ctxt
        response = self.model.generate_content(self.message) # Gera a resposta baseada no contexto
        self.message.append(response.candidates[0].content) # Adiciona a resposta ao contexto

    def generate_content(self, prompt:str):
        '''Método que gera conteúdo baseado em um prompt.
        funcionamento:
            - Adiciona o prompt ao contexto;
            - Gera a resposta baseada no contexto;
            - Adiciona a resposta ao contexto.
            - Retorna a resposta em texto.
        Args:
            prompt (str): Prompt para gerar a resposta.
        '''
        self.message.append({'parts':[prompt], 'role': 'user'}) # Adiciona o novo prompt ao contexto

        response = self.model.generate_content(self.message) # Gera a resposta baseada no contexto
        self.message.append(response.candidates[0].content) # Adiciona a resposta ao contexto
        return response.text # Retorna a resposta em texto
