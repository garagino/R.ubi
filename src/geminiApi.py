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
        response = self.model.generate_content(prompt)
        return markdown.markdown(response.text)

# Exemplo de uso
'''gemini = GeminiApi()
pergunta = input("Pergunte algo: ")
print(gemini.generate_content(pergunta))'''