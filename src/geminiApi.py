import google.generativeai as genai
from decouple import config
import markdown

class GeminiApi:
    def __init__(self):
        # Definindo a chave de API
        self.GOOGLE_API_KEY = config('TOKEN')
        # Configurando a chave de API
        genai.configure(api_key=self.GOOGLE_API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')
    
    def generate_content(self, prompt):
        # Metodo para gerar conteudo
        prompt_base = 'Considere que seu nome é Rubi e você é um assistente virtual. Você está conversando com uma pessoa.\
            Ajude-a com o que ela precisar. Seja gentil e educado. Não compartilhe informações pessoais. Responda como se fosse uma conversa fluída\
            responda com no maximo 100 caracteres.\
            Ela disse o seguinte: '
        response = self.model.generate_content(prompt_base + prompt)
        return markdown.markdown(response.text)

# Exemplo de uso
'''gemini = GeminiApi()
pergunta = input("Pergunte algo: ")
print(gemini.generate_content(pergunta))'''