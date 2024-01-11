from rubi import Rubi

rubi = Rubi()

rubi.speak('Olá pessoa! Meu nome é Rubi! E estou aqui para te ajudar!')

primeira_interacao = rubi.listen()
print(primeira_interacao)

if 'susto' in primeira_interacao:
    rubi.speak('Desculpa, eu não quis te assustar! Eu sou o Rubi, um ambiente ubíquo.\
               Isso quer dizer que eu sou toda essa sala que nós estamos!')

    rubi.speak('Eu posso criar um lembrete pra você! É só você falar "criar lembrete"')

while True:
    segunda_interacao = rubi.listen()
    print(segunda_interacao)

    if 'lembrete' in segunda_interacao.lower() and 'criar' in segunda_interacao.lower() or 'sim' in segunda_interacao.lower() or 'quero' in segunda_interacao.lower() or 'crie' in segunda_interacao.lower():
        rubi.speak('Ok, qual o lembrete?')
        terceira_interacao = rubi.listen()
        print(terceira_interacao)

        with open('lembrete.txt', 'a') as f:
            f.write(terceira_interacao + '\n')
        
        rubi.speak('Ok, lembrete criado!')
        rubi.speak('Você quer que eu repita o lembrete?')
        quarta_interacao = rubi.listen()
        print(quarta_interacao)
        if 'sim' in quarta_interacao.lower() or 'quero' in quarta_interacao.lower() or 'repita' in quarta_interacao.lower():
            rubi.speak(f'Seu lembrete foi: {terceira_interacao}')
        
        rubi.speak('Você quer criar mais um lembrete?')
    
    elif 'encerrar' in segunda_interacao.lower() or 'sair' in segunda_interacao.lower() or 'não' in segunda_interacao:
        rubi.speak('Ok, até mais!')
        break

    else:
        rubi.speak('Desculpe. Ainda não sei fazer isso!')
        rubi.speak('Eu posso criar mais um lembrete pra você!')


